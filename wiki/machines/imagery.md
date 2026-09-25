---
type: machine
title: Imagery
platform: htb
os: linux
difficulty: medium
tags: [linux, web, flask, xss, directory-traversal, ssti, command-injection, password-cracking, sudo, privesc, backup-forensics]
solved: 2026-07-09
sources: [[htb-imagery]]
related: []
---
# Imagery
> Imagery hosts a Flask-based image gallery application with multiple vulnerabilities. The attack chain exploits stored XSS for admin access, directory traversal for source code review, command injection in image transformation, password cracking from database dumps, encrypted backup forensics for additional credentials, and sudo abuse of a custom backup utility for root access.

## Attack path
1. [[xss]] — Stored XSS in bug report feature to steal admin cookie
2. [[directory-traversal]] — Admin directory traversal to read application source code
3. [[command-injection]] — Command injection in image crop feature for RCE as test user
4. [[password-cracking]] — Crack MD5 password hashes from database
5. [[backup-forensics]] — Brute-force pyAesCrypt password, extract older database backup
6. [[password-cracking]] — Crack additional user hash from backup for horizontal movement
7. [[sudo]] — Exploit sudo permissions on custom charcol backup utility
8. [[adcs-template-abuse]] — Alternative path via ADCS template abuse

## Techniques used
- [[xss]] — Stored XSS in bug report details to steal admin Flask session cookie
- [[directory-traversal]] — Admin path traversal via log_identifier parameter to read source code
- [[command-injection]] — Command injection in ImageMagick crop transformation requiring test user account
- [[password-cracking]] — Crack MD5 and SHA256 hashes using CrackStation and hashcat
- [[backup-forensics]] — Brute-force pyAesCrypt encrypted backup with custom script
- [[sudo]] — Abuse sudo permissions on charcol backup utility for privilege escalation
- [[adcs-template-abuse]] — ADCS ESC4 abuse via template modification for certificate enrollment

## Tools used
- [[nmap]], [[feroxbuster]], [[curl]], [[flask-unsign]], [[hashcat]], [[crackstation]], [[evil-winrm]]
- CyberChef, pyAesCrypt, 7z2john.pl, john, certipy, bloodyAD, dacledit.py

## Services / ports
- [[ssh]] (22), [[http]] (8000)
- Werkzeug/3.1.3 Python/3.12.7, Flask application, ImageMagick

## Lessons / notes
- XSS exploitation requires non-HttpOnly session cookies in Flask applications
- Directory traversal can reveal sensitive configuration and source code
- Command injection often requires specific user permissions or contexts
- Password cracking can reveal additional attack surfaces and credentials
- Encrypted backups may contain additional credentials but require password recovery
- Custom backup utilities may have unintended privilege escalation paths
- ADCS ESC4 is a powerful attack vector in Active Directory environments
- The box demonstrates a complex web application with multiple security issues
