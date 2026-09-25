---
type: machine
title: Breadcrumbs
platform: htb
os: windows
difficulty: hard
tags: [windows, web, privesc, crypto]
solved: 2026-07-09
sources: [[htb-breadcrumbs]]
related: []
---
# Breadcrumbs
> Hard Windows box featuring directory traversal for source code leaks, PHP session cookie and JWT token forgery, webshell upload, Sticky Notes password extraction, and password manager SQL injection.
## Attack path
1. [[directory-traversal]] — Leak PHP source code via bookController.php file read vulnerability
2. [[prng-prediction]] — Predict and forge PHP session cookies using time-based seed
3. [[jwt-forgery]] — Forge JWT tokens using exposed secret key from authController.php
4. [[php-deserialization]] — Exploit unserialize() in AvatarInterface class for webshell upload
5. [[hash-cracking]] — Crack MD5 password hashes with site-wide salt from database
6. [[sticky-notes-extraction]] — Extract plaintext passwords from Windows Sticky Notes SQLite database
7. [[sqli]] — SQL injection in custom password manager for admin credential extraction
## Techniques used
- [[directory-traversal]] — File read vulnerability in bookController.php with path traversal
- [[prng-prediction]] — Predict PHP session cookies seeded with time()
- [[jwt-forgery]] — Forge admin JWT tokens using hardcoded secret key
- [[php-deserialization]] — AvatarInterface __wakeup() method abuse for file upload
- [[hash-cracking]] — Crack MD5($salt . $password) hashes using hashcat mode 20
- [[sticky-notes-extraction]] — Extract passwords from plum.sqlite database
- [[sqli]] — UNION-based SQL injection in password manager API
## Tools used
- [[nmap]] — Full port scan identifying Apache, MySQL, SMB
- gobuster — Directory brute force with PHP extension
- python — Session cookie generation and JWT token forgery
- [[netcat]] — PowerShell reverse shell via nc64.exe
- [[hashcat]] — Password hash cracking with salt
- smbclient — Sticky Notes database exfiltration
- crackmapexec — Password validation and SSH access testing
- sqlite3 — Sticky Notes database parsing
- chisel — SSH tunneling for localhost service access
- curl — Local service interaction via tunnel
## Services / ports
- [[http]] (80/443) — Apache 2.4.46 with PHP 8.0.1
- [[ssh]] (22) — OpenSSH for Windows (alternative to RDP)
- [[smb]] (445) — File share access for Sticky Notes exfil
- mysql (3306) — Local database access (not directly used)
- Custom TCP 1234 — Internal password manager service
## Lessons / notes
- File read vulnerabilities provide excellent reconnaissance for complex web apps
- Weak PRNG seeding with time() allows predictable session cookie generation
- Hardcoded JWT secret keys enable trivial token forgery
- PHP deserialization vulnerabilities can lead to file upload and RCE
- Windows Sticky Notes stores passwords in plaintext SQLite database
- Custom password managers often have SQL injection vulnerabilities