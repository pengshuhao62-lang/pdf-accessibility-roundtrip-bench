"""Benchmark orchestration over disposable copies of the corpus."""

from __future__ import annotations

import hashlib
import json
import platform
import shutil
import sys
import tempfile
import time
import uuid
from dataclasses import replace
from importlib.metadata import version as package_version
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from .adapters.base import AdapterError, ToolAdapter
from .compare import classify_outcome
from .corpus import Corpus, CorpusError, sha256_file, verify_corpus_files
from .models import (
    CaseResult,
    FixtureSpec,
    OPERATIONS,
    PROFILES,
    RunReport,
    StructuralSnapshot,
    TransformationResult,
    ValidationResult,
)
from .structure import inspect_structure
from .process import run_command
from .toolchain import Toolchain
from .validators import ValidationError, VeraPDFValidator


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _safe_case_id(fixture: FixtureSpec, tool: str, operation: str) -> str:
    return f"{fixture.fixture_id}-{tool}-{operation}"


def environment_snapshot(toolchain: Toolchain) -> Dict[str, str]:
    java = "unavailable"
    if toolchain.java_home:
        try:
            result = run_command([str(toolchain.java_home / "bin/java"), "-version"], toolchain.root, toolchain.environment, 15)
            if result.returncode == 0 and not result.timed_out:
                java = " | ".join((result.stderr or result.stdout).strip().splitlines())
        except OSError:
            pass
    return {
        "java": java,
        "os": platform.system(),
        "os_version": platform.mac_ver()[0] or platform.release(),
        "architecture": platform.machine(),
        "python": platform.python_version(),
        "tool_root": "isolated-external-ssd-toolchain",
        "verapdf": "available" if toolchain.vera_pdf else "missing",
        "qpdf": "available" if toolchain.qpdf else "missing",
        "ghostscript": "available" if toolchain.ghostscript else "missing",
    }


def _relative_output_names(paths: Iterable[Path], workdir: Path) -> Tuple[str, ...]:
    result: List[str] = []
    root = workdir.resolve()
    for path in paths:
        try:
            result.append(path.resolve().relative_to(root).as_posix())
        except ValueError:
            result.append("<outside-workdir>")
    return tuple(result)


def _copy_fixture(corpus: Corpus, fixture: FixtureSpec, destination: Path) -> Path:
    source = corpus.file_path(fixture)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    if sha256_file(destination) != fixture.sha256:
        raise CorpusError("A copied fixture no longer matches its declared hash.")
    return destination


def _aggregate_structures(structures: Iterable[StructuralSnapshot]) -> StructuralSnapshot:
    items = list(structures)
    if not items:
        return StructuralSnapshot(0, False, False, 0, 0, False, False, 0, readable=False)
    if any(not item.readable for item in items):
        return StructuralSnapshot(
            page_count=sum(item.page_count for item in items),
            struct_tree_present=False,
            marked_pdf=False,
            alt_text_count=sum(item.alt_text_count for item in items),
            role_map_count=sum(item.role_map_count for item in items),
            document_language_present=False,
            title_present=False,
            outline_count=sum(item.outline_count for item in items),
            readable=False,
            error="One or more PDF structures could not be inspected.",
        )
    return StructuralSnapshot(
        page_count=sum(item.page_count for item in items),
        struct_tree_present=all(item.struct_tree_present for item in items),
        marked_pdf=all(item.marked_pdf for item in items),
        alt_text_count=sum(item.alt_text_count for item in items),
        role_map_count=sum(item.role_map_count for item in items),
        document_language_present=all(item.document_language_present for item in items),
        title_present=all(item.title_present for item in items),
        outline_count=sum(item.outline_count for item in items),
    )


def _validate_one(
    validator: VeraPDFValidator,
    pdf_path: Path,
    profile: str,
    reports_dir: Path,
    label: str,
) -> ValidationResult:
    report_path = reports_dir / f"{label}.json"
    log_path = reports_dir / f"{label}.log"
    return validator.validate(pdf_path, profile, report_path, log_path)


