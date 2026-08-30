"""Ghostscript pdfwrite adapter."""

from __future__ import annotations

from pathlib import Path
from typing import List, Optional

from pypdf import PdfReader

from ..process import run_command
from ..toolchain import Toolchain
from .base import AdapterError, require_completed, require_output, require_paths_inside


class GhostscriptAdapter:
    name = "ghostscript"

    def __init__(self, toolchain: Toolchain, timeout_seconds: int = 180) -> None:
        self.toolchain = toolchain
        self.timeout_seconds = timeout_seconds
        self._version: Optional[str] = None

    def version(self) -> str:
        if self._version:
            return self._version
        if not self.toolchain.ghostscript:
            raise AdapterError("Ghostscript is not available.")
        result = run_command(
            [str(self.toolchain.ghostscript), "--version"],
            cwd=self.toolchain.root,
            environment=self.toolchain.environment,
            timeout_seconds=30,
        )
        require_completed(result, self.name)
        self._version = next(
            (line.strip() for line in result.stdout.splitlines() if line.strip()),
            "Ghostscript (unknown version)",
        )
        return self._version

    def _run(self, inputs: List[Path], output: Path, workdir: Path, extra: Optional[List[str]] = None) -> None:
        if not self.toolchain.ghostscript:
            raise AdapterError("Ghostscript is not available.")
        args = [
            "-dSAFER",
            "-dBATCH",
            "-dNOPAUSE",
            "-sDEVICE=pdfwrite",
            f"-sOutputFile={output}",
        ]
        if extra:
            args.extend(extra)
        args.extend(str(input_path) for input_path in inputs)
        result = run_command(
            [str(self.toolchain.ghostscript), *args],
            cwd=workdir,
            environment=self.toolchain.environment,
            timeout_seconds=self.timeout_seconds,
        )
        require_completed(result, self.name)
        require_output(output, self.name)

    def merge(self, inputs: List[Path], output: Path, workdir: Path) -> List[Path]:
        if len(inputs) != 2:
            raise AdapterError("Ghostscript merge requires exactly two input PDFs.")
        self._run(inputs, output, workdir)
        require_paths_inside([output], workdir)
        return [output]

    def split(self, input_path: Path, output_dir: Path, workdir: Path) -> List[Path]:
        output_dir.mkdir(parents=True, exist_ok=True)
        try:
            page_count = len(PdfReader(str(input_path), strict=False).pages)
        except Exception as exc:
            raise AdapterError("Ghostscript could not determine the input page count.") from exc
        outputs: List[Path] = []
        for page_number in range(1, page_count + 1):
            output = output_dir / f"split-{page_number:03d}.pdf"
            self._run(
                [input_path],
                output,
                workdir,
                extra=[f"-dFirstPage={page_number}", f"-dLastPage={page_number}"],
            )
            outputs.append(output)
        if not outputs:
            raise AdapterError("Ghostscript did not produce split PDF files.")
        require_paths_inside(outputs, workdir)
        return outputs

    def resave(self, input_path: Path, output: Path, workdir: Path) -> List[Path]:
        self._run([input_path], output, workdir)
        require_paths_inside([output], workdir)
        return [output]
