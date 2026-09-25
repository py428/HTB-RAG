---
type: machine
title: Interpreter
platform: htb
os: linux
difficulty: medium
tags: [java, deserialization, linux, database, privesc]
solved: 2026-07-09
sources: [[htb-interpreter]]
related: []
---
# Interpreter
> Interpreter is a medium Linux box hosting Mirth Connect, a healthcare integration engine. The exploitation path leverages an unauthenticated XStream deserialization vulnerability in the Mirth API for initial access, followed by database credential extraction, password cracking, and Python template injection in a Flask notification service for root access.

## Attack path
1. [[xstream-deserialization]] (CVE-2023-43208) in Mirth Connect API for RCE
2. [[database-credential-extraction]] from Mirth configuration files
3. [[password-cracking]] PBKDF2-HMAC-SHA256 hash from MariaDB
4. [[python-template-injection]] in Flask notification server for privesc

## Techniques used
- [[xstream-deserialization]] — Exploiting unauthenticated XStream deserialization in Mirth API
- [[database-credential-extraction]] — Reading database credentials from mirth.properties
- [[password-cracking]] — Cracking PBKDF2-HMAC-SHA256 with hashcat
- [[python-template-injection]] — Abusing eval() on f-string wrapped input in Flask
- [[base64-encoding]] — Bypassing character restrictions in injection payloads

## Tools used
- [[nmap]] — Port scanning and service fingerprinting
- [[curl]] — Testing API endpoints and exploit delivery
- Python script — CVE-2023-43208 exploit implementation
- [[mysql]] — Database access for credential extraction
- [[hashcat]] — Cracking PBKDF2-HMAC-SHA256 hashes
- [[netcat]] — Shell handling and reverse connections
- ssh — User access with cracked credentials

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 9.2p1 Debian
- 80/tcp — [[http]] — Mirth Connect Administrator (HTTP)
- 443/tcp — [[https]] — Mirth Connect Administrator (HTTPS)
- 6661/tcp — HL7 v2 MLLP listener (Mirth Connect)
- 3306/tcp — MariaDB (localhost only)
- 54321/tcp — Python Flask notification server (localhost only)

## Lessons / notes
- XStream deserialization can bypass denylist protections with different gadget chains
- Mirth Connect stores database credentials in plaintext configuration files
- PBKDF2-HMAC-SHA256 with 600,000 iterations requires significant cracking time
- Python eval() on f-strings allows code execution with curly braces
- Flask template injection often bypasses filters with __import__() built-in
- Healthcare systems like HL7 may expose version information in responses