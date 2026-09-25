---
type: machine
title: DevArea
platform: htb
os: linux
difficulty: medium
tags: [linux, web, java, python, cve-exploit, command-injection, privesc]
solved: 2026-07-09
sources: [[htb-devarea]]
related: []
---

# DevArea

> Multi-service development environment hosting Java web service, API simulation tool, and monitoring dashboard where Apache CXF SSRF vulnerability leads to file read, Hoverfly command injection, and syswatch privilege escalation.

## Attack path

1. Download employee-service.jar from anonymous [[ftp]] server
2. Reverse engineer JAR to identify Apache CXF vulnerability and SOAP service
3. Exploit CVE-2022-46364 XOP Include for SSRF / arbitrary file read
4. Read process environment to obtain Hoverfly dashboard credentials
5. Exploit CVE-2025-54123 command injection in Hoverfly middleware for shell
6. Access syswatch monitoring application and forge session cookie with secret
7. Abuse command injection in service status check for privilege escalation
8. Exploit symlink race condition in sudo script to read root SSH key

## Techniques used

- [[anonymous-ftp]] — Access FTP server to download Java application files
- [[cve-exploit]] — Exploit Apache CXF CVE-2022-46364 XOP Include for file read
- [[ssrf]] — Server-side request forgery via XOP Include href parameter
- [[command-injection]] — Pipe character bypass in regex filter for RCE
- [[session-forging]] — Forge Flask session cookie with secret key
- [[symlink-race]] — Abuse symlink validation flaw in sudo script for file read

## Tools used

- [[nmap]] — Comprehensive port scanning and service enumeration
- [[jadx]] — Java decompilation and reverse engineering
- [[curl]] — SOAP request testing and exploit delivery
- [[hashcat]] — Password cracking (if needed for databases)
- [[flask-unsign]] — Flask session cookie forging
- [[netcat]] — Reverse shell catch listener
- hex encoding / xxd — Command obfuscation for injection bypass

## Services / ports

- [[ftp]] (21) — Anonymous access containing employee-service.jar
- [[ssh]] (22) — Secure shell access
- [[http]] (80) — Apache web server (static site)
- [[http]] (8080) — Java SOAP web service (Apache CXF)
- [[http]] (8500) — Hoverfly proxy service
- [[http]] (8888) — Hoverfly dashboard
- [[http]] (7777) — syswatch monitoring dashboard (localhost only)

## Lessons / notes

- Apache CXF before 3.4.10/3.5.5 vulnerable to CVE-2022-46364 XOP Include SSRF
- SOAP services with MTOM/XOP can be exploited for file read via multipart/related requests
- Process enumeration via `/proc` can reveal credentials in command line arguments
- Hoverfly 1.11.3 vulnerable to CVE-2025-54123 middleware command injection
- Flask session cookies can be forged if secret key is readable from environment files
- Regex filters attempting to block command injection often miss pipe characters and backticks
- Sudo scripts with symlink validation can be abused for privilege escalation via race conditions
- Multiple web services on different stacks require systematic enumeration and exploitation
- File read vulnerabilities combined with credential harvesting enable horizontal movement