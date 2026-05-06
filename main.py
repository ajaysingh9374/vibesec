"""VibeSec command-line entry point.

This first version only proves the scanner workflow:
- simulate by reusing an existing Nmap XML file from samples/
- run a local Nmap scan against localhost and save XML output
- parse open port details from the available Nmap XML file
- print simple summaries from the parsed data

AI logic and report generation are planned later.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from scanner.nmap_runner import NmapRunnerError, run_local_scan, use_sample_scan
from scanner.xml_parser import (
    NmapXmlParserError,
    parse_nmap_xml,
    print_open_ports_table,
)


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
    print("Current workflow step:")
    print("1. XML available")
    print("2. parse open port details")
    print("3. summarise parsed data")
    print()
    print("Next planned steps:")
    print("1. report")


def parse_and_print_xml(xml_file: Path) -> list[dict[str, str]]:
    """Parse the available Nmap XML file and print extracted open ports."""
    records = parse_nmap_xml(xml_file)
    print_open_ports_table(records)
    return records


def print_analysis_summary(records: list[dict[str, str]]) -> None:
    """Print simple counts and groupings from parsed Nmap records."""
    hosts = sorted({record["host_ip"] for record in records})
    open_ports_by_host: dict[str, list[str]] = {}
    services_by_name: dict[str, list[str]] = {}

    # Group extracted facts only; this does not score or interpret services.
    for record in records:
        host_ip = record["host_ip"]
        service_name = record["service_name"]
        service_entry = (
            f"{record['host_ip']}:{record['port']}/"
            f"{record['protocol']} ({record['service_version']})"
        )

        open_ports_by_host.setdefault(host_ip, []).append(record["port"])
        services_by_name.setdefault(service_name, []).append(service_entry)

    print()
    print("Analysis Summary")
    print("================")
    print(f"Total hosts with open ports : {len(hosts)}")
    print(f"Total open ports            : {len(records)}")
    print()
    print("Open ports per host")
    print("-------------------")

    if not open_ports_by_host:
        print("No open ports to summarise.")
    else:
        for host_ip, ports in open_ports_by_host.items():
            print(f"{host_ip}: {len(ports)} open port(s) - {', '.join(ports)}")

    print()
    print("Services discovered")
    print("-------------------")

    if not services_by_name:
        print("No services discovered.")
    else:
        for service_name, service_entries in services_by_name.items():
            print(f"{service_name}:")
            for service_entry in service_entries:
                print(f"  - {service_entry}")


def main() -> int:
    """Run the requested VibeSec mode and return a process exit code."""
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.simulate:
            xml_file = use_sample_scan()
            print_summary("simulate", str(xml_file))
            records = parse_and_print_xml(xml_file)
            print_analysis_summary(records)
            return 0

        if args.local:
            xml_file = run_local_scan()
            print_summary("local", str(xml_file))
            records = parse_and_print_xml(xml_file)
            print_analysis_summary(records)
            return 0

    except (NmapRunnerError, NmapXmlParserError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    # This should not be reached because argparse requires exactly one mode.
    parser.error("Choose either --simulate or --local.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
