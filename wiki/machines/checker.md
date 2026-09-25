---
type: machine
title: Checker
platform: htb
os: linux
difficulty: hard
tags: [linux, web, ad, sqli, ssrf, 2fa, linux-privesc]
solved: 2026-07-09
sources: [[htb-checker]]
related: []
---
# Checker
> Hard Linux box with BookStack (CVE-2023-6199) and Teampass (CVE-2023-1545), requiring SQL injection to leak hashes, SSRF with PHP filter chains for 2FA bypass, and shared memory race condition for root via sudo script.

## Attack path
1. [[sqli]] in Teampass /authorize endpoint (CVE-2023-1545) to leak bcrypt hashes
2. Crack bob's password with [[hashcat]] to access BookStack and SSH credentials
3. Exploit [[ssrf]] in BookStack (CVE-2023-6199) with [[php-filter-chains]] to read 2FA seed
4. SSH as reader with oathtool-generated TOTP code
5. Race condition in shared memory used by sudo check_leak script for [[ld-preload]] root

## Techniques used
- [[sqli]] — Teampass CVE-2023-1545 in /authorize endpoint via login parameter
- [[php-filter-chains]] — Blind file oracle technique for SSRF file read
- [[2fa-bypass]] — Read .google_authenticator file via SSRF to generate TOTP
- [[shared-memory-race]] — Poison shared memory between write and read operations
- [[ld-preload]] — Set malicious shared library via LD_PRELOAD environment variable

## Tools used
[[nmap]], ffuf, [[hashcat]], [[curl]], oathtool, sshpass, [[ssh]], evil-winrm, [[netexec]], gcc

## Services / ports
- TCP 22 — SSH with 2FA enabled
- TCP 80 — BookStack on Apache
- TCP 8080 — Teampass on Apache

## Lessons / notes
- SQL injection can leak data through JWT tokens in responses
- PHP filter chains allow blind file reads via error-based oracle
- Time sync critical for TOTP 2FA bypass
- Shared memory with writable permissions allows race condition exploitation
- Multiple sudo privesc paths: PERL5OPT, http_proxy (XXE), LD_PRELOAD

## CVEs
- CVE-2023-1545 — SQL Injection in Teampass < 3.0.0.23
- CVE-2023-6199 — SSRF in BookStack 23.10.2
