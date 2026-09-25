---
type: machine
title: RedCross
platform: htb
os: linux
difficulty: medium
tags: [linux, web, sqli, xss, postgres, kernel, bof]
solved: 2026-07-09
sources: [[htb-redcross]]
related: []
---
# RedCross
> Multi-path Linux box with web exploitation, SQL injection, Haraka SMTP RCE, PostgreSQL manipulation for SSH jail, and kernel buffer overflow.

## Attack path
1. Enumerate subdomains to find admin.redcross.htb and intra.redcross.htb
2. Either steal admin cookie via [[xss]] in contact form or use SQLi to get credentials
3. Access admin panel to open firewall ports and create SSH jail user
4. Expit [[haraka-rce]] or use [[postgresql-nss]] abuse to get shell as penelope
5. Escalate to root via [[sudo]] group manipulation, [[postgresql-nss]] UID 0, or [[buffer-overflow]] in setuid iptctl binary

## Techniques used
- [[xss]] — Inject script in contact form phone field to steal admin PHPSESSID cookie
- [[sqli]] — Blind SQLi in ?o parameter to dump user hashes and crack charles account
- [[haraka-rce]] — Expited Haraka 2.8.8 SMTP attachment handling for RCE
- [[postgresql-nss]] — Abused PostgreSQL user database controlling SSH jail to add users with arbitrary GID/UID
- [[buffer-overflow]] — 64-bit ROP chain in setuid iptctl binary calling setuid(0) and execvp("sh")

## Tools used
[[nmap]], [[gobuster]], [[wfuzz]], [[sqlmap]], [[hashcat]], [[metasploit]], [[psql]], [[gdb]], [[pwntools]]

## Services / ports
[[ssh]] (22), [[http]] (80), [[https]] (443), [[ftp]] (21), Haraka SMTP (1025), [[postgresql]] (5432)

## Lessons / notes
- Contact form phone field lacked XSS filtering present in other fields
- SQLi required --delay due to WAF on the target
- PostgreSQL NSS (Name Service Switch) integration allows database-controlled user authentication
- SSH chroot jail configured via Match group associates in sshd_config
- 64-bit buffer overflow requires ROP with different calling conventions than 32-bit