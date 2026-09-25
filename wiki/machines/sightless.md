---
type: machine
title: Sightless
platform: htb
os: linux
difficulty: easy
tags: [linux, web, docker, privesc]
solved: 2026-07-09
sources: [[htb-sightless]]
related: []
---
# Sightless
> SQLPad instance vulnerable to server-side template injection leading to container RCE, followed by hash cracking for SSH access and Froxlor XSS exploitation for root.
## Attack path
1. [[ssti]] → Server-side template injection in SQLPad connection test → RCE in container
2. [[hash-cracking]] → Crack michael user hash from /etc/shadow → SSH as michael
3. [[xss]] → Stored XSS in Froxlor login logs → Create admin account via CSRF
4. [[ftp-access]] → Access FTP with new admin creds → Find Keepass database with root SSH key
5. [[ssh]] → SSH as root with key
## Techniques used
- [[ssti]] — Server-Side Template Injection in SQLPad connection test endpoint using child_process.exec
- [[hash-cracking]] — SHA512 Unix hashes cracked with hashcat and rockyou.txt
- [[xss]] — Stored blind XSS in Froxlor failed login logs to execute JavaScript as admin
- [[ftp-access]] — FTP access after gaining Froxlor admin credentials
## Tools used
[[nmap]], [[feroxbuster]], hashcat, [[ssh]], [[curl]]
## Services / ports
- [[http]] (80) - nginx/1.18.0
- [[ftp]] (21) - ProFTPD (SSL/TLS required)
- [[ssh]] (22) - OpenSSH 8.9
## Lessons / notes
- SQLPad versions < 6.10.1 vulnerable to SSTI via connection test endpoint
- Container escape often requires finding credentials on host system
- XSS in admin panels can lead to account creation via CSRF
- FTP with SSL/TLS requires lftp or similar clients
- Chrome automation with Selenium visible in process enumeration
