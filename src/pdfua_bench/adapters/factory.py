"""Build adapters from the isolated toolchain."""

from __future__ import annotations

from typing import Dict, Iterable

from ..models import TOOLS
from ..toolchain import Toolchain
from .base import AdapterError, ToolAdapter
from .ghostscript_adapter import GhostscriptAdapter
from .pymupdf_adapter import PymupdfAdapter
from .qpdf_adapter import QpdfAdapter


def build_adapters(toolchain: Toolchain) -> Dict[str, ToolAdapter]:
    return {
        "qpdf": QpdfAdapter(toolchain),
        "pymupdf": PymupdfAdapter(toolchain),
        "ghostscript": GhostscriptAdapter(toolchain),
    }
