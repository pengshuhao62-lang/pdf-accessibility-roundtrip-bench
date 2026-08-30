"""Conservative, non-text structural inspection for PDF files."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterable, Optional, Set, Tuple

from pypdf import PdfReader
from pypdf.generic import ArrayObject, DictionaryObject, IndirectObject

from .models import StructuralSnapshot


MAX_OBJECTS = 200_000


def _resolve(value: Any) -> Any:
    if isinstance(value, IndirectObject):
        return value.get_object()
    return value


def _count_alt_values(value: Any, seen: Set[Tuple[int, int]], budget: list[int]) -> int:
    if budget[0] <= 0:
        return 0
    budget[0] -= 1
    if isinstance(value, IndirectObject):
        key = (value.idnum, value.generation)
        if key in seen:
            return 0
        seen.add(key)
        try:
            value = value.get_object()
        except Exception:
            return 0
    if isinstance(value, DictionaryObject):
        total = 1 if value.get("/Alt") is not None else 0
        for child in value.values():
            total += _count_alt_values(child, seen, budget)
        return total
    if isinstance(value, ArrayObject):
        return sum(_count_alt_values(child, seen, budget) for child in value)
    return 0


def _count_outlines(value: Any) -> int:
    if isinstance(value, list):
        return sum(_count_outlines(item) for item in value)
    if isinstance(value, dict):
        return 1 + sum(_count_outlines(item) for item in value.values())
    return 0


def inspect_structure(path: Path) -> StructuralSnapshot:
    try:
        reader = PdfReader(str(path), strict=False)
        root = _resolve(reader.trailer.get("/Root"))
        if not isinstance(root, DictionaryObject):
            raise ValueError("missing catalog")

        struct_tree = _resolve(root.get("/StructTreeRoot"))
        mark_info = _resolve(root.get("/MarkInfo"))
        role_map = _resolve(struct_tree.get("/RoleMap")) if isinstance(struct_tree, DictionaryObject) else None
        if not isinstance(role_map, DictionaryObject):
            role_map_count = 0
        else:
            role_map_count = len(role_map)

        alt_count = 0
        if struct_tree is not None:
            alt_count = _count_alt_values(struct_tree, set(), [MAX_OBJECTS])

        try:
            outlines = reader.outline
            outline_count = _count_outlines(outlines)
        except Exception:
            outline_count = 0

        info = reader.metadata
        title_present = bool(info and (info.title or info.get("/Title")))
        language_present = root.get("/Lang") is not None
        marked = isinstance(mark_info, DictionaryObject) and bool(mark_info.get("/Marked"))
        return StructuralSnapshot(
            page_count=len(reader.pages),
            struct_tree_present=isinstance(struct_tree, DictionaryObject),
            marked_pdf=marked,
            alt_text_count=alt_count,
            role_map_count=role_map_count,
            document_language_present=language_present,
            title_present=title_present,
            outline_count=outline_count,
        )
    except Exception:
        return StructuralSnapshot(
            page_count=0,
            struct_tree_present=False,
            marked_pdf=False,
            alt_text_count=0,
            role_map_count=0,
            document_language_present=False,
            title_present=False,
            outline_count=0,
            readable=False,
            error="The PDF structure could not be inspected.",
        )


def compare_structure(
    before: StructuralSnapshot, after: Iterable[StructuralSnapshot]
) -> bool:
    """Return whether an observable structure signal changed."""

    after_items = list(after)
    if not before.readable or not after_items or any(not item.readable for item in after_items):
        return False
    after_page_count = sum(item.page_count for item in after_items)
    after_alt_count = sum(item.alt_text_count for item in after_items)
    after_role_maps = sum(item.role_map_count for item in after_items)
    after_tagged = all(item.struct_tree_present for item in after_items)
    after_marked = all(item.marked_pdf for item in after_items)
    after_language = all(item.document_language_present for item in after_items)
    after_title = all(item.title_present for item in after_items)
    after_outlines = sum(item.outline_count for item in after_items)
    return any(
        (
            before.page_count != after_page_count,
            before.alt_text_count != after_alt_count,
            before.role_map_count != after_role_maps,
            before.struct_tree_present != after_tagged,
            before.marked_pdf != after_marked,
            before.document_language_present != after_language,
            before.title_present != after_title,
            before.outline_count != after_outlines,
        )
    )
