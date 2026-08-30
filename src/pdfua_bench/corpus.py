"""Corpus manifest loading and integrity checks."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Dict, Iterable, List, Tuple

from pypdf import PdfReader

from .models import FixtureSpec


class CorpusError(RuntimeError):
    """A safe, user-facing corpus error."""


@dataclass(frozen=True)
class Corpus:
    root: Path
    fixtures: Tuple[FixtureSpec, ...]
    manifest_path: Path

    def by_id(self) -> Dict[str, FixtureSpec]:
        return {fixture.fixture_id: fixture for fixture in self.fixtures}

    def file_path(self, fixture: FixtureSpec) -> Path:
        relative = PurePosixPath(fixture.path)
        if relative.is_absolute() or ".." in relative.parts:
            raise CorpusError("A corpus path must remain inside the corpus directory.")
        candidate = self.root / Path(*relative.parts)
        try:
            resolved_root = self.root.resolve()
            resolved_candidate = candidate.resolve(strict=True)
            resolved_candidate.relative_to(resolved_root)
        except (OSError, ValueError) as exc:
            raise CorpusError("A corpus file is missing or escapes the corpus directory.") from exc
        return resolved_candidate


def _read_json(path: Path) -> Dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(stream)
    except (OSError, ValueError) as exc:
        raise CorpusError("The corpus manifest could not be read.") from exc
    if not isinstance(value, dict):
        raise CorpusError("The corpus manifest must contain an object.")
    return value


def _fixture_from_value(value: Any) -> FixtureSpec:
    if not isinstance(value, dict):
        raise CorpusError("Each corpus fixture must be an object.")
    try:
        fixture = FixtureSpec(
            fixture_id=str(value["id"]),
            profile=str(value["profile"]),
            path=str(value["path"]),
            source=str(value["source"]),
            license=str(value["license"]),
            sha256=str(value["sha256"]).lower(),
            expected_pages=int(value["expected_pages"]),
            merge_partner=str(value["merge_partner"]),
        )
        fixture.validate()
        return fixture
    except (KeyError, TypeError, ValueError) as exc:
        raise CorpusError("A corpus fixture is missing a valid required field.") from exc


def load_corpus(manifest_path: Path) -> Corpus:
    manifest = manifest_path.expanduser()
    payload = _read_json(manifest)
    fixtures_value = payload.get("fixtures")
    if not isinstance(fixtures_value, list) or not fixtures_value:
        raise CorpusError("The corpus manifest must contain a non-empty fixtures list.")

    fixtures = tuple(_fixture_from_value(value) for value in fixtures_value)
    ids = [fixture.fixture_id for fixture in fixtures]
    paths = [fixture.path for fixture in fixtures]
    if len(set(ids)) != len(ids):
        raise CorpusError("Corpus fixture IDs must be unique.")
    if len(set(paths)) != len(paths):
        raise CorpusError("Corpus fixture paths must be unique.")

    by_id = {fixture.fixture_id: fixture for fixture in fixtures}
    for fixture in fixtures:
        partner = by_id.get(fixture.merge_partner)
        if partner is None or partner.profile != fixture.profile:
            raise CorpusError("Every fixture must have a merge partner with the same profile.")

    root = manifest.parent.resolve()
    return Corpus(root=root, fixtures=fixtures, manifest_path=manifest.resolve())


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
    except OSError as exc:
        raise CorpusError("A corpus file could not be read.") from exc
    return digest.hexdigest()


def inspect_pdf(path: Path) -> Tuple[bool, int, str]:
    """Return readability, page count, and a non-sensitive error message."""

    try:
        reader = PdfReader(str(path), strict=False)
        return True, len(reader.pages), ""
    except Exception:
        return False, 0, "The file could not be parsed as a PDF."


def verify_corpus_files(corpus: Corpus) -> List[str]:
    errors: List[str] = []
    for fixture in corpus.fixtures:
        try:
            path = corpus.file_path(fixture)
        except CorpusError as exc:
            errors.append(f"{fixture.fixture_id}: {exc}")
            continue
        digest = sha256_file(path)
        if digest != fixture.sha256:
            errors.append(f"{fixture.fixture_id}: SHA-256 does not match the manifest.")
        readable, pages, error = inspect_pdf(path)
        if not readable:
            errors.append(f"{fixture.fixture_id}: {error}")
        elif pages != fixture.expected_pages:
            errors.append(
                f"{fixture.fixture_id}: expected {fixture.expected_pages} page(s), found {pages}."
            )
    return errors
