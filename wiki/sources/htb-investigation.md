---
type: source
title: "HTB Investigation writeup"
raw: raw/htb-investigation.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[investigation]]
---
# Source: HTB Investigation writeup
> Detailed writeup for HTB Investigation covering Exiftool command injection, Windows event log forensics, and binary abuse for privilege escalation.

## Key facts extracted
- Exiftool version 12.37 vulnerable to CVE-2022-23935 (command injection)
- Windows event logs from eForenzics-DI workstation
- Password "Def@ultf0r3nz!csPa$$" found in failed login event
- Custom binary requires specific argument format and downloads from URLs
- Binary executes downloaded files with perl and sets setuid(0)
- cron job cleanup broken due to immutable file attribute

## Filed into
[[investigation]], [[exiftool-cve-2022-23935]], [[evtx-analysis]]