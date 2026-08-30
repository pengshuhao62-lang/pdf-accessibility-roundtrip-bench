from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

from reportlab.pdfgen import canvas

from pdfua_bench.compare import classify_outcome
from pdfua_bench.corpus import Corpus, CorpusError, load_corpus, verify_corpus_files
from pdfua_bench.models import FixtureSpec, StructuralSnapshot, ValidationResult
from pdfua_bench.process import run_command
from pdfua_bench.reports import json_text, markdown_text
from pdfua_bench.runner import run_case
from pdfua_bench.structure import compare_structure, inspect_structure
from pdfua_bench.validators import ValidationError, parse_verapdf_json


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class CorpusTests(unittest.TestCase):
    def test_public_corpus_has_twenty_fixtures_and_two_profiles(self) -> None:
        corpus = load_corpus(PROJECT_ROOT / "corpus/manifest.json")
        self.assertEqual(len(corpus.fixtures), 20)
        self.assertEqual(
            {fixture.profile for fixture in corpus.fixtures}, {"ua1", "ua2"}
        )
        self.assertEqual(sum("reference" in fixture.path for fixture in corpus.fixtures), 9)

    def test_public_corpus_files_have_matching_hashes_and_pages(self) -> None:
        corpus = load_corpus(PROJECT_ROOT / "corpus/manifest.json")
        self.assertEqual(verify_corpus_files(corpus), [])

    def test_corpus_rejects_path_escape(self) -> None:
        fixture = FixtureSpec(
            fixture_id="escape",
            profile="ua1",
            path="../outside.pdf",
            source="test",
            license="MIT",
            sha256="0" * 64,
            expected_pages=1,
            merge_partner="escape",
        )
        with tempfile.TemporaryDirectory(prefix="pdfua-corpus-") as directory:
            corpus = Corpus(Path(directory), (fixture,), Path(directory) / "manifest.json")
            with self.assertRaises(CorpusError):
                corpus.file_path(fixture)


class ValidatorTests(unittest.TestCase):
    def test_parse_compliant_verapdf_json(self) -> None:
        payload = json.dumps(
            {
                "report": {
                    "jobs": [
                        {
                            "validationResult": [
                                {"compliant": True, "details": {"failedRules": 0}}
                            ]
                        }
                    ]
                }
            }
        )
        self.assertEqual(parse_verapdf_json(payload), (True, ()))

    def test_parse_failed_verapdf_rule(self) -> None:
        payload = json.dumps(
            {
                "report": {
                    "jobs": [
                        {
                            "validationResult": [
                                {
                                    "compliant": False,
                                    "details": {
                                        "ruleSummaries": [
                                            {
                                                "status": "failed",
                                                "clause": "8.8",
                                                "testNumber": 2,
                                            }
                                        ]
                                    },
                                }
                            ]
                        }
                    ]
                }
            }
        )
        self.assertEqual(parse_verapdf_json(payload), (False, ("8.8-2",)))

    def test_invalid_verapdf_json_is_rejected(self) -> None:
        with self.assertRaises(ValidationError):
            parse_verapdf_json("not-json")

    def test_failed_rule_is_classified_as_new_pdfua_violation(self) -> None:
        baseline = ValidationResult("ua1", True, (), "veraPDF", True)
        output = ValidationResult("ua1", False, ("7.1-1",), "veraPDF", True)
        before = StructuralSnapshot(1, True, True, 0, 0, True, True, 0)
        after = StructuralSnapshot(1, True, True, 0, 0, True, True, 0)
        self.assertEqual(
            classify_outcome(baseline, [output], before, [after], True, True),
            "new_pdfua_violation",
        )

    def test_validator_or_output_errors_are_not_reported_as_passes(self) -> None:
        baseline = ValidationResult("ua1", True, (), "veraPDF", True)
        output = ValidationResult(
            "ua1", False, (), "veraPDF", False, error="validator error"
        )
        before = StructuralSnapshot(1, True, True, 0, 0, True, True, 0)
        self.assertEqual(
            classify_outcome(baseline, [output], before, [], True, False),
            "transformation_failed",
        )