def _baseline_result(
    validator: VeraPDFValidator,
    corpus: Corpus,
    fixture: FixtureSpec,
    reports_dir: Path,
    cache: Dict[str, ValidationResult],
) -> ValidationResult:
    cached = cache.get(fixture.fixture_id)
    if cached:
        return cached
    result = _validate_one(
        validator,
        corpus.file_path(fixture),
        fixture.profile,
        reports_dir,
        f"baseline-{fixture.fixture_id}",
    )
    cache[fixture.fixture_id] = result
    return result


def run_case(
    corpus: Corpus,
    fixture: FixtureSpec,
    adapter: ToolAdapter,
    validator: VeraPDFValidator,
    operation: str,
    case_dir: Path,
    baseline_cache: Dict[str, ValidationResult],
) -> CaseResult:
    case_id = _safe_case_id(fixture, adapter.name, operation)
    case_dir.mkdir(parents=True, exist_ok=True)
    reports_dir = case_dir / "validator-reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    input_dir = case_dir / "inputs"
    output_dir = case_dir / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    fixture_copy = _copy_fixture(corpus, fixture, input_dir / f"{fixture.fixture_id}.pdf")
    before_structures = [inspect_structure(fixture_copy)]
    before_structure = _aggregate_structures(before_structures)

    try:
        baseline = _baseline_result(
            validator, corpus, fixture, reports_dir, baseline_cache
        )
    except ValidationError as exc:
        baseline = ValidationResult(
            profile=fixture.profile,
            compliant=False,
            failed_rules=(),
            validator_version="unavailable",
            readable=False,
            error="The validator did not return a usable baseline result.",
        )
        return CaseResult(
            case_id=case_id,
            fixture_id=fixture.fixture_id,
            profile=fixture.profile,
            tool=adapter.name,
            operation=operation,
            baseline=baseline,
            transformation=TransformationResult(False, 0, error="validator stage failed"),
            output_validation=(),
            before_structure=before_structure,
            after_structure=(),
            classification="tool_unavailable",
            details="The baseline validator could not be used.",
        )

    if not baseline.compliant or not baseline.readable:
        return CaseResult(
            case_id=case_id,
            fixture_id=fixture.fixture_id,
            profile=fixture.profile,
            tool=adapter.name,
            operation=operation,
            baseline=baseline,
            transformation=TransformationResult(False, 0, error="baseline invalid"),
            output_validation=(),
            before_structure=before_structure,
            after_structure=(),
            classification="baseline_invalid",
            details="The fixture did not pass its declared PDF/UA profile before transformation.",
        )

    partner_copy: Optional[Path] = None
    if operation == "merge":
        partner = corpus.by_id().get(fixture.merge_partner)
        if partner is None:
            return CaseResult(
                case_id=case_id,
                fixture_id=fixture.fixture_id,
                profile=fixture.profile,
                tool=adapter.name,
                operation=operation,
                baseline=baseline,
                transformation=TransformationResult(False, 0, error="merge partner missing"),
                output_validation=(),
                before_structure=before_structure,
                after_structure=(),
                classification="transformation_failed",
                details="The corpus merge partner was missing.",
            )
        try:
            partner_baseline = _baseline_result(validator, corpus, partner, reports_dir, baseline_cache)
        except ValidationError:
            partner_baseline = ValidationResult(partner.profile, False, (), "unavailable", False)
        if not partner_baseline.readable or not partner_baseline.compliant:
            return CaseResult(
                case_id, fixture.fixture_id, fixture.profile, adapter.name, operation,
                baseline, TransformationResult(False, 0, error="merge partner baseline failed"),
                (), before_structure, (),
                "baseline_invalid" if partner_baseline.readable else "tool_unavailable",
                details="The merge partner must have a valid baseline before transformation.",
            )
        partner_copy = _copy_fixture(
            corpus, partner, input_dir / f"{partner.fixture_id}.pdf"
        )
        before_structures.append(inspect_structure(partner_copy))
        before_structure = _aggregate_structures(before_structures)

    try:
        started = time.monotonic()
        if operation == "merge":
            output = output_dir / "merged.pdf"
            outputs = adapter.merge([fixture_copy, partner_copy], output, case_dir)  # type: ignore[list-item]
        elif operation == "split":
            outputs = adapter.split(fixture_copy, output_dir / "split", case_dir)
        elif operation == "resave":
            output = output_dir / "resaved.pdf"
            outputs = adapter.resave(fixture_copy, output, case_dir)
        else:
            raise AdapterError("unsupported transformation operation")
        duration_ms = int((time.monotonic() - started) * 1000)
        output_names = _relative_output_names(outputs, case_dir)
        transformation = TransformationResult(
            completed=True,
            duration_ms=duration_ms,
            output_files=output_names,
        )
    except AdapterError as exc:
        duration_ms = int((time.monotonic() - started) * 1000)
        transformation = TransformationResult(
            completed=False,
            duration_ms=duration_ms,
            error=str(exc),
        )
        return CaseResult(
            case_id=case_id,
            fixture_id=fixture.fixture_id,
            profile=fixture.profile,
            tool=adapter.name,
            operation=operation,
            baseline=baseline,
            transformation=transformation,
            output_validation=(),
            before_structure=before_structure,
            after_structure=(),
            classification="transformation_failed",
            details="The transformation tool did not complete successfully.",
        )

    output_validation: List[ValidationResult] = []
    after_structures: List[StructuralSnapshot] = []
    try:
        if len(outputs) == 1:
            output_validation = [
                _validate_one(
                    validator,
                    outputs[0],
                    fixture.profile,
                    reports_dir,
                    "output-1",
                )
            ]
        else:
            output_validation = validator.validate_many(
                outputs,
                fixture.profile,
                reports_dir / "output-batch.json",
                reports_dir / "output-batch.log",
            )
    except ValidationError:
        output_validation = [
            ValidationResult(
                profile=fixture.profile,
                compliant=False,
                failed_rules=(),
                validator_version=baseline.validator_version,
                readable=False,
                error="The output validator result was unavailable.",
            )
            for _ in outputs
        ]
    for output_path in outputs:
        after_structures.append(inspect_structure(output_path))

    classification = classify_outcome(
        baseline=baseline,
        outputs=output_validation,
        before_structure=before_structure,
        after_structures=after_structures,
        transformation_completed=True,
        output_readable=all(item.readable for item in after_structures),
    )
    return CaseResult(
        case_id=case_id,
        fixture_id=fixture.fixture_id,
        profile=fixture.profile,
        tool=adapter.name,
        operation=operation,
        baseline=baseline,
        transformation=transformation,
        output_validation=tuple(output_validation),
        before_structure=before_structure,
        after_structure=tuple(after_structures),
        classification=classification,
        details="",
    )


