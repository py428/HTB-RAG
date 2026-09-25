---
type: machine
title: Popcorn
platform: htb
os: linux
difficulty: medium
tags: [linux, web, privesc]
solved: 2026-07-09
sources: [[htb-popcorn]]
related: []
---
# Popcorn
> Medium Linux box with a torrent hosting application. Exploit file upload restrictions to get a PHP webshell, then leverage CVE-2010-0832 (PAM MOTD vulnerability) or DirtyCow for privilege escalation.
## Attack path
1. [[file-upload-bypass]] — Bypass torrent upload filters by changing Content-Type to image/png while keeping .php extension
2. [[cve-2010-0832]] — Exploit PAM MOTD vulnerability to gain ownership of `/etc/passwd` and add root user
3. Alternative: [[dirty-cow]] — Exploit kernel race condition to add root user to `/etc/passwd`
## Techniques used
- [[file-upload-bypass]] — Upload .php webshell by setting Content-Type to image/png (extension check bypassed)
- [[cve-2010-0832]] — Replace ~/.cache with symlink to target file, trigger via SSH login to change ownership
- [[dirty-cow]] — Race condition exploit in kernel to write to `/etc/passwd` as root
- [[password-hashing]] — Generate MD5 password hash with openssl for adding users
## Tools used
- [[nmap]] — Port scanning (SSH 22, HTTP 80)
- [[gobuster]] — Directory brute force on /torrent
- [[curl]] — Webshell interaction
- [[netcat]] — Reverse shell listener
- [[ssh-keygen]] — Generate SSH key pair for www-data user
- [[openssl]] — Generate password hash
- [[gcc]] — Compile dirty.c exploit
## Services / ports
- [[ssh]] — TCP 22 (OpenSSH 5.1p1, Ubuntu 9.10 Karmic)
- [[http]] — TCP 80 (Apache 2.2.12)
## Lessons / notes
- PAM MOTD vulnerability: When SSH login triggers ~/.cache/motd.legal-displayed creation, replacing ~/.cache with symlink to target file grants ownership
- Ubuntu 9.10 Karmic (2.6.31 kernel) vulnerable to both CVE-2010-0832 and DirtyCow (CVE-2016-5195)
- Matt user denied SSH login via DenyUsers in sshd_config, requiring su pivot
- DirtyCow exploit hangs occasionally but still adds user successfully
