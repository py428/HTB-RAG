---
type: machine
title: Timing
platform: htb
os: linux
difficulty: medium
tags: [linux, web, privesc]
solved: 2026-07-09
sources: [[htb-timing]]
related: []
---
# Timing
> Timing is a Linux box demonstrating a timing attack vulnerability in a login form for username enumeration, combined with LFI and mass assignment vulnerabilities. Root is achieved through abusing a custom Java download utility.
## Attack path
1. Use [[lfi]] with PHP filter to read source code and identify timing-based username enumeration
2. Perform [[timing-attack]] to identify valid user "aaron" and default password
3. Exploit [[mass-assignment]] to escalate role from 0 to 1 for admin access
4. Upload webshell via [[file-upload]] vulnerability and execute through LFI
5. Access SSH with leaked password from Git backup
6. Pivtoot to root via [[symlink-abuse]] in custom netutils download program
## Techniques used
- [[lfi]] — PHP filter base64-encode for source code disclosure and file inclusion
- [[timing-attack]] — Sleep-based username enumeration via login timing differences
- [[mass-assignment]] — Role parameter injection to escalate privileges
- [[file-upload]] — Predictable filename generation using time() and uniqid()
- [[symlink-abuse]] — abusing netutils to overwrite root's authorized_keys via symlink
## Tools used
[[nmap]], [[feroxbuster]], [[wfuzz]], [[hashcat]], [[netcat]], [[chisel]], [[proxychains]], ssh, python3
## Services / ports
- [[ssh]] (22)
- [[http]] (80) - Apache 2.4.29 with PHP application
## Lessons / notes
- Timing attacks can reveal valid usernames even with consistent error messages
- os.path.join with absolute path input bypasses directory traversal filters
- Mass assignment vulnerabilities allow privilege escalation through parameter injection
- Predictable upload filenames can be calculated from server timestamps
- Ubuntu 18.04 sudo preserves $HOME by default, allowing .axelrc abuse for alternative root
