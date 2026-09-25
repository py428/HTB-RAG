---
type: source
title: "HTB Awkward writeup"
raw: raw/htb-awkward.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[awkward]]
---
# Source: HTB Awkward writeup
> Detailed walkthrough of exploiting a Node.js HR application with authentication bypass, API vulnerabilities, and symlink-based command injection for privilege escalation.

## Key facts extracted
- Node.js application with Express framework and Webpack bundler
- Authentication bypass via cookie manipulation from "guest" to arbitrary value
- Staff details API exposes password hashes without authentication
- Internal service enumeration via SSRF in store status API
- Awk injection vulnerability allowing arbitrary file read using path manipulation
- Backup archive stored in home directory with SSH credentials in xpad notes
- Email processing vulnerable to command injection via mail --exec parameter
- Symlink abuse enables writing arbitrary content to system files

## Filed into
[[awkward]], [[cookie-bypass]], [[api-bypass]], [[ssrf]], [[awk-injection]], [[hash-cracking]], [[backup-analysis]], [[symlink-abuse]], [[command-injection]]
