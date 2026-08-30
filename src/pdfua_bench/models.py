"""Stable data structures for corpus, validation, and benchmark reports."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple


PROFILES = ("ua1", "ua2")
TOOLS = ("qpdf", "pymupdf", "ghostscript")
OPERATIONS = ("merge", "split", "resave")
CLASSIFICATIONS = (
    "baseline_invalid",
    "tool_unavailable",
    "transformation_failed",
    "output_unreadable",
    "new_pdfua_violation",
    "structure_signal_changed",
    "passed",
    "manual_review",
)


@dataclass(frozen=True)
class FixtureSpec:
    fixture_id: str
    profile: str
    path: str
    source: str
    license: str
    sha256: str
    expected_pages: int
    merge_partner: str

    def validate(self) -> None:
        if self.profile not in PROFILES:
            raise ValueError("Unsupported PDF/UA profile")
        if not self.fixture_id or not self.path:
            raise ValueError("Fixture ID and path are required")
        if self.expected_pages < 1:
            raise ValueError("Fixture page count must be positive")
        if not self.source or not self.license:
            raise ValueError("Fixture source and license are required")
        if len(self.sha256) != 64:
            raise ValueError("Fixture SHA-256 must contain 64 hexadecimal characters")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.fixture_id,
            "profile": self.profile,
            "path": self.path,
            "source": self.source,
            "license": self.license,
            "sha256": self.sha256,
            "expected_pages": self.expected_pages,
            "merge_partner": self.merge_partner,
        }


@dataclass(frozen=True)
class ValidationResult:
    profile: str
    compliant: bool
    failed_rules: Tuple[str, ...]
    validator_version: str
    readable: bool
    raw_report_path: Optional[str] = None
    error: Optional[str] = None

    def to_dict(self, include_raw_path: bool = True) -> Dict[str, Any]:
        result: Dict[str, Any] = {
            "profile": self.profile,
            "compliant": self.compliant,
            "failed_rules": list(self.failed_rules),
            "validator_version": self.validator_version,
            "readable": self.readable,
        }
        if include_raw_path and self.raw_report_path:
            result["raw_report_path"] = self.raw_report_path
        if self.error:
            result["error"] = self.error
        return result


@dataclass(frozen=True)
class StructuralSnapshot:
    page_count: int
    struct_tree_present: bool
    marked_pdf: bool
    alt_text_count: int
    role_map_count: int
    document_language_present: bool
    title_present: bool
    outline_count: int
    readable: bool = True
    error: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {
            "page_count": self.page_count,
            "struct_tree_present": self.struct_tree_present,
            "marked_pdf": self.marked_pdf,
            "alt_text_count": self.alt_text_count,
            "role_map_count": self.role_map_count,
            "document_language_present": self.document_language_present,
            "title_present": self.title_present,
            "outline_count": self.outline_count,
            "readable": self.readable,
        }
        if self.error:
            result["error"] = self.error
        return result


@dataclass(frozen=True)
class TransformationResult:
    completed: bool
    duration_ms: int
    output_files: Tuple[str, ...] = ()
    exit_code: Optional[int] = None
    error: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {
            "completed": self.completed,
            "duration_ms": self.duration_ms,
            "output_files": list(self.output_files),
        }
        if self.exit_code is not None:
            result["exit_code"] = self.exit_code
        if self.error:
            result["error"] = self.error
        return result


@dataclass(frozen=True)
class CaseResult:
    case_id: str
    fixture_id: str
    profile: str
    tool: str
    operation: str
    baseline: ValidationResult
    transformation: TransformationResult
    output_validation: Tuple[ValidationResult, ...]
    before_structure: StructuralSnapshot
    after_structure: Tuple[StructuralSnapshot, ...]
    classification: str
    details: str = ""
    manual_review: bool = False

    def __post_init__(self) -> None:
        if self.profile not in PROFILES:
            raise ValueError("Unsupported case profile")
        if self.tool not in TOOLS:
            raise ValueError("Unsupported case tool")
        if self.operation not in OPERATIONS:
            raise ValueError("Unsupported case operation")
        if self.classification not in CLASSIFICATIONS:
            raise ValueError("Unsupported case classification")

    def to_dict(self, include_raw_paths: bool = True) -> Dict[str, Any]:
        return {
            "case_id": self.case_id,
            "fixture_id": self.fixture_id,
            "profile": self.profile,
            "tool": self.tool,
            "operation": self.operation,
            "baseline": self.baseline.to_dict(include_raw_path=include_raw_paths),
            "transformation": self.transformation.to_dict(),
            "output_validation": [
                item.to_dict(include_raw_path=include_raw_paths)
                for item in self.output_validation
            ],
            "before_structure": self.before_structure.to_dict(),
            "after_structure": [item.to_dict() for item in self.after_structure],
            "classification": self.classification,
            "details": self.details,
            "manual_review": self.manual_review,
        }


@dataclass(frozen=True)
class RunReport:
    run_id: str
    started_at: str
    ended_at: str
    environment: Dict[str, str]
    configuration: Dict[str, Any]
    cases: Tuple[CaseResult, ...] = field(default_factory=tuple)

    def summary(self) -> Dict[str, int]:
        counts: Dict[str, int] = {classification: 0 for classification in CLASSIFICATIONS}
        for case in self.cases:
            counts[case.classification] += 1
        counts["total"] = len(self.cases)
        return counts

    def to_dict(self, include_raw_paths: bool = True) -> Dict[str, Any]:
        return {
            "schema_version": "0.1",
            "run_id": self.run_id,
            "started_at": self.started_at,
            "ended_at": self.ended_at,
            "environment": dict(sorted(self.environment.items())),
            "configuration": self.configuration,
            "summary": self.summary(),
            "cases": [
                case.to_dict(include_raw_paths=include_raw_paths) for case in self.cases
            ],
        }
