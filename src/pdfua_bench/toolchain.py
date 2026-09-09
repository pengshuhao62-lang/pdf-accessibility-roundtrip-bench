"""Resolve the isolated PDF benchmark toolchain without changing the system."""

from __future__ import annotations

import os
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional


TOOLCHAIN_DIRECTORY_NAME = "pdf-accessibility-roundtrip-bench"


@dataclass(frozen=True)
class Toolchain:
    root: Path
    vera_pdf: Optional[Path]
    qpdf: Optional[Path]
    ghostscript: Optional[Path]
    java_home: Optional[Path]

    @property
    def environment(self) -> Dict[str, str]:
        environment = os.environ.copy()
        if self.java_home:
            environment["JAVA_HOME"] = str(self.java_home)
            java_bin = self.java_home / "bin"
            existing_path = environment.get("PATH", "")
            environment["PATH"] = f"{java_bin}:{existing_path}" if existing_path else str(java_bin)
        return environment

    def executable_paths(self) -> Dict[str, Optional[str]]:
        return {
            "verapdf": str(self.vera_pdf) if self.vera_pdf else None,
            "qpdf": str(self.qpdf) if self.qpdf else None,
            "ghostscript": str(self.ghostscript) if self.ghostscript else None,
            "java": str(self.java_home / "bin" / "java") if self.java_home else None,
        }


def _executable(value: Optional[str], fallback: Path, name: str) -> Optional[Path]:
    if value:
        path = Path(value).expanduser()
        return path if path.is_file() and os.access(path, os.X_OK) else None
    if fallback.is_file() and os.access(fallback, os.X_OK):
        return fallback
    discovered = shutil.which(name)
    return Path(discovered) if discovered else None


def _discover_default_root() -> Path:
    """Find a sibling external-SSD tool directory without embedding local paths."""

    candidates = [
        Path.cwd() / ".tools" / TOOLCHAIN_DIRECTORY_NAME,
        Path.cwd().parent / ".tools" / TOOLCHAIN_DIRECTORY_NAME,
    ]
    for candidate in candidates:
        if candidate.is_dir():
            return candidate
    return Path.cwd() / ".pdfua-bench-tools"


def resolve_toolchain(root: Optional[Path] = None) -> Toolchain:
    configured_root = os.environ.get("PDFUA_BENCH_TOOL_ROOT")
    tool_root = Path(configured_root).expanduser() if configured_root else (root or _discover_default_root())
    environment_root = tool_root / "env"
    java_home = Path(os.environ["JAVA_HOME"]) if os.environ.get("JAVA_HOME") else environment_root / "lib" / "jvm"
    if not (java_home / "bin/java").is_file():
        java_home = None
    return Toolchain(
        root=tool_root if tool_root.is_dir() else Path.cwd(),
        vera_pdf=_executable(
            os.environ.get("PDFUA_BENCH_VERAPDF"),
            tool_root / "verapdf" / "verapdf",
            "verapdf",
        ),
        qpdf=_executable(
            os.environ.get("PDFUA_BENCH_QPDF"),
            environment_root / "bin" / "qpdf",
            "qpdf",
        ),
        ghostscript=_executable(
            os.environ.get("PDFUA_BENCH_GHOSTSCRIPT"),
            environment_root / "bin" / "gs",
            "gs",
        ),
        java_home=java_home,
    )
