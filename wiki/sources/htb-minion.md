---
type: source
title: "HTB Minion writeup"
raw: raw/htb-minion.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[minion]]
---
# Source: HTB Minion writeup
> Windows insane box requiring ICMP-based shell construction due to firewall restrictions, scheduled task hijacking, and alternative data stream credential extraction for Administrator access.

## Key facts extracted
- test.asp allows SSRF to localhost, revealing admin panel and webshell
- Webshell at cmd.aspx has blind command execution
- Firewall blocks all outbound except ICMP, requiring custom ICMP shell
- Scheduled task runs world-writable c.ps1 every 5 minutes
- backup.zip contains password in NTFS alternate data stream "pass"
- root.exe implements flag protection requiring current directory check

## Filed into
[[minion]], [[ssrf]], [[webshell]], [[icmp-tunnel]], [[scheduled-task]], [[alternative-data-stream]], [[reverse-engineering]], [[pscredential]]
