"""Explicit, bounded, integrity-checked single-case reproduction packages."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import re
import stat
import tempfile
import zipfile
from pathlib import Path
from importlib.metadata import version

from .corpus import load_corpus, verify_corpus_files
from .run_diff import _index, _context, _signals, compare_runs, comparison_exit_code
from .runner import analyzer_fingerprint, environment_snapshot, run_benchmark
from .validators import VeraPDFValidator
from .adapters.factory import build_adapters


MAX_BYTES = 256 * 1024 * 1024
MAX_MEMBERS = 512
FILES = {"case.json", "corpus/manifest.json", "LICENSE", "ATTRIBUTIONS.md", "REPRODUCE.md"}
PDF_NAME = re.compile(r"(?:corpus/pdfs/input|outputs/output)-[1-9][0-9]*\.pdf\Z")


def _json(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def _hash(value):
    return hashlib.sha256(value).hexdigest()


def _read_bounded(path, budget):
    if budget < 0:
        raise ValueError("Package exceeds the size limit.")
    with path.open("rb") as stream:
        data = stream.read(budget + 1)
    if len(data) > budget:
        raise ValueError("Document exceeds the package size limit.")
    return data


def _read_json_bytes(data):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError("Duplicate JSON keys are not accepted.")
            result[key] = value
        return result
    def constant(value):
        raise ValueError("Non-finite JSON numbers are not accepted.")
    return json.loads(data, object_pairs_hook=pairs, parse_constant=constant)


def _case_report(report, case_id):
    _index(report)
    selected = [c for c in report["cases"] if c["case_id"] == case_id]
    if len(selected) != 1 or report.get("schema_version") != "0.3":
        raise ValueError("Select exactly one case from a v0.3 run.")
    case = selected[0]
    context = _context(report, case)
    if not context or _signals(case, context["validator"]) is None:
        raise ValueError("Incomplete or inconsistent case evidence cannot be exported.")
    if case["case_id"] != "{fixture_id}-{tool}-{operation}".format(**case):
        raise ValueError("Case identity does not match its fixture and operation.")
    if any(v.get("diagnostics_complete") is not True for v in case["output_validation"]):
        raise ValueError("Complete diagnostic coverage is required for a reproduction package.")
    result = copy.deepcopy(report)
    result["cases"] = [copy.deepcopy(case)]
    result["summary"] = {case["classification"]: 1, "total": 1}
    result["configuration"].update(expected_case_count=1, fixture_count=1,
                                   profiles=[case["profile"]], tools=[case["tool"]], operations=[case["operation"]])
    return result


def export_case(report, case_id, corpus, run_dir, output, include_pdfs=False):
    if not include_pdfs:
        raise ValueError("Export includes document content; pass --include-pdfs after reviewing its sharing permissions.")
    evidence = _case_report(report, case_id)
    case = evidence["cases"][0]
    if verify_corpus_files(corpus):
        raise ValueError("Corpus integrity verification failed.")
    if run_dir.name != report.get("run_id"):
        raise ValueError("Run directory must match the report run_id.")
    case_dir = (run_dir / "cases" / case_id).resolve(strict=True)
    case_dir.relative_to(run_dir.resolve(strict=True))
    members = {"case.json": _json(evidence)}
    fixtures = []
    expected_inputs = case["provenance"]["inputs"]
    for i, declared in enumerate(expected_inputs, 1):
        fixture = corpus.by_id().get(declared["id"])
        if not fixture or fixture.sha256 != declared["sha256"] or fixture.expected_pages != declared["pages"] or fixture.profile != case["profile"]:
            raise ValueError("Input provenance does not match the selected corpus.")
        data = _read_bounded(corpus.file_path(fixture), MAX_BYTES - sum(map(len, members.values())))
        if _hash(data) != declared["sha256"]:
            raise ValueError("Input changed during export.")
        members["corpus/pdfs/input-%d.pdf" % i] = data
        item = fixture.to_dict()
        item["path"] = "pdfs/input-%d.pdf" % i
        item["merge_partner"] = expected_inputs[-1]["id"] if i == 1 else expected_inputs[0]["id"]
        fixtures.append(item)
    original = corpus.by_id()[case["fixture_id"]]
    if case["operation"] == "merge" and original.merge_partner != expected_inputs[-1]["id"]:
        raise ValueError("Merge partner differs from recorded provenance.")
    outputs = case["provenance"].get("outputs", [])
    if len(outputs) != len(case["output_validation"]):
        raise ValueError("Output fingerprints are incomplete.")
    for i, item in enumerate(outputs, 1):
        name = case["transformation"]["output_files"][i - 1]
        if item.get("path") != name or not re.fullmatch(r"outputs/(?:merged|resaved)\.pdf|outputs/split/[A-Za-z0-9_.-]+\.pdf", name):
            raise ValueError("Unsafe or inconsistent output path.")
        path = case_dir / name
        path.resolve(strict=True).relative_to(case_dir)
        data = _read_bounded(path, MAX_BYTES - sum(map(len, members.values())))
        if _hash(data) != item.get("sha256"):
            raise ValueError("Output bytes differ from the recorded measurement.")
        members["outputs/output-%d.pdf" % i] = data
    members["corpus/manifest.json"] = _json({"schema_version": "1", "fixtures": fixtures})
    source = Path(__file__).resolve().parents[2]
    for name in ("LICENSE", "ATTRIBUTIONS.md"):
        path = source / name
        if not path.is_file():
            path = Path(__file__).parent / "data" / name
        members[name] = path.read_bytes()
    members["REPRODUCE.md"] = (
        "# Single-case reproduction\n\n"
        "This package contains PDF document content. Review licensing and privacy before sharing.\n"
        "The bundled manifest records original fixture source and license metadata.\n"
        "Install the matching pdfua-bench release and recorded PDF tools, then run:\n\n"
        "    pdfua-bench verify-bundle --bundle case.zip\n"
        "    pdfua-bench reproduce --bundle case.zip --output lab/reproduced.json\n\n"
        "Verification reads data only. Reproduction checks the recorded environment and invokes\n"
        "only the built-in adapter. It never executes commands from the archive.\n"
        "Hashes check integrity, not publisher authenticity. The new run may have different PDF\n"
        "bytes due to timestamps; compare recorded semantic signals, not output-byte equality.\n"
    ).encode()
    if len(members) >= MAX_MEMBERS or sum(map(len, members.values())) > MAX_BYTES:
        raise ValueError("Reproduction package exceeds the size limit.")
    manifest = {"schema_version": "0.3-case-bundle", "case_id": case_id,
                "members": {k: {"sha256": _hash(v), "size": len(v)} for k, v in members.items()}}
    members["manifest.json"] = _json(manifest)
    output.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(output, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "wb") as stream, zipfile.ZipFile(stream, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(members.items()):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100600 << 16
            archive.writestr(info, data)
    return manifest


def verify_bundle(path):
    try:
        with zipfile.ZipFile(path) as archive:
            items = archive.infolist()
            names = [i.filename for i in items]
            if not items or len(items) > MAX_MEMBERS or len(set(names)) != len(names) or sum(i.file_size for i in items) > MAX_BYTES:
                raise ValueError("Archive size or member count is invalid.")
            for item in items:
                if item.filename not in FILES | {"manifest.json"} and not PDF_NAME.fullmatch(item.filename):
                    raise ValueError("Unexpected archive member.")
                if stat.S_ISLNK(item.external_attr >> 16) or item.flag_bits & 1:
                    raise ValueError("Symlink or encrypted archive member rejected.")
            members = {name: archive.read(name) for name in names}
        manifest = _read_json_bytes(members.pop("manifest.json"))
        if manifest.get("schema_version") != "0.3-case-bundle" or set(manifest["members"]) != set(members) or not FILES.issubset(members):
            raise ValueError("Incomplete package manifest.")
        for name, data in members.items():
            if manifest["members"][name] != {"sha256": _hash(data), "size": len(data)}:
                raise ValueError("Bundle checksum mismatch.")
        report = _read_json_bytes(members["case.json"])
        evidence = _case_report(report, manifest["case_id"])
        case = evidence["cases"][0]
        corpus_doc = _read_json_bytes(members["corpus/manifest.json"])
        inputs = case["provenance"]["inputs"]
        fixtures = corpus_doc["fixtures"]
        if len(fixtures) != len(inputs):
            raise ValueError("Bundled input count is inconsistent.")
        expected_pdfs = set()
        for i, (item, source) in enumerate(zip(fixtures, inputs), 1):
            name = "corpus/pdfs/input-%d.pdf" % i
            expected_pdfs.add(name)
            if item["id"] != source["id"] or item["path"] != "pdfs/input-%d.pdf" % i or item["profile"] != case["profile"] or item["expected_pages"] != source["pages"] or item["sha256"] != source["sha256"] or _hash(members[name]) != source["sha256"]:
                raise ValueError("Bundled input provenance differs from case evidence.")
            expected_partner = inputs[-1]["id"] if i == 1 else inputs[0]["id"]
            if item["merge_partner"] != expected_partner or not item.get("license") or not item.get("source"):
                raise ValueError("Missing licensing or inconsistent merge partner.")
        outputs = case["provenance"].get("outputs", [])
        if len(outputs) != len(case["output_validation"]):
            raise ValueError("Missing output provenance.")
        for i, item in enumerate(outputs, 1):
            name = "outputs/output-%d.pdf" % i
            expected_pdfs.add(name)
            if _hash(members[name]) != item["sha256"] or item["path"] != case["transformation"]["output_files"][i - 1]:
                raise ValueError("Bundled output provenance differs from case evidence.")
        if set(members) - FILES != expected_pdfs:
            raise ValueError("Unexpected document content in bundle.")
        return manifest, evidence, members
    except (KeyError, TypeError, AttributeError, IndexError, RecursionError, zipfile.BadZipFile, UnicodeError) as exc:
        raise ValueError("Malformed reproduction package.") from exc


def reproduce_bundle(bundle, toolchain, output):
    manifest, expected, members = verify_bundle(bundle)
    case = expected["cases"][0]
    context = _context(expected, case)
    actual_env = environment_snapshot(toolchain)
    if context["analyzer"] != analyzer_fingerprint() or any(actual_env[k] != value for k, value in context["environment"].items()):
        raise ValueError("Analyzer or environment differs from recorded evidence; exact reproduction stopped.")
    if any(version(k) != value for k, value in context["packages"].items()) or VeraPDFValidator(toolchain).version() != context["validator"]:
        raise ValueError("Validator or Python dependency version differs from recorded evidence.")
    adapter = build_adapters(toolchain)[case["tool"]]
    if adapter.version() != expected["configuration"]["tool_versions"][case["tool"]]:
        raise ValueError("Processing tool version differs from recorded evidence.")
    if output.exists() or output.is_symlink():
        raise ValueError("Choose a new output path.")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="pdfua-reproduce-", dir=output.parent.resolve()) as directory:
        root = Path(directory)
        for name, data in members.items():
            if name.startswith("corpus/"):
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
        corpus = load_corpus(root / "corpus/manifest.json")
        report = run_benchmark(corpus, toolchain, [case["profile"]], [case["tool"]], [case["operation"]], output.parent, [case["fixture_id"]])
    comparison = compare_runs(expected, report.to_dict(False))
    return report, comparison_exit_code(comparison)
