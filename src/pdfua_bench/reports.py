"""Public-safe JSON and Markdown report rendering."""

from __future__ import annotations

import json
import html
import shlex
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping

from .models import CLASSIFICATIONS, RunReport


def json_text(report: RunReport, include_raw_paths: bool = False) -> str:
    return (
        json.dumps(
            report.to_dict(include_raw_paths=include_raw_paths),
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )


def _cell(value: Any) -> str:
    text = html.escape(str(value)).replace("`", "&#96;").replace("|", "\\|").replace("\n", " ").replace("\r", " ")
    return text


def _matrix_lines(cases: Iterable[Mapping[str, Any]]) -> List[str]:
    grouped: Dict[tuple, Counter] = {}
    for case in cases:
        key = (case.get("profile", ""), case.get("tool", ""), case.get("operation", ""))
        grouped.setdefault(key, Counter())[case.get("classification", "")] += 1
    lines = [
        "## Compatibility matrix",
        "",
        "| Profile | Tool | Operation | Total | Passed | New PDF/UA violations | Other |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for (profile, tool, operation), counts in sorted(grouped.items()):
        total = sum(counts.values())
        passed = counts.get("passed", 0)
        violations = counts.get("new_pdfua_violation", 0)
        other = total - passed - violations
        lines.append(
            f"| `{_cell(profile)}` | `{_cell(tool)}` | `{_cell(operation)}` | {total} | {passed} | {violations} | {other} |"
        )
    return lines


def _diagnostic_lines(cases):
    from .run_diff import SAFE_ID
    from .models import TOOLS, OPERATIONS, PROFILES
    lines = ["", "## Diagnostics and reproduction", ""]
    for case in cases:
        if not isinstance(case, dict) or case.get("classification") == "passed":
            continue
        lines += [f"### {_cell(case.get('case_id', 'unknown'))}", "",
                  f"Classification: {_cell(case.get('classification', 'unknown'))}"]
        if case.get("details"):
            lines += [_cell(case["details"])]
        for index, validation in enumerate(case.get("output_validation", []), 1):
            if not isinstance(validation, dict):
                continue
            for rule in validation.get("failed_rules", []):
                lines += [f"- Output {index}: PDF/UA rule {_cell(rule)}"]
            if validation.get("error"):
                lines += [f"- Output {index}: {_cell(validation['error'])}"]
        before, after = case.get("before_structure", {}), case.get("after_structure", [])
        from .run_diff import FIELDS
        if isinstance(before, dict) and isinstance(after, list) and after and all(isinstance(s, dict) and s.get("readable") for s in after):
            for field in FIELDS:
                values = [s.get(field) for s in after]
                if type(before.get(field)) not in (int, bool) or any(type(v) != type(before[field]) for v in values):
                    continue
                observed = all(values) if type(before[field]) is bool else sum(values)
                if observed != before[field]:
                    lines += [f"- {_cell(field)}: {_cell(before[field])} → {_cell(observed)}"]
        fixture = case.get("fixture_id", "")
        if isinstance(fixture, str) and SAFE_ID.fullmatch(fixture) and case.get("tool") in TOOLS and case.get("operation") in OPERATIONS and case.get("profile") in PROFILES:
            command = shlex.join(["pdfua-bench", "run", "--profiles", case["profile"], "--tools", case["tool"], "--operations", case["operation"], "--fixtures", fixture, "--output", "lab/reproduction.json"])
            lines += ["", "```sh", command, "```", ""]
    lines += ["Use the recorded tool versions and corpus. Output numbers refer to result order, not inferred PDF page/object locations.", ""]
    return lines


def markdown_text(report: RunReport) -> str:
    summary = report.summary()
    configuration = report.configuration
    lines = [
        "# PDF Accessibility Roundtrip Bench report",
        "",
        f"- Run ID: `{_cell(report.run_id)}`",
        f"- Started: `{_cell(report.started_at)}`",
        f"- Ended: `{_cell(report.ended_at)}`",
        f"- Profiles: `{', '.join(configuration.get('profiles', []))}`",
        f"- Tools: `{', '.join(configuration.get('tools', []))}`",
        f"- Operations: `{', '.join(configuration.get('operations', []))}`",
        "",
        "## Summary",
        "",
        "| Classification | Cases |",
        "| --- | ---: |",
    ]
    for classification in CLASSIFICATIONS:
        lines.append(f"| `{classification}` | {summary.get(classification, 0)} |")
    lines.append(f"| **Total** | **{summary.get('total', 0)}** |")
    lines.extend(["", *_matrix_lines([case.to_dict(include_raw_paths=False) for case in report.cases])])
    lines.extend(["", "## Environment", "", "| Field | Value |", "| --- | --- |"])
    for key, value in sorted(report.environment.items()):
        lines.append(f"| `{_cell(key)}` | `{_cell(value)}` |")

    lines.extend(["", "## Tool versions", "", "| Tool | Version |", "| --- | --- |"])
    tool_versions = configuration.get("tool_versions", {})
    for tool, version in sorted(tool_versions.items()):
        lines.append(f"| `{_cell(tool)}` | `{_cell(version)}` |")
    if configuration.get("verapdf_version"):
        lines.append(
            f"| `verapdf` | `{_cell(configuration['verapdf_version'])}` |"
        )

    lines.extend(
        [
            "",
            "## Cases",
            "",
            "| Fixture | Profile | Tool | Operation | Classification | Duration (ms) |",
            "| --- | --- | --- | --- | --- | ---: |",
        ]
    )
    for case in report.cases:
        lines.append(
            "| `{fixture}` | `{profile}` | `{tool}` | `{operation}` | `{classification}` | {duration} |".format(
                fixture=_cell(case.fixture_id),
                profile=_cell(case.profile),
                tool=_cell(case.tool),
                operation=_cell(case.operation),
                classification=_cell(case.classification),
                duration=case.transformation.duration_ms,
            )
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "This report covers machine-verifiable PDF/UA checks and limited structural signals. "
            "It is not a complete manual screen-reader accessibility assessment.",
            "",
        ]
    )
    lines.extend(_diagnostic_lines([case.to_dict(include_raw_paths=False) for case in report.cases]))
    return "\n".join(lines)


def markdown_from_dict(payload: Mapping[str, Any]) -> str:
    lines = [
        "# PDF Accessibility Roundtrip Bench report",
        "",
        f"- Run ID: `{_cell(payload.get('run_id', 'unknown'))}`",
        f"- Started: `{_cell(payload.get('started_at', 'unknown'))}`",
        f"- Ended: `{_cell(payload.get('ended_at', 'unknown'))}`",
    ]
    configuration = payload.get("configuration", {})
    if isinstance(configuration, dict):
        lines.extend(
            [
                f"- Profiles: `{', '.join(configuration.get('profiles', []))}`",
                f"- Tools: `{', '.join(configuration.get('tools', []))}`",
                f"- Operations: `{', '.join(configuration.get('operations', []))}`",
            ]
        )
    lines.extend(["", "## Summary", "", "| Classification | Cases |", "| --- | ---: |"])
    summary = payload.get("summary", {})
    if not isinstance(summary, dict):
        summary = {}
    for classification in CLASSIFICATIONS:
        lines.append(f"| `{classification}` | {summary.get(classification, 0)} |")
    lines.append(f"| **Total** | **{summary.get('total', 0)}** |")
    cases = payload.get("cases", [])
    if not isinstance(cases, list):
        cases = []
    lines.extend(["", *_matrix_lines([case for case in cases if isinstance(case, dict)])])
    lines.extend(["", "## Environment", "", "| Field | Value |", "| --- | --- |"])
    environment = payload.get("environment", {})
    if isinstance(environment, dict):
        for key, value in sorted(environment.items()):
            lines.append(f"| `{_cell(key)}` | `{_cell(value)}` |")
    lines.extend(["", "## Tool versions", "", "| Tool | Version |", "| --- | --- |"])
    tool_versions = configuration.get("tool_versions", {}) if isinstance(configuration, dict) else {}
    if isinstance(tool_versions, dict):
        for tool, version in sorted(tool_versions.items()):
            lines.append(f"| `{_cell(tool)}` | `{_cell(version)}` |")
    if isinstance(configuration, dict) and configuration.get("verapdf_version"):
        lines.append(f"| `verapdf` | `{_cell(configuration['verapdf_version'])}` |")
    lines.extend(["", "## Cases", "", "| Fixture | Profile | Tool | Operation | Classification |", "| --- | --- | --- | --- | --- |"])
    if cases:
        for case in cases:
            if not isinstance(case, dict):
                continue
            transformation = case.get("transformation", {})
            duration = transformation.get("duration_ms", "") if isinstance(transformation, dict) else ""
            lines.append(
                "| `{fixture}` | `{profile}` | `{tool}` | `{operation}` | `{classification}` |".format(
                    fixture=_cell(case.get("fixture_id", "")),
                    profile=_cell(case.get("profile", "")),
                    tool=_cell(case.get("tool", "")),
                    operation=_cell(case.get("operation", "")),
                    classification=_cell(case.get("classification", "")),
                )
            )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "This report covers machine-verifiable PDF/UA checks and limited structural signals. "
            "It is not a complete manual screen-reader accessibility assessment.",
            "",
        ]
    )
    lines.extend(_diagnostic_lines(cases))
    return "\n".join(lines)


def load_json(path: Path) -> Dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as stream:
            payload = json.load(stream)
    except (OSError, ValueError) as exc:
        raise ValueError("The run report could not be read as JSON.") from exc
    if not isinstance(payload, dict):
        raise ValueError("The run report must contain an object.")
    return payload
