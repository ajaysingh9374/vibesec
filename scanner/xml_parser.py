"""Parse Nmap XML output into simple structured port data.

This module only reads and extracts scan evidence. It does not interpret,
score, or analyse the services found in the XML file.
"""

from __future__ import annotations

from pathlib import Path
from xml.etree import ElementTree


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_NMAP_XML = PROJECT_ROOT / "reports" / "localhost_nmap.xml"


class NmapXmlParserError(RuntimeError):
    """Raised when an Nmap XML file cannot be read or parsed."""


def parse_nmap_xml(xml_file: Path = DEFAULT_NMAP_XML) -> list[dict[str, str]]:
    """Read an Nmap XML file and return open port records."""
    if not xml_file.exists():
        raise NmapXmlParserError(f"Nmap XML file was not found: {xml_file}")

    try:
        tree = ElementTree.parse(xml_file)
    except ElementTree.ParseError as error:
        raise NmapXmlParserError(f"Invalid Nmap XML file: {xml_file}") from error

    root = tree.getroot()
    records: list[dict[str, str]] = []

    # Each host can contain one or more addresses, hostnames, and ports.
    for host in root.findall("host"):
        host_ip = _get_host_ip(host)
        hostname = _get_hostname(host)

        for port in host.findall("./ports/port"):
            state = port.find("state")
            if state is None or state.get("state") != "open":
                continue

            service = port.find("service")
            records.append(
                {
                    "host_ip": host_ip,
                    "hostname": hostname,
                    "port": port.get("portid", "unknown"),
                    "protocol": port.get("protocol", "unknown"),
                    "service_name": _get_service_name(service),
                    "service_version": _get_service_version(service),
                }
            )

    return records


def print_open_ports_table(records: list[dict[str, str]]) -> None:
    """Print extracted open port records in a simple text table."""
    print()
    print("Extracted Nmap open ports")
    print("=========================")

    if not records:
        print("No open ports found in the XML file.")
        return

    headers = ["Host IP", "Hostname", "Port", "Protocol", "Service", "Version"]
    rows = [
        [
            record["host_ip"],
            record["hostname"],
            record["port"],
            record["protocol"],
            record["service_name"],
            record["service_version"],
        ]
        for record in records
    ]

    widths = [
        max(len(str(row[index])) for row in [headers, *rows])
        for index in range(len(headers))
    ]

    print(_format_row(headers, widths))
    print(_format_row(["-" * width for width in widths], widths))

    for row in rows:
        print(_format_row(row, widths))


def _get_host_ip(host: ElementTree.Element) -> str:
    """Return the first IP address recorded for a host."""
    for address in host.findall("address"):
        if address.get("addrtype") in {"ipv4", "ipv6"}:
            return address.get("addr", "unknown")
    return "unknown"


def _get_hostname(host: ElementTree.Element) -> str:
    """Return the first hostname recorded for a host, if available."""
    hostname = host.find("./hostnames/hostname")
    if hostname is None:
        return "unknown"
    return hostname.get("name", "unknown")


def _get_service_name(service: ElementTree.Element | None) -> str:
    """Return the service name from a port record, if available."""
    if service is None:
        return "unknown"
    return service.get("name", "unknown")


def _get_service_version(service: ElementTree.Element | None) -> str:
    """Return available service version details from a port record."""
    if service is None:
        return "unknown"

    version_parts = [
        service.get("product", ""),
        service.get("version", ""),
        service.get("extrainfo", ""),
    ]
    version = " ".join(part for part in version_parts if part).strip()
    return version or "unknown"


def _format_row(values: list[str], widths: list[int]) -> str:
    """Format one table row with padded columns."""
    return " | ".join(value.ljust(width) for value, width in zip(values, widths))
