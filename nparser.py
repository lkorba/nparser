#!/usr/bin/env python
# nparser.py out.xml

import sys
from libnmap.parser import NmapParser

nmap_report = NmapParser.parse_fromfile(sys.argv[1])

hostport = []

for host in nmap_report.hosts:
    for service in host.services:
        if service.state != "open|filtered":
            hostport.append(str(host.hostnames[0]) + "," + str(service.port))

for item in hostport:
    print(item)
