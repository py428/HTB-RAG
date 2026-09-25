---
type: source
title: "HTB SolidState writeup"
raw: raw/htb-solidstate.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[solidstate]]
---
# Source: HTB SolidState writeup
> Detailed writeup covering James mail server exploitation, directory traversal for arbitrary file write, restricted shell escape, and cron job hijacking.

## Key facts extracted
- James Remote Admin accessible on TCP 4555 with default root/root
- Five user accounts: james, thomas, john, mindy, mailadmin
- Mindy's email contains SSH credentials: mindy / P@55W0rd1!2@
- User mindy has rbash restricted shell
- CVE-2017-12629: James directory traversal in username creation
- Bash completion scripts execute on any user login
- World-writable Python script /opt/tmp.py in cron running as root

## Filed into
[[solidstate]], [[james-directory-traversal]], [[rbash-escape]], [[cronjob-hijack]]
