---
type: machine
title: Clicker
platform: htb
os: linux
difficulty: medium
tags: [linux, web, nfs, sqli, linux-privesc]
solved: 2026-07-09
sources: [[htb-clicker]]
related: []
---
# Clicker
> Medium Linux box with PHP clicker game, NFS source backup leak, mass assignment via newline/SQLi bypass, webshell through file upload, setuid binary for SSH key theft, and three sudo privesc vectors.

## Attack path
1. [[nfs]] mount /mnt/backups reveals website source code
2. [[mass-assignment]] via role parameter bypass (newline injection or SQLi)
3. [[file-upload]] exploit to create PHP webshell with malicious nickname
4. [[setuid]] binary execute_query abuses to read jack's SSH key via directory traversal
5. Three [[sudo-privesc]] paths: PERL5OPT, http_proxy (XXE), [[ld-preload]]

## Techniques used
- [[mass-assignment]] — Role parameter bypass via newline injection or SQL injection
- [[newline-injection]] — Bypass role filter with %0a in parameter name
- [[file-upload]] — Export PHP webshell via unchecked extension parameter
- [[setuid]] — Abuse execute_query binary to read files via SQL command injection
- [[perl-debug]] — PERL5OPT=-d PERL5DB for code execution via xml_pp
- [[xxe]] — http_proxy interception for XML external entity file read
- [[ld-preload]] — Shared library injection for root shell

## Tools used
[[nmap]], ffuf, [[feroxbuster]], [[curl]], [[showmount]], [[ssh]], [[netcat]], gcc

## Services / ports
- TCP 22 — SSH
- TCP 80 — Apache clicker game
- TCP 111/2049 — NFS /mnt/backups share

## Lessons / notes
- NFS shares often contain source code backups
- Mass assignment vulnerabilities bypassable with whitespace tricks
- File upload filters often bypassable with unexpected extensions
- Setuid binaries can be abused for file reads via command injection
- Multiple sudo privesc vectors when environment variables preserved

## CVEs
None
