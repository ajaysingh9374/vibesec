"""Nmap workflow helpers for VibeSec.

This module intentionally stops at producing or selecting Nmap XML.
Future modules will parse, analyse, and report from that XML.
"""

from __future__ import annotations

import subprocess
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLES_DIR = PROJECT_ROOT / "samples"
REPORTS_DIR = PROJECT_ROOT / "reports"
DEFAULT_SAMPLE_XML = SAMPLES_DIR / "localhost_sample.xml"
LOCAL_SCAN_XML = REPORTS_DIR / "localhost_nmap.xml"


class NmapRunnerError(RuntimeError):
    """Raised when the Nmap workflow cannot complete."""


def use_sample_scan(sample_file: Path = DEFAULT_SAMPLE_XML) -> Path:
    """Return an existing sample XML file for simulation mode."""
    if not sample_file.exists():
        raise NmapRunnerError(
            f"Sample XML file was not found: {sample_file}. "
            "Add an Nmap XML file under samples/ or restore the default sample."
        )

    return sample_file


def run_local_scan(output_file: Path = LOCAL_SCAN_XML) -> Path:
    """Run nmap.exe against localhost and write XML output with -oX."""
    output_file.parent.mkdir(parents=True, exist_ok=True)

    command = [
        "nmap.exe",
        "-oX",
        str(output_file),
        "localhost",
    ]

    try:
        result = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError as error:
        raise NmapRunnerError(
            "nmap.exe was not found. Confirm Nmap for Windows is installed "
            "and available on your PATH."
        ) from error

    if result.returncode != 0:
        details = (result.stderr or result.stdout).strip()
        message = "Nmap scan failed."
        if details:
            message = f"{message} Nmap output: {details}"
        raise NmapRunnerError(message)

    if not output_file.exists():
        raise NmapRunnerError(f"Nmap completed, but no XML file was created: {output_file}")

    return output_file
