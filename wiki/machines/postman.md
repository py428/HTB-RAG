---
type: machine
title: Postman
platform: htb
os: linux
difficulty: easy
tags: [linux, web, privesc]
solved: 2026-07-09
sources: [[htb-postman]]
related: []
---
# Postman
> Easy Linux box demonstrating Redis file write to gain SSH access, credential cracking for user pivot, and Webmin command injection for root.
## Attack path
1. [[redis-write-ssh]] — Write SSH public key to Redis authorized_keys file
2. [[ssh-key-cracking]] — Crack Matts encrypted SSH key with john
3. [[password-reuse]] — Use same password for Webmin login
4. [[webmin-command-injection]] — Exploit CVE-2019-12840 in package updates for root RCE
## Techniques used
- [[redis-write-ssh]] — Use Redis CONFIG to change directory to ~/.ssh and write authorized_keys via SAVE
- [[ssh-key-cracking]] — Use ssh2john.py to convert encrypted key for john cracking
- [[password-reuse]] — Matt reuses SSH key password for Webmin authentication
- [[webmin-command-injection]] — CVE-2019-12840: pipe command injection in package-updates/update.cgi
## Tools used
- [[nmap]] — Port scanning (SSH 22, HTTP 80, Redis 6379, Webmin 10000)
- [[redis-cli]] — Write SSH key and interact with Redis
- [[ssh-keygen]] — Generate RSA key pair for Redis access
- [[john]] — Crack encrypted SSH key (ssh2john.py format)
- [[curl]] — Webmin exploitation with Python requests
- [[netcat]] — Reverse shell listener
- [[gobuster]] — Directory brute force
## Services / ports
- [[ssh]] — TCP 22 (OpenSSH 7.6p1)
- [[http]] — TCP 80 (Apache 2.4.29)
- [[redis]] — TCP 6379 (Redis 4.0.9, unauthenticated)
- [[http]] — TCP 10000 (Webmin 1.910)
## Lessons / notes
- Redis MODULE command disabled, preventing master-slave RCE exploit
- Webmin password_change.cgi not enabled, requiring alternative CVE-2019-12840 exploit
- Matt denied SSH login via DenyUsers in sshd_config, requiring Webmin pivot
- Webmin package updates vulnerable to command injection via pipe in package name
