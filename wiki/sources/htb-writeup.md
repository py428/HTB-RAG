---
type: source
title: "HTB Writeup writeup"
raw: raw/htb-writeup.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[writeup]]
---
# Source: HTB Writeup writeup
> Complete walkthrough of Writeup HackTheBox machine covering CMS Made Simple SQL injection exploitation, SSH credential cracking, staff group privilege escalation, and Perl module hijacking techniques.
## Key facts extracted
- CMS Made Simple v2.2.9 vulnerable to blind SQL injection
- Time-based SQLi using sleep() for data extraction
- MD5 password hashes with salt extraction and cracking
- staff group with write permissions to /usr/local/bin and /usr/local/sbin
- SSH login triggers run-parts with modified PATH
- Perl cleanup script running from cron with module loading
## Filed into
[[writeup]], [[blind-sqli]], [[staff-group-abuse]], [[perl-module-hijacking]], [[password-cracking]], [[linux]], [[web]]
