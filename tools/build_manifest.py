#!/usr/bin/env python3
"""Build the deterministic fixture manifest after baseline PDF generation."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Dict, List

from pypdf import PdfReader


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fixture_id(profile: str, path: Path) -> str:
    stem = path.stem
    if profile == "ua1" and stem.startswith("PDFUA-Ref-"):
        return "ua1-ref-" + stem.removeprefix("PDFUA-Ref-").replace("_", "-").lower()
    return stem


def build(corpus_root: Path) -> Dict[str, object]:
    fixtures: List[Dict[str, object]] = []
    for profile in ("ua1", "ua2"):
        profile_root = corpus_root / profile
        paths = sorted(profile_root.glob("**/*.pdf"))
        profile_items: List[Dict[str, object]] = []
        for path in paths:
            reader = PdfReader(str(path), strict=False)
            relative = path.relative_to(corpus_root).as_posix()
            is_reference = "reference" in path.parts
            profile_items.append(
                {
                    "id": fixture_id(profile, path),
                    "profile": profile,
                    "path": relative,
                    "source": "PDF Association PDF/UA-1 Reference Suite 1.1" if is_reference else "self-authored",
                    "license": "CC-BY-4.0" if is_reference else "CC0-1.0",
                    "sha256": sha256(path),
                    "expected_pages": len(reader.pages),
                }
            )
        ids = [str(item["id"]) for item in profile_items]
        for index, item in enumerate(profile_items):
            item["merge_partner"] = ids[(index + 1) % len(ids)]
            fixtures.append(item)
    return {"schema_version": "0.1", "fixtures": fixtures}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus-root", type=Path, default=Path(__file__).resolve().parents[1] / "corpus")
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "corpus/manifest.json")
    args = parser.parse_args()
    payload = build(args.corpus_root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(payload['fixtures'])} fixture entries to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
