---
type: machine
title: Soccer
platform: htb
os: linux
difficulty: easy
tags: [linux, web, sqli, privesc]
solved: 2026-07-09
sources: [[htb-soccer]]
related: []
---
# Soccer
> Easy Linux box starting with default credentials in Tiny File Manager to upload webshell, then SQL injection over websocket to leak credentials, and finally doas plugin abuse for root shell.

## Attack path
1. Find [[tiny-file-manager]] with default credentials (admin/admin@123)
2. Upload [[webshell]] via file manager to get shell as www-data
3. Discover second virtual host with websocket-based ticket validation
4. Exploit [[sqli-websocket]] to leak player credentials from database
5. SSH as player and abuse [[doas-plugin]] to craft malicious dstat plugin for root

## Techniques used
- [[tiny-file-manager]] — Default credentials lead to RCE via PHP upload
- [[webshell]] — PHP system() execution for initial foothold
- [[sqli-websocket]] — Blind SQL injection over websocket protocol
- [[doas-plugin]] — Craft malicious dstat plugin for privilege escalation

## Tools used
- [[nmap]]
- [[feroxbuster]]
- [[ffuf]]
- [[netcat]]
- [[sqlmap]]

## Services / ports
- [[ssh]] (22)
- [[http]] (80) — nginx with Tiny File Manager
- websocket (9091) — Custom application

## Lessons / notes
- Always check default credentials for web applications
- Tiny File Manager has known default credentials
- SQL injection can exist over websocket connections
- sqlmap supports websocket injection testing
- doas is OpenBSD alternative to sudo with plugin support
- dstat plugins are Python scripts executed in user context
