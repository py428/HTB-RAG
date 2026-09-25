---
type: machine
title: Intuition
platform: htb
os: linux
difficulty: hard
tags: [web, xss, docker, ansible, linux, privesc]
solved: 2026-07-09
sources: [[htb-intuition]]
related: []
---
# Intuition
> Intuition is a hard Linux box featuring a multi-domain web application with XSS vulnerabilities, file read capabilities, and Ansible automation for privilege escalation. The exploitation path involves blind XSS for cookie theft, Python urllib vulnerability for file reads, FTP access for SSH credentials, Suricata log analysis for password discovery, and Ansible Galaxy abuse for root access.

## Attack path
1. [[blind-xss]] in bug report form to steal admin and webdev cookies
2. [[python-urllib-bypass]] (CVE-2023-24329) for file read via wkhtmltopdf
3. [[ftp-access]] using credentials from backup script to get SSH key
4. [[log-analysis]] in Suricata FTP logs to find user password
5. [[ansible-galaxy-cve-2023-5115]] for symlink attack and privilege escalation

## Techniques used
- [[blind-xss]] — Stealing session cookies from admins reviewing bug reports
- [[python-urllib-bypass]] — Bypassing URL filtering with space prefix in urllib.parse
- [[file-read]] — Exporting arbitrary files as PDF via wkhtmltopdf SSRF
- [[log-analysis]] — Extracting credentials from Suricata FTP event logs
- [[command-injection]] — Injecting commands via Ansible role filename
- [[symlink-attack]] — Overwriting files via Ansible Galaxy role extraction

## Tools used
- [[nmap]] — Full port scanning and service detection
- [[ffuf]] — Subdomain fuzzing and enumeration
- [[feroxbuster]] — Directory brute forcing
- Python webserver — XSS payload collection
- [[steghide]] — Extracting hidden data from images (not used)
- [[ssh]] — Access with stolen keys and credentials
- [[sqlite3]] — Reading user database hashes
- [[hashcat]] — Cracking Werkzeug SHA256 hashes

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 8.9p1 Ubuntu
- 80/tcp — [[http]] — nginx 1.18.0 with multiple subdomains
- 4444/tcp — Selenium Grid (localhost only)
- 21/tcp — [[ftp]] — pyftpdlib 1.5.7 (localhost only)

## Lessons / notes
- Blind XSS can target privileged users viewing reports later
- Python urllib < 3.11.4 doesn't handle space-prefixed URLs correctly
- wkhtmltopdf can be exploited for SSRF and file reads
- Suricata logs FTP commands including passwords in plaintext
- Ansible Galaxy role extraction vulnerable to symlink attacks (CVE-2023-5115)
- Docker containers can provide VNC access for debugging and potential exploitation
- Custom Ansible runners may have command injection vulnerabilities

## Beyond Root
- Selenium container accessible via VNC on port 5900 (default password: secret)
- Docker escape possible via raw disk access through /proc/<pid>/root
- Unintended root path involved breaking out of Selenium container