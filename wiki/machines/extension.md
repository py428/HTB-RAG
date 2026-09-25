---
type: machine
title: Extension
platform: htb
os: linux
difficulty: hard
tags: [linux, web, idor, password-reset, firefox-extension, docker]
solved: 2026-07-09
sources: [[htb-extension]]
related: []
---
# Extension
> Complex multi-stage exploitation with IDOR, password reset token manipulation, custom Firefox extension, and Docker breakout.

## Attack path
1. [[database-dump]] via admin management endpoint to leak user hashes
2. [[password-crack]] to access site and email
3. [[idor]] to identify target user Jean Castux
4. [[password-reset-token-prediction]] — predictable tokens allow access as target user
5. Custom Firefox extension for [[xss]] → file download from Gitea
6. SSH access, then [[command-injection]] in web app container
7. [[docker-socket-abuse]] for container escape to host root

## Techniques used
- [[database-dump]] — Laravel management endpoint dumps user table
- [[password-crack]] — SHA256 hash cracking with hashcat
- [[idor]] — Insecure direct object reference on snippet IDs
- [[password-reset-token-prediction]] — Weak token generation (MD5 + random)
- [[xss]] — Stored XSS in custom Firefox extension
- [[command-injection]] — Hash extension template injection
- [[docker-socket-abuse]] — Writable Docker socket for container escape

## Tools used
- [[nmap]], [[wfuzz]], [[hashcat]], [[john]], [[curl]]

## Services / ports
- [[ssh]] (22), [[http]] (80)

## Lessons / notes
- Laravel applications may expose management endpoints via JavaScript route definitions
- Token predictability stems from partially random generation (first 32 chars = MD5 of email)
- Custom browser extensions can bypass normal XSS filters
- Docker socket access = immediate root via container creation