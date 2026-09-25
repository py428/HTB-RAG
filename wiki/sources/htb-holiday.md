---
type: source
title: "HTB Holiday writeup"
raw: raw/htb-holiday.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[holiday]]
---
# Source: HTB Holiday writeup
> Detailed exploitation guide for Holiday HackTheBox machine covering SQL injection enumeration, XSS cookie theft, command injection with character restrictions, and npm preinstall script privilege escalation.
## Key facts extracted
- SQLite database with users, notes, bookings, sessions tables
- RickA credentials: fdc8cd4cff2c19e0d1022e78481ddf36 = "nevergonnagiveyouup" (MD5)
- XSS in notes approval system executed by PhantomJS headless browser
- Command injection in /admin/export?table= parameter with ampersand separator
- Sudo rule: (ALL) NOPASSWD: /usr/bin/npm i *
- npm preinstall scripts run as root during package installation
## Filed into
[[holiday]], [[sqli]], [[xss]], [[command-injection]], [[npm-hijack]]
