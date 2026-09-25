---
type: source
title: "HTB Sau writeup"
raw: raw/htb-sau.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[sau]]
---
# Source: HTB Sau writeup

> Quick exploitation of SSRF vulnerability in request-baskets to reach internal Maltrail service, followed by command injection and systemctl less pager abuse for root access.

## Key facts extracted

- Request-baskets 1.2.1 vulnerable to CVE-2023-27163 SSRF
- Internal Maltrail v0.53 service on ports 80 and 8338
- Maltrail login page username parameter vulnerable to OS command injection
- Puma user can run `sudo systemctl status trail.service` without password
- Less pager invoked by systemctl allows `!sh` command execution as root
- User flag location: `/home/puma/user.txt`
- Root flag location: `/root/root.txt`

## Filed into

[[sau]], [[ssrf]], [[command-injection]], [[less-pager-escape]]
