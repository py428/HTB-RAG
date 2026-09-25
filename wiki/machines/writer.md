---
type: machine
title: Writer
platform: htb
os: linux
difficulty: medium
tags: [linux, web, sqli, privesc]
solved: 2026-07-09
sources: [[htb-writer]]
related: []
---
# Writer
> Linux machine running CMS Made Simple with SQL injection vulnerability for authentication bypass and file read. Initial foothold via command injection in image upload, then privilege escalation through Django database credential cracking, Postfix mail filter abuse, and apt configuration file manipulation.
## Attack path
1. Exploit [[sqli]] to bypass authentication and read files from database
2. Gain shell through command injection in image URL processing using file:// protocol
3. Crack Django password hash from database to access as kyle user
4. Abuse Postfix mail filter running as john via SSH tunneling and email trigger
5. Exploit apt configuration file writable by john to get root shell
## Techniques used
- [[sqli]] — Authentication bypass and file read using UNION-based injection
- [[command-injection]] — Image upload via file:// URL with malicious filename
- [[django-cracking]] — PBKDF2_SHA256 password hash extraction and cracking
- [[postfix-abuse]] — Mail filter script injection for user escalation
- [[apt-config-abuse]] — APT Update::Pre-Invoke directive for command execution
## Tools used
- [[nmap]], [[feroxbuster]], [[sqlmap]], [[smbclient]], [[hashcat]], [[netcat]], swaks
## Services / ports
- [[ssh]] (22), [[http]] (80), [[smb]] (139/445), [[smtp]] (25)
## Lessons / notes
- SQLi with UNION injection can bypass authentication and read files
- Django PBKDF2_SHA256 hashes can be cracked with hashcat mode 10000
- Postfix mail filters run as specified user and process all incoming emails
- apt configuration files in /etc/apt/apt.conf.d are executed alphabetically
- APT::Update::Pre-Invoke allows command execution before apt operations
- SSH tunneling required to access localhost SMTP from external
