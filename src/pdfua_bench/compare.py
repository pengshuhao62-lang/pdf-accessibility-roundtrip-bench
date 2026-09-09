"""Compare validation and structure outcomes for one roundtrip case."""

from __future__ import annotations

from typing import Iterable, List

from .models import ValidationResult
from .structure import compare_structure


def classify_outcome(
    baseline: ValidationResult,
    outputs: Iterable[ValidationResult],
    before_structure,
    after_structures,
    transformation_completed: bool,
    output_readable: bool,
) -> str:
    if not baseline.readable or not baseline.compliant or not before_structure.readable:
        return "baseline_invalid"
    if not transformation_completed:
        return "transformation_failed"
    output_items = list(outputs)
    if any(item.error for item in output_items):
        return "transformation_failed"
    after_structures = list(after_structures)
    if not output_readable or not output_items or len(output_items) != len(after_structures) or any(not item.readable for item in output_items) or any(not item.readable for item in after_structures):
        return "output_unreadable"
    if any(not item.compliant for item in output_items):
        return "new_pdfua_violation"
    if compare_structure(before_structure, after_structures):
        return "structure_signal_changed"
    return "passed"
