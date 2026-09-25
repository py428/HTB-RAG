---
type: machine
title: Charon
platform: htb
os: linux
difficulty: hard
tags: [linux, web, sqli, crypto, privesc]
solved: 2026-07-09
sources: [[htb-charon]]
related: []
---
# Charon

> Hard Linux box featuring SQL injection bypassing WAF filters, file upload exploitation, RSA factorization, and SUID binary command injection for privilege escalation.

## Attack path
1. [[sql-injection]] in forgot.php → operator credential dump via UNION bypass
2. Admin login → [[file-upload-bypass]] via magic bytes + hidden field manipulation → webshell
3. RSA private key factorization → decoder user password
4. [[suid-exploitation]] → command injection via supershell binary → root shell

## Techniques used
- [[sql-injection]] — UNION-based SQL injection with case variation (UNiON) to bypass WAF
- [[file-upload-bypass]] — PNG magic bytes with embedded PHP webshell + hidden form field
- [[rsa-factorization]] — Small 256-bit RSA key factored via factordb.com
- [[command-injection]] — Subshell execution via $() in SUID binary
- [[suid-exploitation]] — Path validation bypass in supershell binary for root command execution

## Tools used
- [[nmap]] — Port scanning identifying HTTP and SSH services
- [[gobuster]] — Directory enumeration discovering /cmsdata and other paths
- [[curl]] — SQL injection testing and webshell command execution
- python crypto — Manual RSA factorization and decryption
- [[ssh]] — Remote access with cracked credentials
- ltrace — Binary analysis to understand supershell behavior
- [[netcat]] — Traditional netcat for reverse shell

## Services / ports
- [[http]] (80) — PHP web application with CMS and upload functionality
- [[ssh]] (22) — Remote shell access with cracked credentials

## Lessons / notes
- WAF filters can often be bypassed with case variations (UNiON vs UNION)
- UNION-based SQL injection requires matching column count and proper data type casting
- File upload filters can be bypassed by combining multiple techniques (magic bytes + form manipulation)
- Small RSA keys (256-bit) are trivial to factor using online databases
- SUID binaries may have command validation that can be bypassed with alternative syntax
- Command injection via $() subshells can bypass character blacklists
- Binary analysis with ltrace can quickly reveal vulnerability patterns
- Hidden form fields in HTML can sometimes be leveraged for file name manipulation
