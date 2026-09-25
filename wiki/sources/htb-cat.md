---
type: source
title: "HTB Cat writeup"
raw: raw/htb-cat.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[cat]]
---
# Source: HTB Cat writeup
> Best Cat Competition website writeup covering exposed Git repository, XSS for cookie theft, SQL injection for webshell, hash cracking for user pivoting, log poisoning for credential discovery, and Gitea CVE exploitation for root access.

## Key facts extracted
- Machine: Cat (Medium, Linux)
- Exposed .git directory on TCP 80
- PHP application with SQLite database
- XSS via username field and HTML injection via onerror attribute
- SQLite stack injection for file write webshell
- MD5 password hashes crackable (rosa/soyunaprincesarosa)
- Apache access logs contain axel password (aNdZwgC4tI9gnVXv_e3Q)
- Gitea 1.22.0 with CVE-2024-6886 stored XSS
- Private Employee-management repo contains admin credentials (IKw75eR0MR7CMIxhH0)
- rosa user in adm group with access to logs

## Filed into
[[cat]], [[git-exposure]], [[xss]], [[html-injection]], [[sqlite-sqli]], [[webshell-upload]], [[hash-cracking]], [[log-poisoning]], [[gitea-cve-2024-6886]], [[ssrf]]
