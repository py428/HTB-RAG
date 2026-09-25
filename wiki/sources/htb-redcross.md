---
type: source
title: "HTB RedCross writeup"
raw: raw/htb-redcross.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[redcross]]
---
# Source: HTB RedCross writeup
> Multi-path exploitation including XSS for cookie theft, SQL injection for credential harvesting, Haraka SMTP RCE, PostgreSQL NSS abuse for SSH jail manipulation, and kernel buffer overflow.

## Key facts extracted
- XSS vulnerability in contact form phone field allowed stealing admin PHPSESSID cookie
- SQLi in ?o parameter dumped users table with bcrypt hashes, charles cracked to "cookiemonster"
- Admin panel allowed opening firewall ports and creating users in SSH jail
- Haraka 2.8.8 SMTP server vulnerable to attachment handling RCE
- PostgreSQL NSS integration controlled SSH jail user authentication via passwd_table
- Setuid iptctl binary had 64-bit buffer overflow with NX enabled requiring ROP chain

## Filed into
[[redcross]], [[xss]], [[sqli]], [[haraka-rce]], [[postgresql-nss]], [[buffer-overflow]]