---
type: source
title: "HTB Keeper writeup"
raw: raw/htb-keeper.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[keeper]]
---
# Source: HTB Keeper writeup
> Concise 0xdf writeup covering Request Ticket default credentials, KeePass password recovery from memory dump using CVE-2022-32784, and PuTTY key conversion for root access.

## Key facts extracted
- Ubuntu 22.04 running Request Tracker 4.4.4 with default root:password credentials
- User lnorgaard had KeePass crash dump (RT30000.zip) with password-protected database
- CVE-2022-32784 exploited to recover master password "rødgrød med fløde" from memory
- Root SSH key stored in KeePass in PuTTY format, converted using puttygen

## Filed into
[[keeper]], [[default-credentials]], [[keepass-password-dump]], [[putty-key-conversion]]
