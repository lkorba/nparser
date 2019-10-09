#!/usr/bin/env python
import sys
from pathlib import Path

from libnmap.parser import NmapParser

FILTERED = "open|filtered"


def main(log):
    logfile = Path(log)
    if logfile.exists():
        results = parse(log)
        while True:
            try:
                print(next(results))
            except StopIteration:
                break
    else:
        print(f"Can't file {log} to parse...")


def parse(log):
    report = NmapParser.parse_fromfile(sys.argv[1])

    yield from [
        f"{host.ipv4},{service.port}"
        for host in report.hosts
        for service in host.services
        if service.state != FILTERED
    ]


def usage():
    filename = __file__.split("/")[-1]
    print(f"usage: {filename} FILENAME")
    print(f"\n  example: {filename} out.xml")
    exit()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()

    main(sys.argv[1])