class StructureTests(unittest.TestCase):
    def test_structure_inspector_reads_a_pdf_without_text_extraction(self) -> None:
        with tempfile.TemporaryDirectory(prefix="pdfua-structure-") as directory:
            pdf_path = Path(directory) / "probe.pdf"
            document = canvas.Canvas(str(pdf_path))
            document.setTitle("Structure probe")
            document.drawString(72, 720, "Synthetic content")
            document.save()
            snapshot = inspect_structure(pdf_path)
        self.assertTrue(snapshot.readable)
        self.assertEqual(snapshot.page_count, 1)
        self.assertTrue(snapshot.title_present)

    def test_structure_compare_detects_tag_tree_loss(self) -> None:
        before = StructuralSnapshot(1, True, True, 1, 0, True, True, 1)
        after = StructuralSnapshot(1, False, False, 0, 0, True, True, 0)
        self.assertTrue(compare_structure(before, [after]))


class ProcessTests(unittest.TestCase):
    def test_process_does_not_use_shell(self) -> None:
        with tempfile.TemporaryDirectory(prefix="pdfua-process-") as directory:
            marker = Path(directory) / "created-by-injection"
            result = run_command(
                [
                    sys.executable,
                    "-c",
                    "import sys; print(sys.argv[1])",
                    "literal;touch;should-not-run",
                ],
                Path(directory),
                timeout_seconds=10,
            )
        self.assertEqual(result.returncode, 0)
        self.assertIn("literal;touch;should-not-run", result.stdout)
        self.assertFalse(marker.exists())

    def test_process_timeout_is_bounded(self) -> None:
        with tempfile.TemporaryDirectory(prefix="pdfua-process-") as directory:
            started = time.monotonic()
            result = run_command(
                [sys.executable, "-c", "import time; time.sleep(5)"],
                Path(directory),
                timeout_seconds=1,
            )
            elapsed = time.monotonic() - started
        self.assertTrue(result.timed_out)
        self.assertLess(elapsed, 5)


class RunnerTests(unittest.TestCase):
    def test_fake_adapter_runs_a_case_without_external_tools(self) -> None:
        corpus = load_corpus(PROJECT_ROOT / "corpus/manifest.json")
        fixture = next(
            item for item in corpus.fixtures if item.fixture_id == "ua1-paragraph-001"
        )

        class FakeValidator:
            def validate(self, pdf_path, profile, report_path, log_path):
                report_path.parent.mkdir(parents=True, exist_ok=True)
                report_path.write_text("{}", encoding="utf-8")
                log_path.write_text("", encoding="utf-8")
                return ValidationResult(profile, True, (), "fake-verapdf", True, report_path.name)

        class FakeAdapter:
            name = "pymupdf"

            def version(self):
                return "fake-pymupdf"

            def resave(self, input_path, output, workdir):
                shutil.copy2(input_path, output)
                return [output]

            def split(self, input_path, output_dir, workdir):
                output_dir.mkdir(parents=True, exist_ok=True)
                output = output_dir / "split-001.pdf"
                shutil.copy2(input_path, output)
                return [output]

            def merge(self, inputs, output, workdir):
                shutil.copy2(inputs[0], output)
                return [output]

        with tempfile.TemporaryDirectory(prefix="pdfua-runner-") as directory:
            result = run_case(
                corpus,
                fixture,
                FakeAdapter(),
                FakeValidator(),
                "resave",
                Path(directory),
                {},
            )
        self.assertEqual(result.classification, "passed")
        self.assertEqual(len(result.output_validation), 1)
        self.assertEqual(result.transformation.output_files, ("outputs/resaved.pdf",))


class ReportTests(unittest.TestCase):
    def test_report_serialization_does_not_require_absolute_paths(self) -> None:
        report = type(
            "Report",
            (),
            {
                "to_dict": lambda self, include_raw_paths=False: {
                    "schema_version": "0.1",
                    "cases": [],
                    "summary": {"total": 0},
                }
            },
        )()
        self.assertNotIn(str(PROJECT_ROOT), json_text(report))


if __name__ == "__main__":
    unittest.main()
