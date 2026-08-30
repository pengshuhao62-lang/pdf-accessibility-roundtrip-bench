"""Common adapter protocol and process result helpers."""

from __future__ import annotations

from pathlib import Path
from typing import List, Protocol

from ..process import ProcessResult
from ..toolchain import Toolchain


class AdapterError(RuntimeError):
    """A transformation could not be completed by a tool adapter."""


class ToolAdapter(Protocol):
    name: str

    def version(self) -> str:
        ...

    def merge(self, inputs: List[Path], output: Path, workdir: Path) -> List[Path]:
        ...

    def split(self, input_path: Path, output_dir: Path, workdir: Path) -> List[Path]:
        ...

    def resave(self, input_path: Path, output: Path, workdir: Path) -> List[Path]:
        ...


def require_completed(result: ProcessResult, tool_name: str) -> None:
    if result.timed_out:
        raise AdapterError(f"{tool_name} timed out.")
    if result.returncode != 0:
        raise AdapterError(f"{tool_name} exited with a non-zero status.")


def require_output(path: Path, tool_name: str) -> None:
    if not path.is_file() or path.stat().st_size == 0:
        raise AdapterError(f"{tool_name} did not produce the expected output.")


def require_paths_inside(paths: List[Path], directory: Path) -> None:
    root = directory.resolve()
    for path in paths:
        try:
            path.resolve().relative_to(root)
        except ValueError as exc:
            raise AdapterError("A transformation output escaped its work directory.") from exc
