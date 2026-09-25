---
type: machine
title: Falafel
platform: htb
os: linux
difficulty: hard
tags: [linux, web, privesc]
solved: 2026-07-09
sources: [[htb-falafel]]
related: []
---
# Falafel
> A PHP web application box featuring SQL injection, PHP type juggling vulnerabilities for authentication bypass, file upload with filename truncation to get webshell, then framebuffer screenshot extraction to get a user password, and disk group access for root flag.
## Attack path
1. Enumerate HTTP services with [[nmap]] and [[gobuster]]
2. Perform [[username-enumeration]] using [[wfuzz]] on login form
3. Exploit [[sqli]] with [[sqlmap]] to dump database and crack user password
4. Bypass admin login using [[type-juggling]] with magic hash "240610708"
5. Upload webshell via [[file-upload-truncation]] vulnerability (239+ char filenames truncated to bypass extension filter)
6. Access [[www-data]] shell via webshell
7. Find database credentials in connection.php and re-use as user password
8. Capture framebuffer from [[framebuffer]] (/dev/fb0) to visualize another user's desktop
9. Read user password from screenshot and SSH in
10. Access root via [[disk-group]] - read raw disk device or use [[debugfs]] to read root.txt
## Techniques used
- [[sqli]] — Blind SQL injection in login form to enumerate users and dump password hashes
- [[type-juggling]] — PHP type comparison weakness allows login with "240610708" matching MD5 hash starting with "0e"
- [[file-upload-truncation]] — Filename length limit causes truncation, allowing .php.png to become .php
- [[framebuffer]] — Video group membership allows reading /dev/fb0 to capture screen contents
- [[disk-group]] — Disk group access allows reading raw block devices to extract root flag
## Tools used
- [[nmap]], [[gobuster]], [[wfuzz]], [[sqlmap]], [[hashcat]]
- python -m http.server, [[curl]], [[netcat]]
## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 7.2p2 Ubuntu
- 80/tcp — [[http]] — Apache httpd 2.4.18 with PHP
## Lessons / notes
- PHP type juggling occurs when comparing strings to numbers using loose equality (==)
- Magic hashes are hashes that start with "0e" and are treated as zero in scientific notation
- Framebuffer devices (/dev/fb*) contain raw screen data that can be captured and viewed
- Disk group membership provides direct access to block devices, bypassing filesystem permissions
