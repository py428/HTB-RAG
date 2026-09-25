---
type: machine
title: Carrier
platform: htb
os: linux
difficulty: medium
tags: [bgp, network, web, ssh, ftp, command-injection, privesc]
solved: 2026-07-09
sources: [[htb-carrier]]
related: []
---
# Carrier
> Carrier is a medium Linux box focused on network infrastructure exploitation. The box simulates an ISP network with BGP routing, requiring SNMP enumeration for initial access, command injection in a web interface for router foothold, and BGP hijacking to intercept FTP traffic containing credentials for the final compromise.

## Attack path
1. [[snmp-enumeration]] → Serial number for admin login
2. [[web-enumeration]] → [[command-injection]] in diagnostics page
3. Router foothold via command injection
4. [[network-enumeration]] → Identify FTP traffic path
5. [[bgp-hijacking]] → Intercept FTP credentials
6. [[ftp-access]] → Root access on target system

## Techniques used
- [[snmp-enumeration]] — Retrieve device serial number via SNMPv1
- [[command-injection]] — Inject commands via grep parameter in diagnostic tool
- [[network-enumeration]] — Map network topology and identify internal services
- [[bgp-hijacking]] — Manipulate BGP advertisements to intercept network traffic
- [[credential-interception]] — Capture FTP credentials from hijacked traffic

## Tools used
- [[nmap]] — Comprehensive port scanning (TCP and UDP)
- snmpwalk — SNMP enumeration for serial number
- gobuster — Directory brute force on web interface
- [[python]] — Scripted command injection shell
- tcpdump — Traffic capture for credential interception
- [[netcat]] — Reverse shell and FTP impersonation
- vtysh — Quagga BGP configuration and manipulation

## Services / ports
- 22/tcp — [[ssh]] (OpenSSH 7.6p1)
- 80/tcp — [[http]] (Apache 2.4.18)
- 161/udp — [[snmp]] (SNMPv1 public)
- 179/tcp — [[bgp]] (Quagga)
- 21/tcp — [[ftp]] (vsftpd 3.0.3)

## Lessons / notes
- SNMP often contains valuable configuration data like serial numbers
- Network device management interfaces frequently have command injection vulnerabilities
- BGP hijacking can redirect traffic through attacker-controlled infrastructure
- FTP credentials may be reused across services
- Network topology understanding is crucial for complex exploitation scenarios
