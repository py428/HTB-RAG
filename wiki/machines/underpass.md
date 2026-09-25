---
type: machine
title: UnderPass
platform: htb
os: linux
difficulty: easy
tags: [snmp, radius, web, privesc]
solved: 2026-07-09
sources: [[htb-underpass]]
related: []
---
# UnderPass
> Easy Linux box featuring SNMP enumeration to discover a daloRADIUS server, default credential access, hash cracking for SSH, and sudo abuse on Mobile Shell (Mosh) for root.

## Attack path
1. [[snmp-enumeration]] to find daloRADIUS server and email
2. [[default-credentials]] on daloRADIUS operator login (administrator/radius)
3. [[hash-cracking]] user hash from daloRADIUS to get password
4. [[password-spraying]] credentials to gain SSH access as svcMosh
5. [[sudo-abuse]] running mosh-server as root to get root shell

## Techniques used
- [[snmp-enumeration]] — SNMP community string "public" reveals hostname and daloRADIUS reference
- [[default-credentials]] — daloRADIUS default operator login (administrator/radius)
- [[hash-cracking]] — cracking MD5 hash from daloRADIUS user database with hashcat
- [[sudo-abuse]] — sudo privileges on mosh-server allow spawning root shell via MOSH_KEY

## Tools used
- [[nmap]]
- [[snmpwalk]]
- [[feroxbuster]]
- hashcat
- [[netexec]]
- [[curl]]

## Services / ports
- [[snmp]] — UDP 161 (SNMPv1/v3 with community string "public")
- [[ssh]] — TCP 22
- [[http]] — TCP 80 (Apache with daloRADIUS application)

## Lessons / notes
- SNMP often exposes valuable system information even with default community strings
- daloRADIUS has well-known default credentials (administrator/radius)
- The hash found in daloRADIUS was a standard MD5 that could be cracked with hashcat
- Mosh server can be abused for privilege escalation when run with sudo - the MOSH_KEY environment variable controls authentication
- Username case sensitivity matters for SSH login (svcMosh vs svcmosh)
