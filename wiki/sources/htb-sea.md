---
type: source
title: "HTB Sea writeup"
raw: raw/htb-sea.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[sea]]
---
# Source: HTB Sea writeup
> Comprehensive writeup for HTB Sea machine covering WonderCMS XSS exploitation, CVE-2023-41425 theme upload, password hash cracking, internal monitoring command injection, and multiple privilege escalation paths.

## Key facts extracted
- Sea runs WonderCMS with login URL at `/loginURL` and contact form vulnerable to stored XSS
- WonderCMS database.js contains admin password hash that can be cracked with rockyou.txt
- Internal monitoring service on localhost:8080 protected by HTTP basic auth
- Monitoring panel allows log file analysis with command injection vulnerability via file parameter

## Filed into
[[sea]], [[stored-xss]], [[theme-upload-exploit]], [[bcrypt-cracking]], [[command-injection]]
