#!/usr/bin/env python3
"""Generate small deterministic tagged-PDF fixtures for the benchmark."""

from __future__ import annotations

import argparse
import tempfile
from pathlib import Path
from typing import Iterable, List

from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    ArrayObject,
    BooleanObject,
    DecodedStreamObject,
    DictionaryObject,
    NameObject,
    NumberObject,
    TextStringObject,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import reportlab


FONT_NAME = "RepoPortVera"


def _register_font() -> None:
    font_path = Path(reportlab.__file__).resolve().parent / "fonts/Vera.ttf"
    if font_path.is_file() and FONT_NAME not in pdfmetrics.getRegisteredFontNames():
        pdfmetrics.registerFont(TTFont(FONT_NAME, str(font_path)))


def _draw_source_pdf(path: Path, title: str, lines: Iterable[str], pages: int) -> None:
    document = canvas.Canvas(str(path), pagesize=(595.276, 841.89))
    document.setTitle(title)
    document.setAuthor("RepoPort fixture generator")
    document.setCreator("pdfua-bench fixture generator")
    line_items = list(lines)
    for page_index in range(pages):
        text = document.beginText(72, 760)
        text.setFont(FONT_NAME, 18)
        text.textLine(title)
        text.setFont(FONT_NAME, 11)
        text.textLine(f"Fixture page {page_index + 1} of {pages}.")
        for line in line_items:
            text.textLine(line)
        document.drawText(text)
        document.showPage()
    document.save()


def _xmp(title: str, profile: str) -> bytes:
    part = "1" if profile == "ua1" else "2"
    revision = "" if profile == "ua1" else "\n          <pdfuaid:rev>2024</pdfuaid:rev>"
    return f'''<?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description rdf:about="" xmlns:pdfuaid="http://www.aiim.org/pdfua/ns/id/">
      <pdfuaid:part>{part}</pdfuaid:part>{revision}
    </rdf:Description>
    <rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/">
      <dc:title><rdf:Alt><rdf:li xml:lang="x-default">{title}</rdf:li></rdf:Alt></dc:title>
    </rdf:Description>
  </rdf:RDF>
</x:xmpmeta>
<?xpacket end="r"?>'''.encode("utf-8")


def _stream(data: bytes) -> DecodedStreamObject:
    stream = DecodedStreamObject()
    stream.set_data(data)
    return stream


