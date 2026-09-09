"""Comparison evidence is synthetic; integration reports come from real tools."""
import copy
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pdfua_bench.cli import _write_output, main
from pdfua_bench.models import StructuralSnapshot, ValidationResult
from pdfua_bench.compare import classify_outcome
from pdfua_bench.run_diff import compare_runs, comparison_exit_code, comparison_markdown
from pdfua_bench.structure import _count_alt_values


def report(rules=()):
    structure = dict(page_count=1, struct_tree_present=True, marked_pdf=True,
                     alt_text_count=0, role_map_count=0, document_language_present=True,
                     title_present=True, outline_count=0, readable=True, error=None)
    baseline = dict(profile="ua1", compliant=True, readable=True,
                    validator_version="1.30.2", failed_rules=[], error=None)
    output = dict(baseline, compliant=not rules, failed_rules=list(rules))
    case = dict(case_id="sample-qpdf-resave", fixture_id="sample", profile="ua1",
                tool="qpdf", operation="resave", baseline=baseline,
                transformation=dict(completed=True, output_files=["output.pdf"], error=None),
                output_validation=[output], before_structure=structure,
                after_structure=[copy.deepcopy(structure)],
                classification="new_pdfua_violation" if rules else "passed",
                provenance=dict(inputs=[dict(id="sample", sha256="a"*64, pages=1)],
                                parameters=dict(operation="resave", adapter_defaults="v1")))
    return dict(schema_version="0.2", cases=[case],
                environment=dict(os="Darwin", os_version="15.6", architecture="arm64", python="3.9.6", java="17.0.18"),
                configuration=dict(expected_case_count=1, comparison_protocol="pdfua-roundtrip-v2",
                                   analyzer_sha256="b"*64, tool_versions=dict(qpdf="12.3.2"),
                                   verapdf_version="1.30.2", python_packages=dict(pypdf="6.16.2", reportlab="5.0.1")))


class RunComparisonTests(unittest.TestCase):
    def test_identical_valid_run(self):
        result = compare_runs(report(), report())
        self.assertEqual(result["summary"]["comparable"], 1)
        self.assertEqual(comparison_exit_code(result), 0)

    def test_new_persistent_and_removed_rules(self):
        result = compare_runs(report(["7.1-1", "8.2-1"]), report(["8.2-1", "9.1-2"]))
        row = result["cases"][0]
        self.assertEqual(row["new"], ["output-1:pdfua:9.1-2"])
        self.assertEqual(row["persistent"], ["output-1:pdfua:8.2-1"])
        self.assertEqual(row["no_longer_observed"], ["output-1:pdfua:7.1-1"])
        self.assertEqual(comparison_exit_code(result), 1)

    def test_target_version_change_allowed_and_rendered(self):
        after = report()
        after["configuration"]["tool_versions"]["qpdf"] = "12.4.0"
        result = compare_runs(report(), after)
        self.assertEqual(comparison_exit_code(result), 0)
        self.assertIn("12.4.0", comparison_markdown(result))

    def test_every_environment_dimension_is_guarded(self):
        for key in report()["environment"]:
            with self.subTest(key=key):
                after = report()
                after["environment"][key] = "different"
                self.assertEqual(comparison_exit_code(compare_runs(report(), after)), 2)

    def test_analyzer_validator_and_package_changes_guarded(self):
        for key, value in [("analyzer_sha256", "c"*64), ("verapdf_version", "1.31"),
                           ("python_packages", dict(pypdf="other", reportlab="5.0.1"))]:
            with self.subTest(key=key):
                after = report()
                after["configuration"][key] = value
                self.assertEqual(comparison_exit_code(compare_runs(report(), after)), 2)

    def test_fixture_hash_change_is_not_a_tool_regression(self):
        after = report()
        after["cases"][0]["provenance"]["inputs"][0]["sha256"] = "c"*64
        self.assertEqual(comparison_exit_code(compare_runs(report(), after)), 2)

    def test_legacy_and_malformed_context_fail_closed(self):
        for key, value in [("schema_version", "0.1"), ("configuration", None), ("environment", [])]:
            with self.subTest(key=key):
                after = report()
                after[key] = value
                self.assertEqual(comparison_exit_code(compare_runs(report(), after)), 2)

    def test_truncated_matrix_rejected_even_if_both_reports_match(self):
        after = report()
        after["configuration"]["expected_case_count"] = 2
        self.assertEqual(comparison_exit_code(compare_runs(after, after)), 2)

    def test_missing_case_is_not_reported_as_fixed(self):
        after = report()
        after["cases"][0]["fixture_id"] = "another"
        result = compare_runs(report(), after)
        self.assertEqual(result["summary"]["not_comparable"], 2)
        self.assertEqual(result["summary"]["no_longer_observed"], 0)

    def test_infrastructure_failures_cannot_remove_signals(self):
        for state in ("baseline_invalid", "tool_unavailable", "transformation_failed", "output_unreadable"):
            with self.subTest(state=state):
                after = report()
                after["cases"][0]["classification"] = state
                result = compare_runs(report(["7.1-1"]), after)
                self.assertEqual(comparison_exit_code(result), 2)
                self.assertEqual(result["summary"]["no_longer_observed"], 0)

    def test_missing_rule_evidence_rejected(self):
        after = report(["7.1-1"])
        after["cases"][0]["output_validation"][0]["failed_rules"] = []
        self.assertEqual(comparison_exit_code(compare_runs(report(), after)), 2)

    def test_output_count_mismatch_rejected(self):
        after = report()
        after["cases"][0]["after_structure"] = []
        self.assertEqual(comparison_exit_code(compare_runs(report(), after)), 2)

    def test_duplicate_and_unsafe_case_ids_rejected(self):
        after = report()
        after["cases"].append(copy.deepcopy(after["cases"][0]))
        with self.assertRaises(ValueError):
            compare_runs(report(), after)
        after = report()
        after["cases"][0]["fixture_id"] = "x; touch /tmp/unsafe"
        with self.assertRaises(ValueError):
            compare_runs(report(), after)

    def test_structure_change_has_exact_values(self):
        after = report()
        after["cases"][0]["after_structure"][0]["title_present"] = False
        after["cases"][0]["classification"] = "structure_signal_changed"
        result = compare_runs(report(), after)
        self.assertEqual(result["cases"][0]["new"], ["structure:title_present:True->False"])

    def test_classification_must_agree_with_evidence(self):
        after = report(["7.1-1"])
        after["cases"][0]["classification"] = "passed"
        self.assertEqual(comparison_exit_code(compare_runs(report(), after)), 2)

    def test_markdown_escapes_report_content(self):
        result = compare_runs(report(), report(["<script>`x`</script>"]))
        rendered = comparison_markdown(result)
        self.assertNotIn("<script>", rendered)
        self.assertIn("--fixtures sample", rendered)

    def test_output_never_overwrites(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            _write_output("original", path)
            with self.assertRaises(FileExistsError):
                _write_output("replacement", path)
            self.assertEqual(path.read_text(), "original")

    def test_unreadable_structure_not_passed(self):
        baseline = ValidationResult("ua1", True, (), "1.30.2", True)
        before = StructuralSnapshot(1, True, True, 0, 0, True, True, 0)
        unreadable = StructuralSnapshot(0, False, False, 0, 0, False, False, 0, readable=False)
        self.assertEqual(classify_outcome(baseline, [baseline], before, [unreadable], True, True), "output_unreadable")

    def test_exhausted_structure_budget_is_not_zero(self):
        with self.assertRaises(ValueError):
            _count_alt_values({}, set(), [0])
