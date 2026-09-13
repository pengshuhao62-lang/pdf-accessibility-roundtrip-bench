"""Evidence-linked veraPDF locations. Never infer a page from an output number."""
import hashlib
import re

from pypdf import PdfReader


PAGE = re.compile(r"^root/document\[0\]/pages\[(\d+)\]\((\d+) (\d+) obj PDPage\)(?:/|$)")
OBJECT = re.compile(r"\((\d+) (\d+) obj ([A-Za-z][A-Za-z0-9]*)\)")
RULE = re.compile(r"[0-9]+(?:\.[0-9]+)*-[0-9]+\Z")
# Only model-path names, never parenthesized font names, text, URIs or messages.
SEGMENTS = {"root", "document", "pages", "contentStream", "operators", "font", "DescendantFonts",
            "usedGlyphs", "structureTree", "StructTreeRoot", "K", "children", "kids", "Kids", "annots",
            "annotations", "metadata", "catalog", "resources", "XObject", "xObjects", "fonts", "action",
            "OpenAction", "ParentTree", "RoleMap", "names", "embeddedFiles", "outline", "outlines"}


def safe_context(context):
    context = re.sub(r"\([^)]*\)", "", context)
    result = []
    for segment in context.split("/"):
        match = re.fullmatch(r"([A-Za-z][A-Za-z0-9]*)(\[\d+\])?", segment)
        result.append((match[1] + (match[2] or "")) if match and match[1] in SEGMENTS else "[model-segment]")
    return "/".join(result)


def extract_diagnostics(validation, pdf_path):
    """Keep each failed check, verify page anchors, and mark missing coverage.

    Rule counts remain independent of this additive diagnostic layer. Completeness
    means all reported failed checks were captured, not that every check has a page.
    """
    page_refs = []
    try:
        reader = PdfReader(str(pdf_path), strict=False)
        for page in reader.pages:
            ref = page.indirect_reference
            page_refs.append((ref.idnum, ref.generation) if ref else None)
    except Exception:
        pass
    details = validation.get("details", {})
    if not isinstance(details, dict):
        return (), False
    rules = details.get("ruleSummaries", [])
    if not isinstance(rules, list):
        return (), False
    records, total = [], 0
    complete = True
    for i, rule in enumerate(rules):
        if not isinstance(rule, dict):
            complete = False
            continue
        if str(rule.get("status", rule.get("ruleStatus", ""))).lower() != "failed":
            continue
        rule_id = "%s-%s" % (rule.get("clause", ""), rule.get("testNumber", ""))
        if not RULE.fullmatch(rule_id):
            complete = False
            continue
        checks = rule.get("checks", [])
        if not isinstance(checks, list):
            complete = False
            continue
        count = 0
        for j, check in enumerate(checks):
            if not isinstance(check, dict) or str(check.get("status", "")).lower() != "failed":
                continue
            count += 1
            raw = check.get("context")
            context = raw if isinstance(raw, str) else ""
            anchor = PAGE.match(context)
            page_number = None
            if anchor:
                index, number, generation = map(int, anchor.groups())
                if index < len(page_refs) and page_refs[index] == (number, generation):
                    page_number = index + 1
            records.append({
                "rule_id": rule_id,
                "report_pointer": "/details/ruleSummaries/%d/checks/%d" % (i, j),
                "context_path": safe_context(context) if context else "",
                "context_sha256": hashlib.sha256(context.encode()).hexdigest(),
                "object_references": [{"number": int(m[0]), "generation": int(m[1]), "model_type": m[2]}
                                      for m in OBJECT.findall(context)],
                "page": page_number,
                "location_status": "verified-page-object" if page_number else "unresolved",
                "location_note": "Page object and zero-based validator index agree." if page_number else
                                 "No uniquely verified page anchor; object references are validator-reported.",
            })
        if type(rule.get("failedChecks")) is not int or count != rule["failedChecks"]:
            complete = False
        total += count
    if type(details.get("failedChecks")) is not int or total != details["failedChecks"]:
        complete = False
    if not validation.get("compliant") and not records:
        complete = False
    return tuple(records), complete
