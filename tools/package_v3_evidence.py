"""Package complete diagnostics losslessly; keep repository summary files small."""
import argparse
import gzip
import hashlib
import json
import shutil
from pathlib import Path

from pdfua_bench.cli import _write_output
from pdfua_bench.reports import load_json, markdown_from_dict
from pdfua_bench.run_diff import compare_runs, comparison_exit_code
from pdfua_bench.bundles import verify_bundle


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--acceptance-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    report = load_json(args.input)
    comparison = compare_runs(report, report)
    assert comparison_exit_code(comparison) == 0 and comparison["summary"]["comparable"] == 180
    acceptance = load_json(args.acceptance_dir / "acceptance.json")
    args.output_dir.mkdir(parents=True, exist_ok=False)
    name = "pdfua-bench-v0.3.0-full-run.json.gz"
    with args.input.open("rb") as source, (args.output_dir / name).open("xb") as target:
        with gzip.GzipFile(filename="", mode="wb", fileobj=target, mtime=0) as compressed:
            shutil.copyfileobj(source, compressed)
    _write_output(markdown_from_dict(report), args.output_dir / "pdfua-bench-v0.3.0-full-run.md")
    _write_output(json.dumps(comparison, indent=2) + "\n", args.output_dir / "pdfua-bench-v0.3.0-self-comparison.json")
    summary = {key: report[key] for key in ("run_id", "started_at", "ended_at", "environment", "configuration", "summary")}
    summary.update(schema_version="0.3-evidence-summary", acceptance=acceptance,
                   complete_diagnostics_asset=name,
                   note="Derived summary, not a comparable run. Full failed-check evidence is in the lossless gzip asset.")
    _write_output(json.dumps(summary, indent=2) + "\n", args.output_dir / "pdfua-bench-v0.3.0-evidence-summary.json")
    bundle = args.acceptance_dir / "merge.zip"
    _, evidence, _ = verify_bundle(bundle)
    assert all("-ref-" not in i["id"] for i in evidence["cases"][0]["provenance"]["inputs"]), "Publish the self-authored sample only."
    with bundle.open("rb") as source, (args.output_dir / "pdfua-bench-v0.3.0-example-case.zip").open("xb") as target:
        shutil.copyfileobj(source, target)
    checksums = []
    for path in sorted(args.output_dir.iterdir()):
        digest = hashlib.sha256()
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024*1024), b""):
                digest.update(chunk)
        checksums.append(f"{digest.hexdigest()}  {path.name}")
    _write_output("\n".join(checksums) + "\n", args.output_dir / "EVIDENCE-SHA256SUMS.txt")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
