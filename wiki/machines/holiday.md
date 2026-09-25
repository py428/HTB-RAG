---
type: machine
title: Holiday
platform: htb
os: linux
difficulty: hard
tags: [linux, web, nodejs]
solved: 2026-07-09
sources: [[htb-holiday]]
related: []
---
# Holiday
> Hard Linux box with a Node.js booking application requiring SQL injection, XSS exploitation, and command injection for initial access, followed by npm preinstall script abuse for root shell.
## Attack path
1. Enumerate [[http]] (8000) running Node.js Express
2. Exploit SQL injection in login form to enumerate database and extract RickA credentials
3. Authenticate and use XSS in notes system to steal administrator session cookie
4. Access admin panel and find command injection in export function (table parameter)
5. Use hex IP address and wget to stage reverse shell, bypassing filters
6. Exploit sudo npm i * privilege to gain root via malicious package.json
## Techniques used
- [[sqli]] — SQL injection in login form with double-quote payload, SQLite database
- [[xss]] — Cross-site scripting in notes approval system to steal admin cookie
- [[command-injection]] — Command injection in export table parameter with & separator
- [[npm-hijack]] — Sudo npm install with preinstall script for root execution
## Tools used
- [[nmap]]
- [[gobuster]]
- dirsearch
- [[burp]] (repeater)
- [[nc]]
- wget
## Services / ports
- [[http]] (8000) — Node.js Express application
- [[ssh]] (22) — OpenSSH 7.2p2 Ubuntu
## Lessons / notes
- SQL injection requires testing both single and double quotes
- SQLite injection uses sqlite_master and sqlite_version for version detection
- XSS payloads can bypass filters using img tags with backtick execution context
- Command injection character restrictions bypassed with hex IP notation (0x7f000001)
- npm preinstall scripts execute before package installation, useful for privilege escalation
- User-Agent filtering affects directory enumeration tool results
