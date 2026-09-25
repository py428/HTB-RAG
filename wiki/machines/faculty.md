---
type: machine
title: Faculty
platform: htb
os: linux
difficulty: medium
tags: [linux, web, sqli, file-read, sudo, gdb, ptrace]
solved: 2026-07-09
sources: [[htb-faculty]]
related: []
---
# Faculty
> PHP school management application with SQL injection, mPDF file read vulnerability, meta-git command injection, and gdb ptrace abuse for root.

## Attack path
1. [[sqli]] — Authentication bypass in login forms
2. [[mpdf-file-read]] — CVE-2021-XXXX for arbitrary file read via annotation tags
3. Database credentials from db_connect.php for SSH access
4. [[command-injection]] in meta-git for developer user
5. [[ptrace-shellcode-injection]] — gdb with cap_sys_ptrace for root shellcode execution

## Techniques used
- [[sqli]] — Login bypass with `' or 1=1;-- -` in both login forms
- [[mpdf-file-read]] — mPDF 6.0 annotation tag allows file inclusion
- [[command-injection]] — meta-git clone parameter injection via || operator
- [[ptrace-shellcode-injection]] — gdb with cap_sys_ptrace for arbitrary process injection

## Tools used
- [[nmap]], [[feroxbuster]], [[sqlmap]], [[curl]], [[crackmapexec]], [[gdb]]

## Services / ports
- [[ssh]] (22), [[http]] (80 - nginx)

## Lessons / notes
- Time-based blind SQL injection detected by sqlmap but manual exploitation simpler
- mPDF 6.0 vulnerable to local file read via <annotation file="path">
- meta-git command injection works even when git clone fails
- gdb with cap_sys_ptrace can attach to any process and inject shellcode
- SetUID bash on /tmp doesn't work when tmpfs mounted with nosuid

## CVEs
- CVE-2019-6447 (ES File Explorer) - not used on this box
- mPDF file read vulnerability (no CVE specified)