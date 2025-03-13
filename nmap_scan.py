# '''
# NMAP Scanner

# REQUIREMENTS:
# a)	Target IP: localhost and scanme.nmap.org
# b)	Ports: Top 10 ports
# c)	Protocols: TCP and UDP
# d)	Enable OS and version detection, script scanning, and traceroute


import nmap
from tabulate import tabulate
from datetime import datetime

def scan_and_table():
    nmScan = nmap.PortScanner()
    IP = 'localhost scanme.nmap.org'

    print(f"\nType of nmScan: {type(nmScan)}")
    print(f"Scanning Ports:{IP}")

    options = '--top-ports 10 -sTUV -O -sC --traceroute'
    start_time = datetime.now()
    print(f"Scan started at: {start_time}")

    results = nmScan.scan(hosts=IP, arguments=options)

    end_time = datetime.now()
    print(f"Scan completed at: {end_time}")
    print(f"Scan duration: {end_time - start_time}")

    print(f"Type of Results: {type(results)}")

    table = []

    for host in nmScan.all_hosts():
        for proto in nmScan[host].all_protocols():
            for port in nmScan[host][proto].keys():
                table.append([
                    host, nmScan[host].hostname(), proto, port,
                    nmScan[host][proto][port]["state"],
                    nmScan[host][proto][port]["product"],
                    nmScan[host][proto][port]["extrainfo"],
                    nmScan[host][proto][port]["reason"],
                    nmScan[host][proto][port]["cpe"]
                ])

    print(tabulate(table, headers=["Host", "Hostname", "Protocol", "Port", "State", "Product", "Extra Info", "Reason", "CPE"], tablefmt="mixed_grid"))
    print("\n")

scan_and_table()