---
type: source
title: "HTB Agile writeup"
raw: raw/htb-agile.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[agile]]
---
# Source: HTB Agile writeup
> Complete walkthrough of Agile, a medium Linux HackTheBox machine featuring a password manager application with Flask debug exploitation, Chrome debug session hijacking, and sudo vulnerability for privilege escalation.

## Key facts extracted
- Flask debug PIN requires: username, MAC address, machine-id, cgroup, and correct module name (wsgi_app)
- Database credentials: superpassuser / dSA6l7q*yIVs$39Ml6ywvgK
- User passwords stored in plaintext in MySQL database
- Chrome debug port 41829 exposed during Selenium testing
- All users source /app/venv/bin/activate via /etc/bash.bashrc
- edwards user has sudoedit permissions on config_test.json and creds.txt as dev_admin

## Filed into
[[agile]], [[directory-traversal]], [[flask-debug-rce]], [[chrome-debug-exploitation]], [[sudo-cve-2023-22809]]
