"""Conservative comparison of recorded runs. Reports are data, never commands."""
from __future__ import annotations
import re
import shlex
from .models import CLASSIFICATIONS, PROFILES, TOOLS, OPERATIONS

VALID = {"passed", "new_pdfua_violation", "structure_signal_changed"}
SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,180}\Z")
HASH = re.compile(r"[0-9a-f]{64}\Z")
FIELDS = ("page_count", "struct_tree_present", "marked_pdf", "alt_text_count", "role_map_count", "document_language_present", "title_present", "outline_count")


def _index(report):
    if not isinstance(report, dict):
        raise ValueError("A run must be an object.")
    cases = report.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("A run must contain a nonempty cases list.")
    result = {}
    for case in cases:
        if not isinstance(case, dict):
            raise ValueError("Every case must be an object.")
        for key in ("case_id", "fixture_id"):
            if not isinstance(case.get(key), str) or not SAFE_ID.fullmatch(case[key]):
                raise ValueError("Case and fixture identifiers must be safe, nonempty identifiers.")
        if case.get("profile") not in PROFILES or case.get("tool") not in TOOLS or case.get("operation") not in OPERATIONS or case.get("classification") not in CLASSIFICATIONS:
            raise ValueError("Unknown case profile, tool, operation or classification.")
        key = (case["fixture_id"], case["profile"], case["tool"], case["operation"])
        if key in result:
            raise ValueError("Duplicate case identities are not comparable.")
        result[key] = case
    return result


def _context(report, case):
    config = report.get("configuration", {})
    env = report.get("environment", {})
    provenance = case.get("provenance", {})
    if report.get("schema_version") not in ("0.2", "0.3") or not isinstance(config, dict) or not isinstance(env, dict) or not isinstance(provenance, dict):
        return None
    if type(config.get("expected_case_count")) is not int or config["expected_case_count"] != len(report["cases"]):
        return None
    expected_protocol = "pdfua-roundtrip-v3" if report["schema_version"] == "0.3" else "pdfua-roundtrip-v2"
    if config.get("comparison_protocol") != expected_protocol or not HASH.fullmatch(str(config.get("analyzer_sha256", ""))):
        return None
    if report["schema_version"] == "0.3":
        outputs = case.get("output_validation")
        if not isinstance(outputs, list) or not outputs:
            return None
        for output in outputs:
            if not isinstance(output, dict) or output.get("diagnostics_complete") is not True:
                return None
            checks = output.get("failed_checks")
            if not isinstance(checks, list) or any(not isinstance(c, dict) for c in checks):
                return None
            rules = output.get("failed_rules")
            if not isinstance(rules, list) or any(not isinstance(r, str) for r in rules):
                return None
            if any(not isinstance(c.get("rule_id"), str) for c in checks) or {c["rule_id"] for c in checks} != set(rules):
                return None
    inputs = provenance.get("inputs")
    expected = 2 if case["operation"] == "merge" else 1
    if not isinstance(inputs, list) or len(inputs) != expected:
        return None
    for item in inputs:
        if not isinstance(item, dict) or not SAFE_ID.fullmatch(str(item.get("id", ""))) or not HASH.fullmatch(str(item.get("sha256", ""))) or type(item.get("pages")) is not int or item["pages"] < 1:
            return None
    if inputs[0]["id"] != case["fixture_id"]:
        return None
    parameters = provenance.get("parameters")
    if parameters != {"operation": case["operation"], "adapter_defaults": "v1"}:
        return None
    versions = config.get("tool_versions", {})
    if not isinstance(versions, dict) or not isinstance(versions.get(case["tool"]), str) or versions[case["tool"]] in ("", "unavailable", "unknown"):
        return None
    packages = config.get("python_packages")
    if not isinstance(packages, dict) or any(not isinstance(packages.get(k), str) or not packages[k] for k in ("pypdf", "reportlab")):
        return None
    required_env = ("os", "os_version", "architecture", "python", "java")
    if any(not isinstance(env.get(k), str) or not env[k] or env[k] == "unavailable" for k in required_env):
        return None
    validator = config.get("verapdf_version")
    if not isinstance(validator, str) or validator in ("", "unknown", "unavailable"):
        return None
    return {"protocol": expected_protocol, "inputs": inputs, "parameters": parameters, "validator": validator,
            "environment": {k: env[k] for k in required_env}, "packages": packages,
            "analyzer": config["analyzer_sha256"]}


