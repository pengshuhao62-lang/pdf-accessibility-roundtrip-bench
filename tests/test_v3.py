"""Synthetic safety/diagnostic tests; real-tool acceptance is recorded separately."""
import contextlib
import copy
import hashlib
import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from pypdf import PdfReader
from pdfua_bench.bundles import export_case, verify_bundle, reproduce_bundle, _read_json_bytes
from pdfua_bench.cli import main
from pdfua_bench.corpus import load_corpus
from pdfua_bench.diagnostics import extract_diagnostics, safe_context
from pdfua_bench.run_diff import compare_runs, comparison_exit_code
from pdfua_bench.toolchain import resolve_toolchain
from test_run_diff import report

ROOT = Path(__file__).resolve().parents[1]


def validation(context, count=1):
    return dict(compliant=False, details=dict(failedChecks=count, ruleSummaries=[
        dict(status="failed", clause="7.1", testNumber=1, failedChecks=count,
             checks=[dict(status="failed", context=context, errorMessage="PRIVATE TEXT")])]))


class DiagnosticTests(unittest.TestCase):
    def setUp(self):
        corpus = load_corpus(ROOT / "corpus/manifest.json")
        self.path = corpus.file_path(corpus.fixtures[0])
        ref = PdfReader(str(self.path)).pages[0].indirect_reference
        self.context = f"root/document[0]/pages[0]({ref.idnum} {ref.generation} obj PDPage)/font[0](PRIVATE FONT)"

    def test_verified_page_and_exact_evidence_pointer(self):
        checks, complete = extract_diagnostics(validation(self.context), self.path)
        self.assertTrue(complete)
        self.assertEqual(checks[0]["page"], 1)
        self.assertEqual(checks[0]["location_status"], "verified-page-object")
        self.assertEqual(checks[0]["report_pointer"], "/details/ruleSummaries/0/checks/0")
        self.assertNotIn("PRIVATE", json.dumps(checks))
        self.assertEqual(checks[0]["context_sha256"], hashlib.sha256(self.context.encode()).hexdigest())

    def test_wrong_object_or_index_is_unresolved(self):
        for context in (self.context.replace("pages[0]", "pages[99999]"),
                        "root/document[0]/pages[0](99999 0 obj PDPage)", "root/structureTree[0]"):
            checks, complete = extract_diagnostics(validation(context), self.path)
            self.assertTrue(complete)
            self.assertIsNone(checks[0]["page"])
            self.assertEqual(checks[0]["location_status"], "unresolved")

    def test_unreadable_pdf_never_yields_page(self):
        checks, complete = extract_diagnostics(validation(self.context), Path("missing.pdf"))
        self.assertTrue(complete)
        self.assertIsNone(checks[0]["page"])

    def test_truncated_or_malformed_diagnostics_fail_closed(self):
        samples = [validation(self.context, 2), dict(compliant=False),
                   dict(compliant=False, details=None), dict(compliant=False, details=dict(ruleSummaries=None))]
        for item in samples:
            with self.subTest(item=item):
                self.assertFalse(extract_diagnostics(item, self.path)[1])

    def test_complete_zero_failure_report(self):
        self.assertEqual(extract_diagnostics(dict(compliant=True, details=dict(failedChecks=0, ruleSummaries=[])), self.path), ((), True))

    def test_context_scrubs_unknown_text_and_parentheses(self):
        result = safe_context("root/private-secret(/Users/private)/font[0](Secret)/https://secret.com")
        self.assertNotIn("private", result)
        self.assertNotIn("secret", result)
        self.assertNotIn("Secret", result)


class BundleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.corpus = load_corpus(ROOT / "corpus/manifest.json")
        self.fixture = self.corpus.fixtures[0]
        self.report = report()
        self.report.update(schema_version="0.3", run_id="recorded-run")
        self.report["configuration"]["comparison_protocol"] = "pdfua-roundtrip-v3"
        self.case = self.report["cases"][0]
        self.case.update(fixture_id=self.fixture.fixture_id, case_id=self.fixture.fixture_id + "-qpdf-resave", profile=self.fixture.profile)
        for result in [self.case["baseline"], *self.case["output_validation"]]:
            result.update(profile=self.fixture.profile, diagnostics_complete=True, failed_checks=[])
        self.case["before_structure"]["page_count"] = self.fixture.expected_pages
        self.case["after_structure"][0]["page_count"] = self.fixture.expected_pages
        self.case["provenance"]["inputs"] = [dict(id=self.fixture.fixture_id, sha256=self.fixture.sha256, pages=self.fixture.expected_pages)]
        self.case["transformation"]["output_files"] = ["outputs/resaved.pdf"]
        self.case["provenance"]["outputs"] = [dict(path="outputs/resaved.pdf", sha256=self.fixture.sha256)]
        self.run_dir = self.root / "recorded-run"
        self.case_dir = self.run_dir / "cases" / self.case["case_id"]
        (self.case_dir / "outputs").mkdir(parents=True)
        (self.case_dir / "outputs/resaved.pdf").write_bytes(self.corpus.file_path(self.fixture).read_bytes())
        self.zip = self.root / "case.zip"

    def export(self, **overrides):
        args = dict(report=self.report, case_id=self.case["case_id"], corpus=self.corpus,
                    run_dir=self.run_dir, output=self.zip, include_pdfs=True)
        args.update(overrides)
        return export_case(**args)

    def rewrite(self, changes, name="modified.zip", rehash=False):
        with zipfile.ZipFile(self.zip) as source:
            items = {n: source.read(n) for n in source.namelist()}
        items.update(changes)
        if rehash:
            doc = json.loads(items["manifest.json"])
            doc["members"] = {n: dict(size=len(v), sha256=hashlib.sha256(v).hexdigest()) for n, v in items.items() if n != "manifest.json"}
            items["manifest.json"] = json.dumps(doc).encode()
        target = self.root / name
        with zipfile.ZipFile(target, "w") as archive:
            for n, data in items.items():
                archive.writestr(n, data)
        return target

    def test_export_verify_exact_members_and_licensing(self):
        self.export()
        manifest, evidence, members = verify_bundle(self.zip)
        self.assertEqual(manifest["case_id"], self.case["case_id"])
        self.assertEqual(len(members), 7)
        self.assertEqual(len(evidence["cases"]), 1)
        fixture = json.loads(members["corpus/manifest.json"])["fixtures"][0]
        self.assertEqual(fixture["license"], self.fixture.license)
        self.assertEqual(fixture["source"], self.fixture.source)
        self.assertEqual(fixture["merge_partner"], self.fixture.fixture_id)

    def test_requires_document_sharing_confirmation(self):
        with self.assertRaisesRegex(ValueError, "include-pdfs"):
            self.export(include_pdfs=False)
        self.assertFalse(self.zip.exists())

    def test_export_never_overwrites(self):
        self.export()
        original = self.zip.read_bytes()
        with self.assertRaises(FileExistsError):
            self.export()
        self.assertEqual(self.zip.read_bytes(), original)

    def test_changed_output_and_missing_fingerprints_rejected(self):
        (self.case_dir / "outputs/resaved.pdf").write_bytes(b"changed")
        with self.assertRaisesRegex(ValueError, "bytes differ"):
            self.export()
        self.case["provenance"]["outputs"] = []
        with self.assertRaises(ValueError):
            self.export()

    def test_wrong_run_and_incomplete_diagnostics_rejected(self):
        with self.assertRaisesRegex(ValueError, "run_id"):
            self.export(run_dir=self.root)
        self.case["output_validation"][0]["diagnostics_complete"] = False
        with self.assertRaises(ValueError):
            self.export()

    def test_unsafe_output_paths_rejected(self):
        self.case["transformation"]["output_files"] = ["../../private.pdf"]
        self.case["provenance"]["outputs"][0]["path"] = "../../private.pdf"
        with self.assertRaisesRegex(ValueError, "Unsafe"):
            self.export()

    def test_checksum_tamper_rejected(self):
        self.export()
        target = self.rewrite({"outputs/output-1.pdf": b"tamper"})
        with self.assertRaisesRegex(ValueError, "checksum"):
            verify_bundle(target)

    def test_rehashed_input_still_must_match_recorded_provenance(self):
        self.export()
        target = self.rewrite({"corpus/pdfs/input-1.pdf": b"tamper"}, rehash=True)
        with self.assertRaisesRegex(ValueError, "provenance"):
            verify_bundle(target)

    def test_traversal_extra_files_and_malformed_manifest_rejected(self):
        self.export()
        for changes in ({"../outside": b"x"}, {"run.sh": b"exit 0"}, {"manifest.json": b"[]"}):
            with self.subTest(changes=changes):
                with self.assertRaises(ValueError):
                    verify_bundle(self.rewrite(changes))

    def test_symlink_duplicate_and_size_limit_rejected(self):
        self.export()
        target = self.root / "symlink.zip"
        with zipfile.ZipFile(target, "w") as archive:
            info = zipfile.ZipInfo("manifest.json")
            info.external_attr = 0o120777 << 16
            archive.writestr(info, b"outside")
        with self.assertRaisesRegex(ValueError, "Symlink"):
            verify_bundle(target)
        with patch("pdfua_bench.bundles.MAX_BYTES", 10):
            with self.assertRaises(ValueError):
                verify_bundle(self.zip)
        with zipfile.ZipFile(self.zip, "a") as archive:
            with self.assertWarns(UserWarning):
                archive.writestr("manifest.json", b"{}")
        with self.assertRaises(ValueError):
            verify_bundle(self.zip)

    def test_environment_mismatch_stops_before_adapter(self):
        self.export()
        with patch("pdfua_bench.bundles.build_adapters") as adapters:
            with self.assertRaisesRegex(ValueError, "environment"):
                reproduce_bundle(self.zip, resolve_toolchain(), self.root / "reproduced.json")
            adapters.assert_not_called()

    def test_cli_verifies_or_returns_error(self):
        self.export()
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(main(["verify-bundle", "--bundle", str(self.zip)]), 0)
            self.assertEqual(main(["verify-bundle", "--bundle", str(self.root / "missing.zip")]), 2)

    def test_v3_comparison_requires_complete_diagnostics(self):
        self.assertEqual(comparison_exit_code(compare_runs(self.report, self.report)), 0)
        broken = copy.deepcopy(self.report)
        broken["cases"][0]["output_validation"][0]["diagnostics_complete"] = False
        self.assertEqual(comparison_exit_code(compare_runs(broken, broken)), 2)

    def test_v2_v3_cross_protocol_comparison_is_not_valid(self):
        old = copy.deepcopy(self.report)
        old["schema_version"] = "0.2"
        old["configuration"]["comparison_protocol"] = "pdfua-roundtrip-v2"
        self.assertEqual(comparison_exit_code(compare_runs(old, self.report)), 2)

    def test_duplicate_or_nonfinite_json_rejected(self):
        for data in (b'{"a":1,"a":2}', b'{"a":NaN}'):
            with self.assertRaises(ValueError):
                _read_json_bytes(data)


if __name__ == "__main__":
    unittest.main()
