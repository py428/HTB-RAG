---
type: source
title: "HTB Timing writeup"
raw: raw/htb-timing.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[timing]]
---
# Source: HTB Timing writeup
> Comprehensive guide for HackTheBox Timing machine covering timing attack username enumeration, LFI exploitation, mass assignment privilege escalation, and custom binary abuse for root access.
## Key facts extracted
- Timing attack vulnerability with 1-second sleep for valid usernames
- PHP LFI with directory traversal filtered but php://filter bypass available
- Mass assignment in profile update allowing role parameter injection
- Predictable upload filename generation using server time
- Custom netutils Java binary vulnerable to symlink abuse
- Ubuntu 18.04 with Apache 2.4.29 and PHP
## Filed into
[[timing]], [[lfi]], [[timing-attack]], [[mass-assignment]], [[file-upload]], [[symlink-abuse]]
