"""Command-line interface for the PDF Accessibility Roundtrip Bench."""

from __future__ import annotations

import argparse
import json
import platform
import sys
import tempfile
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple

from reportlab.pdfgen import canvas

from . import __version__
from .adapters.factory import build_adapters
from .corpus import Corpus, CorpusError, load_corpus, verify_corpus_files
from .models import OPERATIONS, PROFILES, TOOLS
from .reports import json_text, load_json, markdown_from_dict, markdown_text
from .runner import run_benchmark
from .toolchain import Toolchain, resolve_toolchain
from .validators import ValidationError, VeraPDFValidator
from .structure import inspect_structure


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pdfua-bench",
        description="Benchmark machine-verifiable PDF/UA changes after PDF roundtrip operations.",
    )
    parser.add_argument("--version", action="version", version=f"pdfua-bench {__version__}")
    subparsers = parser.add_subparsers(dest="command")

    preflight = subparsers.add_parser("preflight", help="check the local toolchain")
    preflight.add_argument("--json", action="store_true", help="print machine-readable output")

    verify = subparsers.add_parser("verify-corpus", help="verify corpus integrity and baselines")
    verify.add_argument("--corpus", type=Path, default=Path("corpus/manifest.json"))
    verify.add_argument("--output-dir", type=Path, default=Path("lab/corpus-verification"))

    run = subparsers.add_parser("run", help="run the selected roundtrip matrix")
    run.add_argument("--corpus", type=Path, default=Path("corpus/manifest.json"))
    run.add_argument("--profiles", default="ua1,ua2")
    run.add_argument("--tools", default="qpdf,pymupdf,ghostscript")
    run.add_argument("--operations", default="merge,split,resave")
    run.add_argument("--output", type=Path, default=Path("lab/runs/run.json"))

    summarize = subparsers.add_parser("summarize", help="render a JSON run report as Markdown")
    summarize.add_argument("--input", type=Path, required=True)
    summarize.add_argument("--format", choices=("markdown", "json"), default="markdown")
    summarize.add_argument("--output", type=Path)

    return parser


def _split_values(value: str, allowed: Sequence[str], label: str) -> List[str]:
    values = [part.strip() for part in value.split(",") if part.strip()]
    if not values or set(values) - set(allowed):
        raise ValueError(f"Unsupported {label}; choose from {', '.join(allowed)}.")
    return values


def _write_output(content: str, path: Optional[Path]) -> None:
    if path is None:
        sys.stdout.write(content)
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _tool_version(adapter) -> str:
    try:
        return adapter.version()
    except Exception:
        return "unavailable"


def _preflight(toolchain: Toolchain) -> Tuple[bool, dict]:
    checks = {}
    problems: List[str] = []
    checks["python"] = platform.python_version()
    checks["java"] = "available" if toolchain.java_home else "missing"
    if not toolchain.java_home:
        problems.append("isolated Java runtime is missing")
    checks["verapdf"] = _tool_version(VeraPDFValidator(toolchain))
    if not toolchain.vera_pdf:
        problems.append("veraPDF is missing")
    else:
        try:
            profiles = VeraPDFValidator(toolchain).list_profiles()
            checks["verapdf_profiles"] = list(profiles)
            missing = set(PROFILES) - set(profiles)
            if missing:
                problems.append("veraPDF is missing profile(s): " + ", ".join(sorted(missing)))
        except ValidationError as exc:
            problems.append(str(exc))
    adapters = build_adapters(toolchain)
    for name in TOOLS:
        checks[name] = _tool_version(adapters[name])
        if checks[name] == "unavailable":
            problems.append(f"{name} is missing or could not report a version")

    dependency_checks = {}
    for module_name in ("pymupdf", "pypdf", "reportlab"):
        try:
            module = __import__(module_name)
            dependency_checks[module_name] = str(getattr(module, "__version__", "available"))
        except Exception:
            dependency_checks[module_name] = "missing"
            problems.append(f"Python dependency {module_name} is missing")
    checks["python_dependencies"] = dependency_checks

    try:
        with tempfile.TemporaryDirectory(prefix="pdfua-bench-preflight-") as directory:
            pdf_path = Path(directory) / "probe.pdf"
            document = canvas.Canvas(str(pdf_path))
            document.setTitle("pdfua-bench preflight probe")
            document.drawString(72, 720, "Preflight probe")
            document.save()
            structure = inspect_structure(pdf_path)
            checks["pdf_probe_readable"] = structure.readable
            if not structure.readable:
                problems.append("the Python PDF probe could not be read")
            if toolchain.vera_pdf:
                validator = VeraPDFValidator(toolchain)
                probe_reports = Path(directory) / "reports"
                for profile in PROFILES:
                    try:
                        result = validator.validate(
                            pdf_path,
                            profile,
                            probe_reports / f"{profile}.json",
                            probe_reports / f"{profile}.log",
                        )
                        checks[f"verapdf_probe_{profile}"] = {
                            "readable": result.readable,
                            "compliant": result.compliant,
                        }
                    except ValidationError as exc:
                        problems.append(f"veraPDF {profile} probe failed: {exc}")
    except Exception:
        problems.append("the PDF preflight probe could not be generated")

    return not problems, {"ok": not problems, "checks": checks, "problems": problems}


