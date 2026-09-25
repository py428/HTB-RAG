---
type: machine
title: WingData
platform: htb
os: linux
difficulty: easy
tags: [linux, web, cve, privesc]
solved: 2026-07-09
sources: [[htb-wingdata]]
related: []
---
# WingData
> Wing FTP Server running on Linux with anonymous access enabled, exploited via a null-byte injection vulnerability (CVE-2025-47812) to gain initial shell. Privilege escalation involves cracking FTP password hashes and exploiting a Python tarfile vulnerability (CVE-2025-4517) in a backup script.
## Attack path
1. Exploit [[cve-2025-47812]] (null-byte injection in Wing FTP web interface) to get RCE as wingftp user
2. Extract and crack SHA256 salted password hashes from Wing FTP data files to gain access as wacky user
3. Exploit [[cve-2025-4517]] (tarfile path validation bypass) via sudo backup script to write arbitrary files as root
## Techniques used
- [[cve-2025-47812]] — Wing FTP null-byte injection allowing Lua code execution via session file manipulation
- [[password-cracking]] — SHA256 hashes with salt from Wing FTP user configuration files
- [[cve-2025-4517]] — Python tarfile module path validation bypass to write files outside extraction directory
- [[sudo-abuse]] — Backup script that can be run as root with arbitrary parameters
## Tools used
- [[nmap]], [[ffuf]], [[feroxbuster]], [[hashcat]], [[netcat]], ssh
## Services / ports
- [[ssh]] (22), [[http]] (80), FTP services
## Lessons / notes
- CVE-2025-47812 is a critical 10.0 CVSS vulnerability affecting Wing FTP Server before 7.4.4
- The vulnerability allows anonymous users to execute arbitrary Lua code by injecting null bytes into usernames
- Wing FTP stores SHA256 passwords with salt in XML configuration files
- CVE-2025-4517 bypasses tarfile's "data" filter using PATH_MAX overflow tricks
- Python 3.12's tarfile extraction filters were supposed to add security but introduced new bypasses
