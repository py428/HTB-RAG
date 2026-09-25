---
type: source
title: "HTB Book writeup"
raw: raw/htb-book.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[book]]
---
# Source: HTB Book writeup
> Details SQL truncation attack for admin access, XSS in PDF generation, and logrotate exploitation.

## Key facts extracted
- SQL field length of 20 characters for email addresses
- admin@book.htb original password: Sup3r_S3cur3_P455
- PDF generation vulnerable to XSS with JavaScript file read
- logrotate config: /home/reader/backups/access.log with daily rotation, size 1k
- root runs logrotate every 5 seconds via /root/log.sh calling /usr/sbin/logrotate

## Filed into
[[book]], [[sql-truncation]], [[xss-file-read]], [[logrotten]]
