---
type: source
title: "HTB Usage writeup"
raw: raw/htb-usage.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[usage]]
---
# Source: HTB Usage writeup
> Detailed writeup for HTB Usage covering blind SQL injection in password reset, CVE-2023-24249 exploitation, password reuse from Monit config, and 7z wildcard abuse for file read.

## Key facts extracted
- Laravel application with subdomain-based routing (usage.htb, admin.usage.htb)
- Blind SQL injection in forgot-password form allows database dumping
- Laravel-admin 1.8.18 vulnerable to file upload bypass via extension change
- Monit configuration contains password for user pivot
- Custom backup script uses 7z with wildcard, vulnerable to file inclusion

## Filed into
[[usage]], [[sqli-blind]], [[hash-cracking]], [[file-upload-bypass]], [[password-reuse]], [[7z-wildcard]]
