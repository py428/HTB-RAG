---
type: machine
title: Union
platform: htb
os: linux
difficulty: medium
tags: [web, sql, php, privesc]
solved: 2026-07-09
sources: [[htb-union]]
related: []
---
# Union
> Medium Linux box featuring tricky UNION SQL injection for file reads, database credential extraction, and command injection via X-Forwarded-For header.

## Attack path
1. [[sql-injection-union]] in player parameter for data extraction
2. [[file-read-via-sql]] using MySQL LOAD_FILE() function
3. [[credential-extraction]] from config.php to get database credentials
4. [[password-reuse]] between database and SSH access
5. [[command-injection]] via X-Forwarded-For header in firewall.php
6. [[sudo-abuse]] with full sudo privileges for www-data

## Techniques used
- [[sql-injection-union]] — Blind UNION injection in player parameter
- [[file-read-via-sql]] — MySQL LOAD_FILE() to read arbitrary files
- [[command-injection]] — X-Forwarded-For header injected into iptables command
- [[sudo-abuse]] — www-data has NOPASSWD: ALL in sudoers

## Tools used
- [[nmap]]
- [[curl]]
- [[feroxbuster]]
- [[netcat]]
- sshpass

## Services / ports
- [[ssh]] — TCP 22 (openssh after flag submission)
- [[http]] — TCP 80 (nginx 1.18.0 PHP application)

## Lessons / notes
- Some SQL injection points are subtle - small output differences matter
- MySQL LOAD_FILE() requires FILE privilege and can read files
- Light filtering ("WAF") can be bypassed with careful payload construction
- X-Forwarded-For headers are often logged but can be command injection points
- Default WAF behavior can sometimes be bypassed by understanding what triggers it
- Web application firewalls may filter common strings like "or" but miss other payloads
- Always check sudo privileges even when you think you're done

## CVEs
- No CVEs used - standard web vulnerabilities