def run_benchmark(
    corpus: Corpus,
    toolchain: Toolchain,
    profiles: Sequence[str],
    tools: Sequence[str],
    operations: Sequence[str],
    output_dir: Path,
    fixture_ids: Optional[Sequence[str]] = None,
) -> RunReport:
    invalid = set(profiles) - set(PROFILES)
    invalid |= set(tools) - {"qpdf", "pymupdf", "ghostscript"}
    invalid |= set(operations) - set(("merge", "split", "resave"))
    if invalid:
        raise CorpusError("The benchmark selection contains an unsupported value.")
    if not profiles or not tools or not operations or any(len(set(items)) != len(items) for items in (profiles, tools, operations)):
        raise CorpusError("Benchmark selections must be nonempty and unique.")
    integrity_errors = verify_corpus_files(corpus)
    if integrity_errors:
        raise CorpusError("Corpus integrity checks failed: " + "; ".join(integrity_errors))
    if fixture_ids and (set(fixture_ids) - set(corpus.by_id()) or len(set(fixture_ids)) != len(fixture_ids)):
        raise CorpusError("Unknown or duplicate fixture selection.")

    from .adapters.factory import build_adapters

    selected_fixtures = [fixture for fixture in corpus.fixtures if fixture.profile in profiles and (not fixture_ids or fixture.fixture_id in fixture_ids)]
    if fixture_ids and len(selected_fixtures) != len(fixture_ids):
        raise CorpusError("Selected fixture profiles do not match the profile selection.")
    if not selected_fixtures:
        raise CorpusError("The selected profiles contain no corpus fixtures.")
    adapters = build_adapters(toolchain)
    tool_versions: Dict[str, str] = {}
    for tool_name in tools:
        try:
            tool_versions[tool_name] = adapters[tool_name].version()
        except AdapterError:
            tool_versions[tool_name] = "unavailable"
    validator = VeraPDFValidator(toolchain)
    try:
        validator_version = validator.version()
    except ValidationError:
        validator_version = "unavailable"
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
    run_dir = output_dir.resolve() / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    baseline_cache: Dict[str, ValidationResult] = {}
    cases: List[CaseResult] = []
    started_at = utc_now()
    total_cases = len(selected_fixtures) * len(tools) * len(operations)
    for fixture in selected_fixtures:
        for tool_name in tools:
            adapter = adapters[tool_name]
            for operation in operations:
                case_dir = run_dir / "cases" / _safe_case_id(fixture, tool_name, operation)
                case_number = len(cases) + 1
                print(
                    f"[{case_number}/{total_cases}] {fixture.fixture_id} {tool_name} {operation}",
                    file=sys.stderr,
                    flush=True,
                )
                case_result = run_case(
                    corpus,
                    fixture,
                    adapter,
                    validator,
                    operation,
                    case_dir,
                    baseline_cache,
                )
                inputs = [{"id": fixture.fixture_id, "sha256": fixture.sha256, "pages": fixture.expected_pages}]
                if operation == "merge":
                    partner = corpus.by_id()[fixture.merge_partner]
                    inputs.append({"id": partner.fixture_id, "sha256": partner.sha256, "pages": partner.expected_pages})
                case_result = replace(case_result, provenance={
                    "inputs": inputs,
                    "parameters": {"operation": operation, "adapter_defaults": "v1"},
                })
                cases.append(case_result)
                print(
                    f"[{case_number}/{total_cases}] result={case_result.classification}",
                    file=sys.stderr,
                    flush=True,
                )
    report = RunReport(
        run_id=run_id,
        started_at=started_at,
        ended_at=utc_now(),
        environment=environment_snapshot(toolchain),
        configuration={
            "profiles": list(profiles),
            "tools": list(tools),
            "operations": list(operations),
            "fixture_count": len(selected_fixtures),
            "expected_case_count": len(selected_fixtures) * len(tools) * len(operations),
            "tool_versions": tool_versions,
            "verapdf_version": validator_version,
            "comparison_protocol": "pdfua-roundtrip-v2",
            "analyzer_sha256": analyzer_fingerprint(),
            "python_packages": {name: package_version(name) for name in ("pypdf", "reportlab")},
        },
        cases=tuple(cases),
    )
    return report


def analyzer_fingerprint() -> str:
    root = Path(__file__).parent
    digest = hashlib.sha256()
    for name in ("runner.py", "compare.py", "structure.py", "validators.py", "adapters/qpdf_adapter.py", "adapters/pymupdf_adapter.py", "adapters/ghostscript_adapter.py"):
        digest.update(name.encode())
        digest.update((root / name).read_bytes().replace(b"\r\n", b"\n"))
    return digest.hexdigest()