def _verify_corpus(corpus: Corpus, toolchain: Toolchain, output_dir: Path) -> List[str]:
    errors = verify_corpus_files(corpus)
    output_dir.mkdir(parents=True, exist_ok=True)
    validator = VeraPDFValidator(toolchain)
    for fixture in corpus.fixtures:
        if errors:
            pass
        try:
            result = validator.validate(
                corpus.file_path(fixture),
                fixture.profile,
                output_dir / f"{fixture.fixture_id}.json",
                output_dir / f"{fixture.fixture_id}.log",
            )
            if not result.compliant:
                errors.append(
                    f"{fixture.fixture_id}: baseline does not pass {fixture.profile}."
                )
        except (CorpusError, ValidationError) as exc:
            errors.append(f"{fixture.fixture_id}: baseline validation failed.")
    return errors


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    toolchain = resolve_toolchain()
    try:
        if args.command is None:
            parser.print_help()
            return 0
        if args.command == "preflight":
            ok, payload = _preflight(toolchain)
            if args.json:
                print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
            else:
                print("pdfua-bench preflight")
                for key, value in payload["checks"].items():
                    print(f"- {key}: {value}")
                if payload["problems"]:
                    print("Problems:")
                    for problem in payload["problems"]:
                        print(f"- {problem}")
                else:
                    print("All preflight checks passed.")
            return 0 if ok else 2

        if args.command == "verify-corpus":
            corpus = load_corpus(args.corpus)
            errors = _verify_corpus(corpus, toolchain, args.output_dir)
            if errors:
                for error in errors:
                    print(f"ERROR: {error}", file=sys.stderr)
                return 1
            print(f"Corpus verified: {len(corpus.fixtures)} fixture(s).")
            return 0

        if args.command == "run":
            profiles = _split_values(args.profiles, PROFILES, "profiles")
            tools = _split_values(args.tools, TOOLS, "tools")
            operations = _split_values(args.operations, OPERATIONS, "operations")
            corpus = load_corpus(args.corpus)
            report = run_benchmark(
                corpus,
                toolchain,
                profiles=profiles,
                tools=tools,
                operations=operations,
                output_dir=args.output.parent,
            )
            _write_output(json_text(report), args.output)
            print(
                f"Completed {report.summary().get('total', 0)} case(s); "
                f"report written to {args.output}.",
                file=sys.stderr,
            )
            return 0

        if args.command == "summarize":
            payload = load_json(args.input)
            if args.format == "json":
                content = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
            else:
                content = markdown_from_dict(payload)
            _write_output(content, args.output)
            return 0

        parser.error("unsupported command")
    except (CorpusError, ValidationError, OSError, ValueError) as exc:
        print(f"pdfua-bench error: {exc}", file=sys.stderr)
        return 2
    return 2
