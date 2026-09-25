---
type: source
title: "HTB Yummy writeup"
raw: raw/htb-yummy.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[yummy]]
---
# Source: HTB Yummy writeup
> Complete writeup covering Yummy restaurant reservation system exploitation including directory traversal, RSA factorization for JWT forgery, SQL injection for file upload, and privilege escalation through Mercurial hooks and rsync SetUID abuse.

## Key facts extracted
- Flask application with SQLite calendar invite generation vulnerable to directory traversal
- JWT tokens signed with weak RSA key (small q factor 2^19-2^20)
- MySQL database with FILE privilege and secure_file_priv="" for file writes
- Multiple cron jobs running from /data/scripts with writable directory
- Mercurial repository containing committed database credentials
- Mercurial hooks executing as dev user via sudo
- rsync with SetUID bash copy for root privilege escalation

## Filed into
[[yummy]], [[directory-traversal]], [[rsa-weak-factorization]], [[jwt-forgery]], [[sqli]], [[mysql-file-write]], [[cronjob-abuse]], [[mercurial-credentials]], [[mercurial-hook-abuse]], [[rsync-privesc]]