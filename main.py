"""VibeSec command-line entry point.

This first version only proves the scanner workflow:
- simulate by reusing an existing Nmap XML file from samples/
- run a local Nmap scan against localhost and save XML output

Parsing, analysis, AI logic, and report generation are planned later.
"""

from __future__ import annotations

import argparse
import sys

from scanner.nmap_runner import NmapRunnerError, run_local_scan, use_sample_scan


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line interface for the first VibeSec workflow."""
    parser = argparse.ArgumentParser(
        description="Run the first VibeSec Nmap XML workflow."
    )

    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--simulate",
        action="store_true",
        help="Use an existing Nmap XML sample from the samples folder.",
    )
    mode.add_argument(
        "--local",
        action="store_true",
        help="Run nmap.exe against localhost and save XML output.",
    )

    return parser


def print_summary(mode: str, xml_file: str) -> None:
    """Print a clear summary for the current workflow stage."""
    print("VibeSec workflow summary")
    print("========================")
    print(f"Running Mode : {mode}")
    print(f"XML File     : {xml_file}")
    print()
    print("Next planned steps:")
    print("1. parse")
    print("2. analyse")
    print("3. report")


def main() -> int:
    """Run the requested VibeSec mode and return a process exit code."""
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.simulate:
            xml_file = use_sample_scan()
            print_summary("simulate", str(xml_file))
            return 0

        if args.local:
            xml_file = run_local_scan()
            print_summary("local", str(xml_file))
            return 0

    except NmapRunnerError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    # This should not be reached because argparse requires exactly one mode.
    parser.error("Choose either --simulate or --local.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