def _make_tagged_pdf(source_path: Path, output_path: Path, title: str, profile: str) -> None:
    reader = PdfReader(str(source_path), strict=False)
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    root = writer._root_object
    if profile == "ua2":
        writer.pdf_header = "%PDF-2.0"
        root[NameObject("/Version")] = NameObject("/2.0")
    root[NameObject("/Lang")] = TextStringObject("en-US")
    root[NameObject("/MarkInfo")] = DictionaryObject(
        {
            NameObject("/Marked"): BooleanObject(True),
            NameObject("/Suspects"): BooleanObject(False),
        }
    )
    root[NameObject("/ViewerPreferences")] = DictionaryObject(
        {NameObject("/DisplayDocTitle"): BooleanObject(True)}
    )
    writer.add_metadata(
        {
            "/Title": title,
            "/Author": "RepoPort fixture generator",
            "/Creator": "pdfua-bench fixture generator",
            "/Producer": "pdfua-bench fixture generator",
        }
    )
    metadata = _stream(_xmp(title, profile))
    metadata.update(
        {
            NameObject("/Type"): NameObject("/Metadata"),
            NameObject("/Subtype"): NameObject("/XML"),
        }
    )
    root[NameObject("/Metadata")] = writer._add_object(metadata)

    struct_root = DictionaryObject(
        {
            NameObject("/Type"): NameObject("/StructTreeRoot"),
            NameObject("/ParentTreeNextKey"): NumberObject(len(writer.pages)),
        }
    )
    struct_root_ref = writer._add_object(struct_root)
    namespace_ref = None
    if profile == "ua2":
        namespace = DictionaryObject(
            {
                NameObject("/Type"): NameObject("/Namespace"),
                NameObject("/NS"): TextStringObject("http://iso.org/pdf2/ssn"),
            }
        )
        namespace_ref = writer._add_object(namespace)
        struct_root[NameObject("/Namespaces")] = ArrayObject([namespace_ref])
    document_element = DictionaryObject(
        {
            NameObject("/Type"): NameObject("/StructElem"),
            NameObject("/S"): NameObject("/Document"),
            NameObject("/P"): struct_root_ref,
            NameObject("/T"): TextStringObject(title),
        }
    )
    if namespace_ref is not None:
        document_element[NameObject("/NS")] = namespace_ref
    document_ref = writer._add_object(document_element)
    structure_children = ArrayObject()
    parent_numbers = ArrayObject()

    for page_index, page in enumerate(writer.pages):
        content = page[NameObject("/Contents")].get_object().get_data()
        marked_content = b"/P <</MCID 0>> BDC\n" + content + b"\nEMC\n"
        page[NameObject("/Contents")] = writer._add_object(_stream(marked_content))
        page[NameObject("/StructParents")] = NumberObject(page_index)
        page[NameObject("/Tabs")] = NameObject("/S")

        paragraph = DictionaryObject(
            {
                NameObject("/Type"): NameObject("/StructElem"),
                NameObject("/S"): NameObject("/P"),
                NameObject("/P"): document_ref,
                NameObject("/K"): NumberObject(0),
            }
        )
        if namespace_ref is not None:
            paragraph[NameObject("/NS")] = namespace_ref
        paragraph_ref = writer._add_object(paragraph)
        structure_children.append(paragraph_ref)
        parent_numbers.extend([NumberObject(page_index), ArrayObject([paragraph_ref])])

    document_element[NameObject("/K")] = structure_children
    struct_root[NameObject("/K")] = document_ref
    parent_tree = DictionaryObject(
        {
            NameObject("/Nums"): parent_numbers,
        }
    )
    struct_root[NameObject("/ParentTree")] = writer._add_object(parent_tree)
    root[NameObject("/StructTreeRoot")] = struct_root_ref
    if profile == "ua1":
        try:
            writer.add_outline_item(title, 0)
        except Exception:
            pass
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("wb") as stream:
        writer.write(stream)


def generate(output_root: Path) -> List[Path]:
    _register_font()
    fixtures = [
        ("ua1-paragraph-001", "ua1", "Accessible Paragraph", ["A short paragraph fixture."], 1),
        ("ua1-heading-001", "ua1", "Accessible Heading", ["Heading and paragraph structure."], 1),
        ("ua1-list-001", "ua1", "Accessible List", ["First item.", "Second item.", "Third item."], 1),
        ("ua1-table-001", "ua1", "Accessible Table", ["Name | Value", "Alpha | 1", "Beta | 2"], 2),
        ("ua1-unicode-001", "ua1", "Unicode Fixture", ["Café, naïve, résumé, and symbols: © ± €."], 1),
        ("ua1-link-001", "ua1", "Accessible Link", ["A document with a link target."], 1),
        ("ua2-paragraph-001", "ua2", "PDF 2 Accessible Paragraph", ["A PDF 2.0 paragraph fixture."], 1),
        ("ua2-heading-001", "ua2", "PDF 2 Accessible Heading", ["A PDF 2.0 heading fixture."], 1),
        ("ua2-table-001", "ua2", "PDF 2 Accessible Table", ["Column A | Column B", "One | Two"], 2),
        ("ua2-unicode-001", "ua2", "PDF 2 Unicode Fixture", ["Unicode: café, ångström, and ©."], 1),
        ("ua2-link-001", "ua2", "PDF 2 Accessible Link", ["A PDF 2.0 link fixture."], 1),
    ]
    generated: List[Path] = []
    with tempfile.TemporaryDirectory(prefix="pdfua-fixture-generation-") as directory:
        working = Path(directory)
        for fixture_id, profile, title, lines, pages in fixtures:
            source = working / f"{fixture_id}-source.pdf"
            output = output_root / profile / f"{fixture_id}.pdf"
            _draw_source_pdf(source, title, lines, pages)
            _make_tagged_pdf(source, output, title, profile)
            generated.append(output)
    return generated


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "corpus",
    )
    args = parser.parse_args()
    for path in generate(args.output_root):
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
