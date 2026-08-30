"""qpdf command-line adapter."""

from __future__ import annotations

from pathlib import Path
from typing import List, Optional

from ..process import run_command
from ..toolchain import Toolchain
from .base import AdapterError, require_completed, require_output, require_paths_inside


class QpdfAdapter:
    name = "qpdf"

    def __init__(self, toolchain: Toolchain, timeout_seconds: int = 120) -> None:
        self.toolchain = toolchain
        self.timeout_seconds = timeout_seconds
        self._version: Optional[str] = None

    def version(self) -> str:
        if self._version:
            return self._version
        if not self.toolchain.qpdf:
            raise AdapterError("qpdf is not available.")
        result = run_command(
            [str(self.toolchain.qpdf), "--version"],
            cwd=self.toolchain.root,
            environment=self.toolchain.environment,
            timeout_seconds=30,
        )
        require_completed(result, self.name)
        self._version = next(
            (line.strip() for line in result.stdout.splitlines() if line.strip()),
            "qpdf (unknown version)",
        )
        return self._version

    def _run(self, args: List[str], workdir: Path) -> None:
        if not self.toolchain.qpdf:
            raise AdapterError("qpdf is not available.")
        result = run_command(
            [str(self.toolchain.qpdf), *args],
            cwd=workdir,
            environment=self.toolchain.environment,
            timeout_seconds=self.timeout_seconds,
        )
        require_completed(result, self.name)

    def merge(self, inputs: List[Path], output: Path, workdir: Path) -> List[Path]:
        if len(inputs) != 2:
            raise AdapterError("qpdf merge requires exactly two input PDFs.")
        self._run(
            [
                "--empty",
                "--pages",
                str(inputs[0]),
                str(inputs[1]),
                "--",
                str(output),
            ],
            workdir,
        )
        require_output(output, self.name)
        require_paths_inside([output], workdir)
        return [output]

    def split(self, input_path: Path, output_dir: Path, workdir: Path) -> List[Path]:
        output_dir.mkdir(parents=True, exist_ok=True)
        prefix = output_dir / "split-%d.pdf"
        self._run(["--split-pages", str(input_path), str(prefix)], workdir)
        outputs = sorted(output_dir.glob("split-*.pdf"))
        if not outputs:
            raise AdapterError("qpdf did not produce split PDF files.")
        for output in outputs:
            require_output(output, self.name)
        require_paths_inside(outputs, workdir)
        return outputs

    def resave(self, input_path: Path, output: Path, workdir: Path) -> List[Path]:
        self._run([str(input_path), str(output)], workdir)
        require_output(output, self.name)
        require_paths_inside([output], workdir)
        return [output]
