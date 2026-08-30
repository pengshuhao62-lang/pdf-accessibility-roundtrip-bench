"""PyMuPDF transformation adapter."""

from __future__ import annotations

from pathlib import Path
from typing import List

import pymupdf

from .base import AdapterError, require_output, require_paths_inside
from ..toolchain import Toolchain


class PymupdfAdapter:
    name = "pymupdf"

    def __init__(self, toolchain: Toolchain) -> None:
        self.toolchain = toolchain

    def version(self) -> str:
        version = getattr(pymupdf, "VersionBind", None)
        if version:
            return str(version)
        versions = getattr(pymupdf, "version", None)
        if isinstance(versions, dict):
            return str(versions.get("version", "unknown"))
        return "PyMuPDF (unknown version)"

    def merge(self, inputs: List[Path], output: Path, workdir: Path) -> List[Path]:
        if len(inputs) != 2:
            raise AdapterError("PyMuPDF merge requires exactly two input PDFs.")
        target = pymupdf.open()
        try:
            for input_path in inputs:
                source = pymupdf.open(str(input_path))
                try:
                    target.insert_pdf(source)
                finally:
                    source.close()
            target.save(str(output))
        except Exception as exc:
            raise AdapterError("PyMuPDF could not merge the PDFs.") from exc
        finally:
            target.close()
        require_output(output, self.name)
        require_paths_inside([output], workdir)
        return [output]

    def split(self, input_path: Path, output_dir: Path, workdir: Path) -> List[Path]:
        output_dir.mkdir(parents=True, exist_ok=True)
        source = pymupdf.open(str(input_path))
        outputs: List[Path] = []
        try:
            for page_number in range(source.page_count):
                target = pymupdf.open()
                try:
                    target.insert_pdf(source, from_page=page_number, to_page=page_number)
                    output = output_dir / f"split-{page_number + 1:03d}.pdf"
                    target.save(str(output))
                    outputs.append(output)
                finally:
                    target.close()
        except Exception as exc:
            raise AdapterError("PyMuPDF could not split the PDF.") from exc
        finally:
            source.close()
        if not outputs:
            raise AdapterError("PyMuPDF did not produce split PDF files.")
        for output in outputs:
            require_output(output, self.name)
        require_paths_inside(outputs, workdir)
        return outputs

    def resave(self, input_path: Path, output: Path, workdir: Path) -> List[Path]:
        document = pymupdf.open(str(input_path))
        try:
            document.save(str(output))
        except Exception as exc:
            raise AdapterError("PyMuPDF could not resave the PDF.") from exc
        finally:
            document.close()
        require_output(output, self.name)
        require_paths_inside([output], workdir)
        return [output]
