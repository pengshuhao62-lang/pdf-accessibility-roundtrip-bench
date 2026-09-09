import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from pdfua_bench.cli import main
from pdfua_bench.corpus import CorpusError, load_corpus
from pdfua_bench.models import ValidationResult
from pdfua_bench.runner import run_benchmark, run_case
from pdfua_bench.toolchain import resolve_toolchain
from test_run_diff import report

ROOT = Path(__file__).resolve().parents[1]


class RunnerV2Tests(unittest.TestCase):
    def setUp(self):
        self.corpus = load_corpus(ROOT / "corpus/manifest.json")
        self.toolchain = resolve_toolchain()

    def test_tampered_corpus_stops_before_tools(self):
        with patch("pdfua_bench.runner.verify_corpus_files", return_value=["hash mismatch"]), patch("pdfua_bench.adapters.factory.build_adapters") as adapters:
            with self.assertRaises(CorpusError):
                run_benchmark(self.corpus, self.toolchain, ["ua1"], ["qpdf"], ["resave"], Path("lab"))
            adapters.assert_not_called()

    def test_unknown_fixture_stops_before_tools(self):
        with patch("pdfua_bench.adapters.factory.build_adapters") as adapters:
            with self.assertRaises(CorpusError):
                run_benchmark(self.corpus, self.toolchain, ["ua1"], ["qpdf"], ["resave"], Path("lab"), ["unknown"])
            adapters.assert_not_called()

    def test_invalid_merge_partner_never_transformed(self):
        fixture = self.corpus.fixtures[0]
        adapter = Mock()
        adapter.name = "qpdf"
        validator = Mock()
        validator.validate.side_effect = [ValidationResult(fixture.profile, True, (), "fake", True),
                                          ValidationResult(fixture.profile, False, ("rule",), "fake", True)]
        with tempfile.TemporaryDirectory() as directory:
            result = run_case(self.corpus, fixture, adapter, validator, "merge", Path(directory), {})
        self.assertEqual(result.classification, "baseline_invalid")
        adapter.merge.assert_not_called()

    def test_relative_output_resolved_before_external_tools(self):
        fixture = self.corpus.fixtures[0]
        with tempfile.TemporaryDirectory(dir=Path.cwd()) as directory:
            relative = Path(directory).relative_to(Path.cwd())
            adapter = Mock()
            adapter.version.return_value = "test"
            validator = Mock()
            validator.version.return_value = "test"
            def capture(*args):
                self.assertTrue(args[5].is_absolute())
                raise RuntimeError("path checked")
            with patch("pdfua_bench.adapters.factory.build_adapters", return_value={"qpdf": adapter}), patch("pdfua_bench.runner.VeraPDFValidator", return_value=validator), patch("pdfua_bench.runner.run_case", side_effect=capture):
                with self.assertRaisesRegex(RuntimeError, "path checked"):
                    run_benchmark(self.corpus, self.toolchain, [fixture.profile], ["qpdf"], ["resave"], relative, [fixture.fixture_id])

    def test_java_home_honored_without_isolated_root(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            java = root / "jdk/bin/java"
            java.parent.mkdir(parents=True)
            java.touch()
            with patch.dict("os.environ", {"JAVA_HOME": str(java.parent.parent), "PDFUA_BENCH_TOOL_ROOT": str(root / "missing")}):
                chain = resolve_toolchain()
                self.assertEqual(chain.java_home, java.parent.parent)
                self.assertTrue(chain.root.is_dir())

    def test_cli_comparison_exit_codes_and_preserves_files(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory) / "before.json"
            after = Path(directory) / "after.json"
            output = Path(directory) / "diff.json"
            base.write_text(json.dumps(report()))
            after.write_text(json.dumps(report(["7.1-1"])))
            args = ["compare-runs", "--before", str(base), "--after", str(after), "--format", "json", "--output", str(output)]
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(main(args), 1)
                self.assertEqual(main(args), 2)
            self.assertEqual(json.loads(output.read_text())["summary"]["new"], 1)
