---
type: machine
title: Usage
platform: htb
os: linux
difficulty: easy
tags: [linux, web, laravel, easy]
solved: 2026-07-09
sources: [[htb-usage]]
related: []
---
# Usage
> Easy Laravel application box featuring blind SQL injection in password reset, CVE-2023-24249 for file upload bypass, password reuse, and 7z wildcard privilege escalation.

## Attack path
1. [[sqli-blind]] — boolean-based blind SQL injection in password reset email field
2. [[hash-cracking]] — crack bcrypt hash from admin_users table using hashcat
3. [[file-upload-bypass]] — exploit CVE-2023-24249 to upload PHP webshell via profile picture
4. [[password-reuse]] — Monit config password reuses for user pivot
5. [[7z-wildcard]] — abuse 7z wildcard with symlink files to read arbitrary files as root

## Techniques used
- [[sqli-blind]] — Boolean-based blind SQL injection in password reset form using conditional responses
- [[hash-cracking]] — Bcrypt hash cracking with hashcat and rockyou.txt wordlist
- [[file-upload-bypass]] — CVE-2023-24249 allows changing extension after client-side validation
- [[password-reuse]] — Password from `.monitrc` config file works for another user
- [[7z-wildcard]] — Create files starting with `@` to include other files as input list for 7z

## Tools used
- [[nmap]] — port scanning
- ffuf — subdomain fuzzing
- sqlmap — automated SQL injection exploitation
- [[hashcat]] — bcrypt hash cracking
- Burp Suite — request interception and modification
- 7za — file compression with wildcard vulnerability

## Services / ports
- [[ssh]] — 22/tcp
- [[http]] — 80/tcp (nginx, Laravel application)

## Lessons / notes
- SQL injection in password reset forms common for data extraction
- Laravel-admin < 1.8.19 vulnerable to arbitrary file upload (CVE-2023-24249)
- Client-side validation can be bypassed by modifying requests
- Password reuse common across services and users
- Wildcards in compression tools can lead to file inclusion vulnerabilities
- Monit configuration files may contain credentials
