"""veraPDF CLI adapter and JSON report normalization."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

from .models import PROFILES, ValidationResult
from .process import ProcessResult, run_command
from .toolchain import Toolchain
from .diagnostics import extract_diagnostics


class ValidationError(RuntimeError):
    """An external validator could not produce a usable result."""


def _walk(value: Any, seen: Optional[Set[int]] = None) -> Iterable[Any]:
    seen = seen or set()
    identity = id(value)
    if identity in seen:
        return
    seen.add(identity)
    yield value
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from _walk(child, seen)
    elif isinstance(value, list):
        for child in value:
            yield from _walk(child, seen)


def _collect_key_values(value: Any, keys: Set[str]) -> List[Any]:
    matches: List[Any] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if str(key).lower() in keys:
                matches.append(child)
            matches.extend(_collect_key_values(child, keys))
    elif isinstance(value, list):
        for child in value:
            matches.extend(_collect_key_values(child, keys))
    return matches


def _find_compliance(payload: Dict[str, Any]) -> Optional[bool]:
    values = _collect_key_values(
        payload,
        {"compliant", "iscompliant", "iscompliantvalue", "validationresult"},
    )
    booleans = [item for item in values if isinstance(item, bool)]
    if booleans:
        return all(booleans)
    for item in values:
        if isinstance(item, dict):
            nested = _find_compliance(item)
            if nested is not None:
                return nested
    return None


def _rule_id_from_value(value: Any) -> Optional[str]:
    if isinstance(value, str):
        candidate = value.strip()
        if candidate and (candidate[0].isdigit() or "." in candidate):
            return candidate
    return None


def _find_failed_rules(payload: Dict[str, Any]) -> Tuple[str, ...]:
    found: Set[str] = set()
    _collect_failed_rules(payload, found)
    return tuple(sorted(found))


def _collect_failed_rules(value: Any, found: Set[str]) -> None:
    if isinstance(value, dict):
        status = str(value.get("status", value.get("ruleStatus", ""))).lower()
        if status in {"failed", "failure"}:
            clause = value.get("clause")
            test_number = value.get("testNumber", value.get("test_number"))
            if clause is not None and test_number is not None:
                found.add(f"{clause}-{test_number}")
            else:
                for key in ("ruleId", "rule_id", "rule", "clause"):
                    candidate = _rule_id_from_value(value.get(key))
                    if candidate:
                        found.add(candidate)
        failed = value.get("failedChecks") or value.get("failed_checks") or value.get("failed")
        if failed:
            if isinstance(failed, list):
                for item in failed:
                    if isinstance(item, dict):
                        for key in ("ruleId", "rule_id", "rule", "clause", "testNumber"):
                            candidate = _rule_id_from_value(item.get(key))
                            if candidate:
                                found.add(candidate)
            elif isinstance(failed, dict):
                for key in ("ruleId", "rule_id", "rule", "clause", "testNumber"):
                    candidate = _rule_id_from_value(failed.get(key))
                    if candidate:
                        found.add(candidate)
        for child in value.values():
            _collect_failed_rules(child, found)
    elif isinstance(value, list):
        for child in value:
            _collect_failed_rules(child, found)


def parse_verapdf_json(payload: str) -> Tuple[bool, Tuple[str, ...]]:
    try:
        data = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise ValidationError("veraPDF returned invalid JSON.") from exc
    if not isinstance(data, dict):
        raise ValidationError("veraPDF returned an unexpected JSON document.")
    compliant = _find_compliance(data)
    if compliant is None:
        raise ValidationError("veraPDF JSON did not contain a compliance result.")
    return compliant, _find_failed_rules(data)


class VeraPDFValidator:
    def __init__(self, toolchain: Toolchain, timeout_seconds: int = 120) -> None:
        self.toolchain = toolchain
        self.timeout_seconds = timeout_seconds
        self._version: Optional[str] = None

    def version(self) -> str:
        if self._version:
            return self._version
        if not self.toolchain.vera_pdf:
            raise ValidationError("veraPDF is not available.")
        result = run_command(
            [str(self.toolchain.vera_pdf), "--version"],
            cwd=self.toolchain.root,
            environment=self.toolchain.environment,
            timeout_seconds=30,
        )
        if result.timed_out or result.returncode != 0:
            raise ValidationError("veraPDF version could not be determined.")
        self._version = next(
            (line.strip() for line in result.stdout.splitlines() if line.strip()),
            "unknown",
        )
        return self._version

    def list_profiles(self) -> Tuple[str, ...]:
        if not self.toolchain.vera_pdf:
            raise ValidationError("veraPDF is not available.")
        result = run_command(
            [str(self.toolchain.vera_pdf), "--list"],
            cwd=self.toolchain.root,
            environment=self.toolchain.environment,
            timeout_seconds=30,
        )
        if result.timed_out or result.returncode != 0:
            raise ValidationError("veraPDF profiles could not be listed.")
        return tuple(profile for profile in PROFILES if f" {profile} -" in result.stdout)

    def validate(
        self,
        pdf_path: Path,
        profile: str,
        report_path: Path,
        log_path: Path,
    ) -> ValidationResult:
        return self.validate_many(
            [pdf_path],
            profile,
            report_path,
            log_path,
        )[0]

    def validate_many(
        self,
        pdf_paths: List[Path],
        profile: str,
        report_path: Path,
        log_path: Path,
    ) -> List[ValidationResult]:
        if profile not in PROFILES:
            raise ValidationError("Unsupported PDF/UA profile.")
        if not self.toolchain.vera_pdf:
            raise ValidationError("veraPDF is not available.")
        if not pdf_paths:
            return []
        report_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        result = run_command(
            [
                str(self.toolchain.vera_pdf),
                "-f",
                profile,
                "--format",
                "json",
                "--maxfailuresdisplayed",
                "-1",
                "--maxfailures",
                "-1",
                *[str(pdf_path) for pdf_path in pdf_paths],
            ],
            cwd=self.toolchain.root,
            environment=self.toolchain.environment,
            timeout_seconds=self.timeout_seconds,
        )
        report_path.write_text(result.stdout, encoding="utf-8")
        log_path.write_text(result.stderr, encoding="utf-8")
        if result.timed_out:
            raise ValidationError("veraPDF timed out.")
        if result.returncode not in (0, 1):
            raise ValidationError("veraPDF failed to validate the PDF.")
        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError as exc:
            raise ValidationError("veraPDF returned invalid JSON.") from exc
        if not isinstance(data, dict):
            raise ValidationError("veraPDF returned an unexpected JSON document.")
        jobs = data.get("report", {}).get("jobs", [])
        if not isinstance(jobs, list):
            raise ValidationError("veraPDF JSON did not contain validation jobs.")

        jobs_by_name: Dict[str, Dict[str, Any]] = {}
        for job in jobs:
            if not isinstance(job, dict):
                continue
            item = job.get("itemDetails", {})
            name = item.get("name") if isinstance(item, dict) else None
            validation = job.get("validationResult")
            if isinstance(name, str) and isinstance(validation, list) and validation:
                if isinstance(validation[0], dict):
                    if name in jobs_by_name or len(validation) != 1:
                        raise ValidationError("veraPDF returned duplicate or ambiguous validation jobs.")
                    jobs_by_name[name] = validation[0]

        version = self.version()
        results: List[ValidationResult] = []
        for pdf_path in pdf_paths:
            validation = jobs_by_name.get(str(pdf_path))
            if validation is None:
                # veraPDF may normalize the input path; fall back to the single-job
                # result only when the batch contains one file.
                if len(pdf_paths) == 1 and len(jobs) == 1:
                    candidate = jobs[0].get("validationResult", [])
                    validation = candidate[0] if candidate and isinstance(candidate[0], dict) else None
            if not isinstance(validation, dict):
                raise ValidationError("veraPDF did not return a result for every PDF.")
            compliant = validation.get("compliant")
            if not isinstance(compliant, bool):
                raise ValidationError("veraPDF JSON did not contain a compliance result.")
            diagnostics, complete = extract_diagnostics(validation, pdf_path)
            results.append(
                ValidationResult(
                    profile=profile,
                    compliant=compliant,
                    failed_rules=_find_failed_rules(validation),
                    validator_version=version,
                    readable=True,
                    raw_report_path=report_path.name,
                    failed_checks=diagnostics,
                    diagnostics_complete=complete,
                )
            )
        return results
