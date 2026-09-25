---
type: machine
title: BroScience
platform: htb
os: linux
difficulty: medium
tags: [linux, web, privesc]
solved: 2026-07-09
sources: [[htb-broscience]]
related: []
---
# BroScience
> Medium Linux box featuring directory traversal for source code analysis, PRNG prediction for activation bypass, PHP deserialization for RCE, password hash cracking, and certificate-based command injection.
## Attack path
1. [[directory-traversal]] — Double URL-encoding to bypass filters and read PHP source
2. [[prng-prediction]] — Predict activation codes using time-seeded PRNG
3. [[php-deserialization]] — Exploit unserialize() in AvatarInterface for webshell
4. [[hash-cracking]] — Crack PostgreSQL MD5 hashes with site-wide salt
5. [[command-injection]] — Craft malicious certificate for cron job command injection
## Techniques used
- [[directory-traversal]] — Double URL-encoded path traversal (..%252f) in img.php
- [[prng-prediction]] — Time-based PRNG seeding in generate_activation_code()
- [[php-deserialization]] — AvatarInterface __wakeup() method with file_get_contents()
- [[hash-cracking]] — Crack MD5($salt . $password) using hashcat mode 20
- [[command-injection]] — Certificate CN field injection in openssl renewal script
## Tools used
- [[nmap]] — Port scan identifying Apache and PostgreSQL
- wfuzz — Directory traversal fuzzing with dotdotpwn wordlist
- [[feroxbuster]] — Web directory enumeration with PHP extension
- php — Activation code generation and serialized payload creation
- [[hashcat]] — Password hash cracking with salt
- [[john]] — Alternative hash cracking tool
- [[psql]] — PostgreSQL database interaction
- openssl — Malicious certificate generation
- [[curl]] — Webshell interaction and testing
## Services / ports
- [[ssh]] (22) — OpenSSH 8.4p1 Debian 5+deb11u1
- [[http]] (80/443) — Apache 2.4.54 with PHP
- Custom TCP 61614 — Additional web service
## Lessons / notes
- Double URL-encoding can bypass directory traversal filters
- Time-seeded PRNG is predictable for activation codes
- PHP deserialization with __wakeup() provides file write capabilities
- Database password hashing often includes site-wide salts
- Certificate renewal scripts may be vulnerable to command injection in CN fields