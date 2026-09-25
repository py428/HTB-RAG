---
type: machine
title: Mentor
platform: htb
os: linux
difficulty: medium
tags: [linux, web, snmp, database, privesc]
solved: 2026-07-09
sources: [[htb-mentor]]
related: []
---
# Mentor
> Linux medium box with FastAPI and SNMP services, requiring SNMP brute force to find credentials, command injection for initial shell in container, database exfiltration, and password reuse for root.

## Attack path
1. [[snmp-brute-force]] to find "internal" community string with more access
2. [[snmp-enumeration]] to find login.py with password "kj23sadkj123as0-d213"
3. Use password for [[api-auth-bypass]] as james to get admin token
4. Exploit [[command-injection]] in /admin/backup endpoint for container shell
5. Use [[docker-tunneling]] with Chisel to access PostgreSQL from container
6. [[database-exfiltration]] to dump users table and crack hash
7. [[configuration-enumeration]] to find SNMPv3 credentials for root access

## Techniques used
- [[snmp-brute-force]] — SNMP community string brute forcing with snmpbrute.py
- [[snmp-enumeration]] — SNMP process enumeration for credentials in command lines
- [[api-auth-bypass]] — FastAPI authentication using found credentials
- [[command-injection]] — Command injection in backup endpoint
- [[docker-tunneling]] — Chisel tunnel from Docker container to host database
- [[database-exfiltration]] — PostgreSQL database dump for user hashes
- [[hash-cracking]] — Cracking MD5 hash with hashcat
- [[configuration-enumeration]] — Finding credentials in SNMP configuration

## Tools used
- [[nmap]]
- snmpbrute.py
- [[snmpwalk]]
- [[curl]]
- sqlmap
- Chisel
- [[psql]]
- [[hashcat]]
- sshpass

## Services / ports
- [[ssh]] (22)
- [[http]] (80)
- [[snmp]] (161)

## Lessons / notes
- SNMPv2c community strings can be brute forced to gain more access than "public"
- SNMP provides process command lines which may contain credentials
- FastAPI requires Authorization header but may not need "Bearer" prefix
- Chisel reverse tunneling allows accessing host services from container
- WordPress database tables contain user hashes even if API doesn't expose them
