"""Reproducible Mac acceptance against an installed pdfua-bench package."""
import argparse
import json
import platform
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    if platform.system() != "Darwin":
        parser.error("This acceptance script targets macOS.")
    root = args.output_dir.resolve()
    root.mkdir(parents=True, exist_ok=False)
    prefix = [sys.executable, "-m", "pdfua_bench"]
    steps = [
        ["preflight", "--json"],
        ["verify-corpus", "--output-dir", str(root / "baselines")],
        ["run", "--output", str(root / "run.json")],
        ["summarize", "--input", str(root / "run.json"), "--output", str(root / "run.md")],
        ["compare-runs", "--before", str(root / "run.json"), "--after", str(root / "run.json"), "--format", "json", "--output", str(root / "self-comparison.json")],
    ]
    for step in steps:
        subprocess.run(prefix + step, check=True)
    result = json.loads((root / "self-comparison.json").read_text())
    if result["summary"]["comparable"] != 180:
        raise SystemExit("Expected 180 comparable cases.")
    print("macOS acceptance passed: 180 measured and self-comparable cases.")


if __name__ == "__main__":
    main()