def _signals(case, validator_version):
    if case["classification"] not in VALID:
        return None
    base = case.get("baseline")
    transformation = case.get("transformation")
    outputs = case.get("output_validation")
    before = case.get("before_structure")
    after = case.get("after_structure")
    if not isinstance(base, dict) or base.get("compliant") is not True or base.get("readable") is not True or base.get("error") or base.get("validator_version") != validator_version or base.get("profile") != case["profile"] or base.get("failed_rules") != []:
        return None
    if not isinstance(transformation, dict) or transformation.get("completed") is not True or transformation.get("error"):
        return None
    if not isinstance(outputs, list) or not outputs or not isinstance(after, list) or len(outputs) != len(after) or not isinstance(transformation.get("output_files"), list) or len(outputs) != len(transformation["output_files"]):
        return None
    for s in [before, *after]:
        if not isinstance(s, dict) or s.get("readable") is not True or s.get("error") or any(k not in s for k in FIELDS):
            return None
        if any(type(s[k]) is not int or s[k] < 0 for k in ("page_count", "alt_text_count", "role_map_count", "outline_count")) or s["page_count"] < 1:
            return None
        if any(type(s[k]) is not bool for k in ("struct_tree_present", "marked_pdf", "document_language_present", "title_present")):
            return None
    if before["page_count"] != sum(item["pages"] for item in case["provenance"]["inputs"]):
        return None
    signals = set()
    for index, result in enumerate(outputs, 1):
        if not isinstance(result, dict) or result.get("readable") is not True or result.get("error") or result.get("validator_version") != validator_version or result.get("profile") != case["profile"] or type(result.get("compliant")) is not bool:
            return None
        rules = result.get("failed_rules")
        if not isinstance(rules, list) or any(not isinstance(r, str) or not r or len(r) > 200 for r in rules):
            return None
        if result["compliant"] == bool(rules):
            return None
        signals.update(f"output-{index}:pdfua:{rule}" for rule in rules)
    for field in FIELDS:
        observed = all(s[field] for s in after) if type(before[field]) is bool else sum(s[field] for s in after)
        if observed != before[field]:
            signals.add(f"structure:{field}:{before[field]}->{observed}")
    expected_class = "new_pdfua_violation" if any(":pdfua:" in s for s in signals) else "structure_signal_changed" if signals else "passed"
    if case["classification"] != expected_class:
        return None
    return signals


def compare_runs(before, after):
    left, right = _index(before), _index(after)
    rows = []
    for key in sorted(set(left) | set(right)):
        a, b = left.get(key), right.get(key)
        row = dict(zip(("fixture", "profile", "tool", "operation"), key))
        row.update(new=[], persistent=[], no_longer_observed=[], status="not_comparable", reason="")
        row["reproduce"] = shlex.join(["pdfua-bench", "run", "--profiles", key[1], "--tools", key[2], "--operations", key[3], "--fixtures", key[0], "--output", "lab/reproduction.json"])
        if a is None or b is None:
            row["reason"] = "Case missing from one run."
        else:
            ca, cb = _context(before, a), _context(after, b)
            if ca is not None and cb is not None:
                row["tool_versions"] = {"before": before["configuration"]["tool_versions"][key[2]], "after": after["configuration"]["tool_versions"][key[2]]}
            if ca is None or cb is None:
                row["reason"] = "Missing or unsupported provenance; legacy reports require a fresh run."
            elif ca != cb:
                row["reason"] = "Comparison context differs: " + ", ".join(k for k in ca if ca[k] != cb[k]) + "."
            else:
                sa, sb = _signals(a, ca["validator"]), _signals(b, cb["validator"])
                if sa is None or sb is None:
                    row["reason"] = "Incomplete, invalid, or internally inconsistent case evidence."
                else:
                    row.update(new=sorted(sb-sa), persistent=sorted(sa & sb), no_longer_observed=sorted(sa-sb), status="comparable")
        rows.append(row)
    return {"schema_version": "0.2-diff", "cases": rows, "summary": {
        "cases": len(rows), "comparable": sum(r["status"] == "comparable" for r in rows),
        "not_comparable": sum(r["status"] != "comparable" for r in rows),
        **{kind: sum(len(r[kind]) for r in rows) for kind in ("new", "persistent", "no_longer_observed")},
    }}


def comparison_exit_code(result):
    return 2 if result["summary"]["not_comparable"] else 1 if result["summary"]["new"] else 0


def comparison_markdown(result):
    from .reports import _cell
    lines = ["# PDF/UA run comparison", "", "## Summary", ""]
    lines += [f"- {key}: {value}" for key, value in result["summary"].items()]
    lines += ["", "## Case details", ""]
    for row in result["cases"]:
        lines += [f"### {row['fixture']} / {row['tool']} / {row['operation']}", "", f"Status: {row['status']}"]
        if row["reason"]:
            lines += [row["reason"]]
        if "tool_versions" in row:
            lines += ["Tool version: " + _cell(row["tool_versions"]["before"]) + " → " + _cell(row["tool_versions"]["after"])]
        for kind in ("new", "persistent", "no_longer_observed"):
            lines += [f"- {kind}: " + ("; ".join(_cell(s) for s in row[kind]) or "none")]
        lines += ["", "Reproduce after selecting the recorded tool versions and matching corpus:", "", "```sh", row["reproduce"], "```", ""]
    lines += ["Output numbers identify result order, not an inferred PDF page/object location.",
              "No-longer-observed signals describe these two valid runs, not a universal repair claim.", ""]
    return "\n".join(lines)
