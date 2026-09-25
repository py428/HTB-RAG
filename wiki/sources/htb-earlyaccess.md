---
type: source
title: "HTB EarlyAccess writeup"
raw: raw/htb-earlyaccess.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[earlyaccess]]
---
# Source: HTB EarlyAccess writeup
> Hard game company themed box with multiple Docker containers. Exploitation chain: XSS for admin access, SQL injection for database, custom key algorithm, command injection via hash functions, Docker breakout, and Linux capabilities abuse. Writeup covers game key reverse engineering, container exploitation, and privilege escalation.

## Key facts extracted
- Multiple subdomains: earlyaccess.htb, game.earlyaccess.htb, dev.earlyaccess.htb
- XSS in profile username allowed stealing admin session cookie
- Second-order SQL injection from main site to game site scoreboard
- Custom game key validation with magic number changing every 30 minutes
- PHP allowed calling arbitrary functions as hash functions with debug parameter
- Docker entrypoint.d directory allowed script execution on container restart
- arp binary had all capabilities (=ep) for file read

## Filed into
[[earlyaccess]], [[xss]], [[second-order-sqli]], [[key-validation]], [[command-injection]], [[docker-container-breakout]], [[capabilities-abuse]]
