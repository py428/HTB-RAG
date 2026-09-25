---
type: source
title: "HTB Union writeup"
raw: raw/htb-union.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[union]]
---
# Source: HTB Union writeup
> Detailed walkthrough of UNION SQL injection exploitation leading to command injection and root access.

## Key facts extracted
- Player parameter injectable with UNION SQL injection
- MySQL LOAD_FILE() can read files from filesystem
- Database credentials: uhc/uhc-11qual-global-pw from config.php
- firewall.php vulnerable to command injection via X-Forwarded-For header
- www-data user has full sudo privileges (NOPASSWD: ALL)

## Filed into
[[union]], [[sql-injection-union]], [[file-read-via-sql]], [[command-injection]], [[sudo-abuse]]
