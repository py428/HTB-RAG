---
type: machine
title: RainyDay
platform: htb
os: linux
difficulty: hard
tags: [web, linux, container, python, privesc, docker]
solved: 2026-07-09
sources: [[htb-rainyday]]
related: []
---
# RainyDay
> Complex multi-stage exploitation involving Flask application IDOR vulnerability, Docker container breakout via process inspection, Python sandbox escape using use-after-free vulnerability, and cryptographic secret recovery using Unicode truncation technique.

## Attack path
1. Exploit [[idor]] vulnerability in API to leak bcrypt password hashes by accessing user endpoints with decimal suffix
2. Crack gary user hash and access container management interface
3. Establish Chisel SOCKS proxy from container to access internal dev.rainycloud.htb
4. Exploit regex API endpoint for file read vulnerability to leak Flask secret key
5. Forge session cookies to access jack user account and secrets container
6. Escape container jail via /proc filesystem inspection of jack's long-running sleep process
7. Exploit Python use-after-free vulnerability to bypass import restrictions in safe_python script
8. Recover secret salt from hash system using Unicode character truncation technique
9. Crack root hash using recovered salt to achieve system access

## Techniques used
- [[idor]] — Access user API endpoints with decimal suffix (1.0) to bypass authentication
- [[container-breakout]] — Escape Docker jail via /proc filesystem of host processes
- [[python-exec-bypass]] — Exploit use-after-free in memoryview to bypass Python import restrictions
- [[unicode-truncation]] — Use multi-byte Unicode characters to bypass bcrypt 72-byte limit and recover secret
- [[file-read]] — Exploit regex matching API to read arbitrary files via custom patterns

## Tools used
- [[nmap]] — Port scanning and service enumeration
- [[ffuf]] — Subdomain fuzzing and user enumeration
- [[feroxbuster]] — Web directory brute forcing
- [[john]] — Bcrypt password hash cracking
- [[flask-unsign]] — Flask session cookie forging
- [[chisel]] — SOCKS proxy tunneling
- [[python3]] — Exploit development and hash manipulation
- [[bcrypt]] — Hash verification and secret recovery testing

## Services / ports
- SSH (22) — OpenSSH 8.9p1 Ubuntu
- HTTP (80) — Nginx with Flask application (rainycloud.htb)

## Lessons / notes
- IDOR vulnerabilities can manifest in unexpected ways like decimal suffix handling
- Docker containers with host process access can be escaped via /proc filesystem inspection
- Python's memoryview use-after-free allows bypassing import restrictions in sandboxed environments
- Unicode multi-byte characters can bypass string length checks while expanding in bytes for hash operations
- Background process execution in containers runs as different user (UID 1000), enabling unintended jailbreaks
- bcrypt has 72-byte character limit that can be exploited for secret recovery using Unicode truncation