"""Bounded external-process execution with no shell interpolation."""

from __future__ import annotations

import os
import signal
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional, Sequence


@dataclass(frozen=True)
class ProcessResult:
    returncode: Optional[int]
    stdout: str
    stderr: str
    timed_out: bool = False


def run_command(
    args: Sequence[str],
    cwd: Path,
    environment: Optional[Dict[str, str]] = None,
    timeout_seconds: int = 120,
) -> ProcessResult:
    """Run one known executable in its own process group."""

    process = subprocess.Popen(
        list(args),
        cwd=str(cwd),
        env=environment,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        start_new_session=True,
        shell=False,
    )
    try:
        stdout, stderr = process.communicate(timeout=timeout_seconds)
        return ProcessResult(process.returncode, stdout, stderr)
    except subprocess.TimeoutExpired:
        try:
            os.killpg(process.pid, signal.SIGTERM)
            stdout, stderr = process.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            stdout, stderr = process.communicate()
        return ProcessResult(process.returncode, stdout, stderr, timed_out=True)
