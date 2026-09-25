---
type: source
title: "HTB Alert writeup"
raw: raw/htb-alert.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[alert]]
---
# Source: HTB Alert writeup
> Walkthrough of exploiting a markdown viewer with XSS, using blind XSS to read internal pages, directory traversal to access Apache configuration, and cronjob hijacking for privilege escalation.

## Key facts extracted
- Markdown viewer allows arbitrary HTML/script injection
- Admin clicks links in contact messages, enabling blind XSS attacks
- Directory traversal vulnerability in messages.php file parameter
- Apache .htpasswd file accessible and crackable with hashcat
- Monitoring script includes writable configuration file executed as root

## Filed into
[[alert]], [[xss-blind]], [[directory-traversal]], [[htpasswd-crack]], [[cronjob-hijack]]
