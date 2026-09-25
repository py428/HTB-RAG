---
type: machine
title: BountyHunter
platform: htb
os: linux
difficulty: easy
tags: [web, xxe, linux, privesc]
solved: 2026-07-09
sources: [[htb-bountyhunter]]
related: []
---
# BountyHunter
> Simple bug bounty reporting form vulnerable to XXE (XML External Entity) injection for file disclosure, leading to SSH access and Python eval injection for root.

## Attack path
1. Discover bug reporting form at /log_submit.php submitting XML data via tracker_diRbPr00f314.php
2. Identify [[xxe]] vulnerability in XML processing, test with /etc/passwd
3. Use PHP filter wrapper php://filter/convert.base64-encode/resource= to read files
4. Extract database credentials from /var/www/html/db.php
5. SSH as development user with leaked credentials
6. Identify sudo ticketValidator.py script running as root
7. Exploit [[python-eval-injection]] in ticket validation to get root shell

## Techniques used
- [[xxe]] — Inject PHP filter via XML ENTITY to read files with base64 encoding
- [[php-filter-wrapper]] — Bypass PHP file read issues with php://filter/convert.base64-encode
- [[python-eval-injection]] — Inject Python code in ticket markdown for eval() execution

## Tools used
- [[nmap]], [[feroxbuster]], [[base64]], [[ssh]], [[python3]]

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 8.2p1 Ubuntu
- 80/tcp — [[http]] — Apache (bug bounty site)

## Lessons / notes
- XML XXE requires DOCTYPE and ENTITY definitions with SYSTEM or FILE URIs
- PHP files may fail to read directly via XXE, use php://filter wrapper
- Python eval injection payload format: **32+110+43+ __import__('os').system('bash')
- Ticket validator checks for modular 7 remainder 4 before calling eval
- Create ticket as markdown file with specific header format
