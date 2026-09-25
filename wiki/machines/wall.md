---
type: machine
title: Wall
platform: htb
os: linux
difficulty: medium
tags: [linux, web, cve, privesc, sudo, suid, waf-bypass, python-reverse-engineering]
solved: 2026-07-09
sources: [[htb-wall]]
related: []
---
# Wall
> Wall is a medium Linux box featuring a Centreon monitoring installation accessible through a misconfigured authentication bypass. Initial access exploits CVE-2019-13024, a Centreon RCE vulnerability, while bypassing a ModSecurity WAF that blocks common payloads using ${IFS} for spaces. Privilege escalation involves decompiling Python bytecode to recover credentials and exploiting a SUID screen binary for root access.

## Attack path
1. [[bypass-authentication]] on /monitoring endpoint using POST instead of GET → discover /centreon
2. [[password-spraying]] against Centreon API → find admin:password1 credentials
3. [[cve-2019-13024]] (Centreon RCE) with [[waf-bypass]] using ${IFS} instead of spaces → shell as www-data
4. [[python-bytecode-decompilation]] of backup.pyc → recover shelby credentials
5. [[suid-binary-exploitation]] of screen 4.5.0 → root shell

## Techniques used
- [[waf-bypass]] — ModSecurity WAF blocking spaces, hostname, nc, ncat, passwd characters; bypassed using ${IFS} environment variable
- [[cve-2019-13024]] — Centreon v19.04 authenticated RCE via poller configuration injection point
- [[python-bytecode-decompilation]] — Recovered password from compiled Python backup script using uncompyle6
- [[suid-binary-exploitation]] — Exploited screen 4.5.0 SUID binary using shared library hijacking technique

## Tools used
- [[nmap]], [[gobuster]], [[hydra]], [[curl]], [[netcat]], [[ssh]], [[uncompyle6]], [[gcc]]

## Services / ports
- 22/tcp — [[ssh]] (OpenSSH 7.6)
- 80/tcp — [[http]] (Apache 2.4.29) → Centreon v19.04

## Lessons / notes
- The .htaccess configuration only required authentication on GET requests, allowing POST to bypass auth
- ModSecurity WAF can be bypassed using environment variables like ${IFS} instead of blocked characters
- Python bytecode can be decompiled to recover hardcoded credentials built character-by-character
- SUID screen exploits are well-documented with reliable exploit scripts available
- The Centreon exploit required authentication, emphasizing credential enumeration importance
