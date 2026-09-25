---
type: machine
title: Antique
platform: htb
os: linux
difficulty: easy
tags: [printer, snmp, telnet, linux, privesc, cups]
solved: 2026-07-09
sources: [[htb-antique]]
related: []
---
# Antique

> Antique simulates an HP printer with exposed SNMP and Telnet services, requiring password extraction via SNMP, then leveraging CUPS vulnerabilities for root access through multiple CVEs.

## Attack path

1. [[snmp-password-leak]] — Extract printer password via SNMP OID
2. [[telnet-execution]] — Access HP JetDirect interface and execute commands
3. [[cups-cve-2012-5519]] — Exploit CUPS file read vulnerability for root flag
4. [[pwnkit-cve-2021-4034]] — Alternative privesc via PolicyKit vulnerability

## Techniques used

- [[snmp-password-leak]] — Reading HP JetDirect admin password via specific SNMP OID
- [[telnet-execution]] — Using HP JetDirect exec command to run system commands
- [[cups-cve-2012-5519]] — CUPS 1.6.1 file read as root via ErrorLog configuration
- [[pwnkit-cve-2021-4034]] — PolicyKit pkexec local privilege escalation vulnerability

## Tools used

- [[nmap]] — TCP and UDP port scanning
- telnet — HP JetDirect interface access
- snmpwalk — SNMP enumeration and password extraction
- Python — ASCII conversion and hash decoding
- chisel — Port forwarding for CUPS access
- cupsctl — CUPS configuration manipulation
- curl — CUPS web interface interaction
- hashcat — Password cracking (unsuccessful in this case)

## Services / ports

- 23/tcp — telnet — HP JetDirect printer interface
- 161/udp — snmp — SNMPv1 public community string
- 631/tcp — ipp — CUPS 1.6.1

## Lessons / notes

- Printers often run vulnerable services with default credentials
- SNMP can leak sensitive configuration data including passwords
- UDP scanning is slower but can reveal services not visible on TCP
- CUPS older versions have file read vulnerabilities via configuration manipulation
- Multiple CVEs may apply to the same service (CUPS had both file read and RCE vulnerabilities)
- PwnKit affects many Linux distributions and is worth checking even on older systems
