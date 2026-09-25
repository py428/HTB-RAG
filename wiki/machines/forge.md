---
type: machine
title: Forge
platform: htb
os: linux
difficulty: medium
tags: [ssrf, web, ftp, python]
solved: 2026-07-09
sources: [[htb-forge]]
related: []
---
# Forge
> An image gallery with SSRF vulnerability leads to internal admin site access and FTP file exfiltration, culminating in Python debugger exploitation for root access.

## Attack path
1. Enumerate [[subdomain-enumeration]] to find admin.forge.htb
2. Exploit [[ssrf]] with redirect bypass to access internal admin site
3. Use [[ssrf]] via admin site to enumerate and fetch files from [[ftp]]
4. Extract SSH private key from FTP for user access
5. Exploit [[python-debugger-abuse]] in sudo script for root shell

## Techniques used
- [[ssrf]] — URL filter bypass using HTTP redirects to access internal admin site
- [[ftp-enum]] — SSRF to FTP for file enumeration and exfiltration
- [[python-debugger-abuse]] — Trigger PDB debugger exception handling in Python script for root shell

## Tools used
- [[nmap]], [[feroxbuster]], [[wfuzz]], [[ffuf]], [[nc]], [[curl]], [[ssh]]

## Services / ports
- [[ssh]] (22), [[http]] (80), [[ftp]] (21 - filtered)

## Lessons / notes
- SSRF filter bypass using redirect chain: target server returns 302 to blocked URL
- Python scripts with pdb.post_mortem in exception handlers are debuggable
- Input validation bypass in non-integer menu options triggers ValueError for PDB access
