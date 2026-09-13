"""Verify a complete real v3 run and replay representative merge/split/resave bundles."""
import argparse
import json
import subprocess
import sys
from dataclasses import replace
from pathlib import Path

from pdfua_bench.cli import default_corpus, _write_output
from pdfua_bench.corpus import load_corpus
from pdfua_bench.bundles import export_case, verify_bundle
from pdfua_bench.reports import load_json
from pdfua_bench.run_diff import compare_runs, comparison_exit_code
from pdfua_bench.validators import VeraPDFValidator
from pdfua_bench.toolchain import resolve_toolchain


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--official-verapdf", type=Path, required=True, help="unmodified launcher for rule/count invariance check")
    args = parser.parse_args()
    report = load_json(args.input)
    comparison = compare_runs(report, report)
    assert len(report["cases"]) == 180 and comparison["summary"]["comparable"] == 180
    assert comparison_exit_code(comparison) == 0
    checks = [d for c in report["cases"] for v in c["output_validation"] for d in v["failed_checks"]]
    located = [d for d in checks if d["location_status"] == "verified-page-object"]
    assert located, "Real matrix must exercise verified PDF page-object locations."
    args.output_dir.mkdir(parents=True, exist_ok=False)
    case, index, measured = max(((c, i, v) for c in report["cases"] for i, v in enumerate(c["output_validation"])), key=lambda item: len(item[2]["failed_checks"]))
    assert len(measured["failed_checks"]) > 10000, "Exercise the upstream diagnostic cap."
    path = args.input.parent / report["run_id"] / "cases" / case["case_id"] / case["transformation"]["output_files"][index]
    original_report = args.output_dir / "official-validator.json"
    original = VeraPDFValidator(replace(resolve_toolchain(), vera_pdf=args.official_verapdf.resolve())).validate(
        path.resolve(), case["profile"], original_report, args.output_dir / "official-validator.log")
    raw = load_json(original_report)["report"]["jobs"][0]["validationResult"][0]
    assert original.compliant == measured["compliant"] and list(original.failed_rules) == measured["failed_rules"]
    assert raw["details"]["failedChecks"] == len(measured["failed_checks"])
    invariance = dict(case=case["case_id"], compliant_unchanged=True, failed_rules_unchanged=True,
                      failed_check_count=raw["details"]["failedChecks"],
                      official_recorded_checks=len(original.failed_checks), overlay_recorded_checks=len(measured["failed_checks"]))
    corpus = load_corpus(default_corpus())
    selected = []
    # Small self-authored fixtures keep the replay fast; every operation is checked.
    for operation in ("merge", "split", "resave"):
        candidates = [c for c in report["cases"] if c["tool"] == "qpdf" and c["operation"] == operation and "-ref-" not in c["fixture_id"]]
        case = min(candidates, key=lambda c: c["before_structure"]["page_count"])
        bundle = args.output_dir / (operation + ".zip")
        export_case(report, case["case_id"], corpus, args.input.parent / report["run_id"], bundle, True)
        verify_bundle(bundle)
        output = args.output_dir / (operation + ".json")
        subprocess.run([sys.executable, "-m", "pdfua_bench", "reproduce", "--bundle", str(bundle), "--output", str(output)], check=True)
        selected.append(case["case_id"])
    payload = dict(cases=180, diagnostic_checks=len(checks), verified_page_checks=len(located),
                   unresolved_checks=len(checks)-len(located), replayed_cases=selected,
                   self_comparison=comparison["summary"], official_overlay_invariance=invariance)
    _write_output(json.dumps(payload, indent=2) + "\n", args.output_dir / "acceptance.json")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
