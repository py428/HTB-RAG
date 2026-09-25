---
type: machine
title: Zipping
platform: htb
os: linux
difficulty: medium
tags: [web, linux, privesc, php]
solved: 2026-07-09
sources: [[htb-zipping]]
related: []
---
# Zipping
> Zipping is a watch store with file upload functionality. The attack path involves abusing symlinks in zip files for file reads, bypassing PHP filters for SQL injection, writing webshells via MySQL FILE privilege, and privilege escalation through malicious shared library hijacking.

## Attack path
1. [[zip-symlink-file-read]] via calendar invite upload functionality
2. [[php-filter-bypass]] using newline character to bypass preg_match filtering
3. [[mysql-file-write]] via stacked SQL injection for webshell upload
4. [[lfi-exploitation]] to include and execute written PHP webshell
5. [[shared-library-hijacking]] for stock binary SUID privilege escalation

## Techniques used
- [[zip-symlink-file-read]] — Symbolic links in zip archives allow reading arbitrary files
- [[php-filter-bypass]] — Newline character (%0A) bypasses preg_match /^.*[A-Za-z] regex
- [[mysql-file-write]] — SELECT INTO OUTFILE with FILE privilege for webshell upload
- [[lfi-exploitation]] — Local file inclusion with .php extension and file_exists check
- [[shared-library-hijacking]] — SUID binary loads .so from user-writable directory

## Tools used
[[nmap]], [[feroxbuster]], [[unzip]], [[zip]], [[python]], [[sqlmap]], [[nc]], [[ssh]], [[gcc]], [[strings]], [[strace]]

## Services / ports
[[ssh]] (22), [[http]] (80), [[mysql]] (3306)

## Lessons / notes
- Zip --symlinks flag preserves symlinks instead of following them
- preg_match with /^.* only checks first line, allowing newline bypass
- MySQL FILE privilege and secure_file_priv="" enable file writes
- PHP file_exists check passes for phar:// wrapper references
- SUID binaries loading .so from user directories are vulnerable to hijacking