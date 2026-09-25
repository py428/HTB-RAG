---
type: source
title: "HTB Mentor writeup"
raw: raw/htb-mentor.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[mentor]]
---
# Source: HTB Mentor writeup
> Linux medium box involving SNMP brute force, FastAPI exploitation, Docker container escape via database tunneling, and SNMP configuration enumeration for root credentials.

## Key facts extracted
- SNMP brute force finds "internal" community string with elevated access
- Process enumeration via SNMP reveals login.py password: kj23sadkj123as0-d213
- FastAPI /admin/backup endpoint has command injection requiring trailing semicolon
- Application runs in Docker container with PostgreSQL on host
- Database contains user hashes not exposed via API
- SNMP configuration contains SNMPv3 bootstrap user password

## Filed into
[[mentor]], [[snmp-brute-force]], [[snmp-enumeration]], [[command-injection]], [[docker-tunneling]], [[database-exfiltration]], [[hash-cracking]], [[configuration-enumeration]]
