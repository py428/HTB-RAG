---
type: machine
title: "HTB Quick"
platform: htb
os: linux
difficulty: hard
tags: [linux, web, privesc, php, quic, docker]
solved: 2026-07-09
sources: [[htb-quick]]
related: []
---

# HTB Quick

> Quick was a chance to play with two technologies that I was familiar with, but I had never put hands on with either. First it was finding a website hosted over Quic/HTTP version 3. I'll build curl so that I can access that, and find creds to get into a ticketing system. In that system, I will exploit an edge side include injection to get execution, and with a bit more work, a shell. Next I'll exploit a new website available on localhost and take advantage of a race condition that allows me to read and write arbitrary files as the next user. Finally, to get root I'll find creds in a cached config file.

## Attack path

1. [[quic]] protocol support using custom-compiled curl for HTTP/3
2. [[file-include]] to find credentials in PDF documentation
3. [[esi-injection]] for SSRF and XSLT code execution via Edge Side Includes
4. [[race-condition]] exploitation in printer job processing for file read/write
5. [[sqli]] to dump and crack user hashes from database
6. [[credential-extraction]] from CUPS printer configuration cache
7. [[password-reuse]] for root access via su

## Techniques used

- [[quic]] — Building curl with HTTP/3 support to access portal.quick.htb on UDP 443
- [[file-include]] — Extracting credentials from Connectivity.pdf served over QUIC
- [[esi-injection]] — Injecting Edge Side Include tags for SSRF and XSLT-based RCE
- [[race-condition]] — Abusing race condition between file creation and printer read operations
- [[sqli]] — Manual and sqlmap-based SQL injection in Complain Management System
- [[symlink-abuse]] — Creating symlinks to read arbitrary files as srvadm via printer job
- [[credential-extraction]] — Extracting credentials from CUPS cache files
- [[password-reuse]] — Using discovered credentials for privilege escalation

## Tools used

- [[nmap]], [[curl]], [[gobuster]], [[feroxbuster]], [[wfuzz]], [[mysql]], [[sqlmap]], [[netcat]], [[ssh]]

## Services / ports

- [[http]] (80/9001) — Apache serving ticketing system and printer interface
- [[ssh]] (22) — OpenSSH 7.6p1
- [[quic]] (443/UDP) — HTTP/3 portal for customer access
- [[mysql]] (3306) — MySQL database backend

## Lessons / notes

- HTTP/3 requires specialized tooling - standard curl/nmap don't support QUIC protocol
- Edge Side Include injection can lead to SSRF and code execution via XSLT
- Race conditions in file operations can be exploited for symlink creation and arbitrary file read
- Multiple SQL injection points in legacy applications provide different exploitation paths
- CUPS printer configuration cache may contain credentials with URL encoding
- Symlink abuse requires precise timing between file creation and exploitation
- SSH tunneling can expose internal services not accessible from external network

## CVEs / exploits

- ESIGate ESI injection vulnerabilities
