---
type: machine
title: VariaType
platform: htb
os: linux
difficulty: medium
tags: [git, file-read, cve, fontforge, setuptools, path-traversal, cronjob-hijack]
solved: 2026-07-09
sources: [[htb-variatype]]
related: []
---
# VariaType
> Font foundry with exposed Git repo on validation portal and vulnerable font generation on main site. Chain involves Git credential exposure, directory traversal for file reads, CVE-2025-66034 for arbitrary file write via fonttools, CVE-2024-25082 for FontForge command injection through cron, and CVE-2025-47273 for root via setuptools path traversal.

## Attack path
1. [[git-exposure]] — Exposed `.git` directory on portal.variatype.htb reveals credentials
2. [[directory-traversal]] — Single-pass filter bypass (`....//`) in `download.php` for file reads
3. [[cve-2025-66034]] — Abused fonttools varLib arbitrary file write via malicious `.designspace` file
4. [[cve-2024-25082]] — Command injection via FontForge processing uploaded fonts in cron
5. [[cve-2025-47273]] — Path traversal in setuptools PackageIndex for arbitrary file write as root

## Techniques used
- [[git-exposure]] — Git repository exposed on `/dev/.git` with hardcoded credentials in diff
- [[directory-traversal]] — Weak filter in `download.php` removing `../` only once; bypassed with `....//`
- [[cve-2025-66034]] — fonttools varLib allows arbitrary file write via crafted `.designspace` XML with `labelname` CDATA injection
- [[cve-2024-25082]] — FontForge 20230101 vulnerable to command injection via archive filenames with `$()` command substitution
- [[cve-2025-47273]] — setuptools <78.1.1 has path traversal in `PackageIndex.download()` allowing writes outside tmpdir
- [[cronjob-hijack]] — FontForge invoked via cron every 2 minutes processing uploaded fonts

## Tools used
- [[nmap]]
- [[ffuf]]
- [[git-dumper]]
- [[flask-unsign]]
- [[curl]]
- [[feroxbuster]]
- [[uv]] (Python package manager)
- [[netcat]]

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 9.2p1 Debian
- 80/tcp — [[http]] — nginx 1.22.1

## Lessons / notes
- Git history revealed credentials: `gitbot:G1tB0t_Acc3ss_2025!`
- File read vulnerability was not an LFI, just file disclosure (PHP not executed)
- Main site was Flask (`secret_key` in source), portal was PHP
- fonttools 4.50.0 vulnerable to CVE-2025-66034
- FontForge 20230101 vulnerable to CVE-2024-25082 (fixed in 20240308)
- setuptools 78.1.0 vulnerable to CVE-2025-47273 (fixed in 78.1.1)
- Cron ran as steve every 2 minutes: `/home/steve/bin/process_client_submissions.sh`
- `sudo` allowed steve to run `/opt/font-tools/install_validator.py` as root
