---
type: source
title: "HTB Cap writeup"
raw: raw/htb-cap.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[cap]]
---
# Source: HTB Cap writeup
> 0xdf's writeup for HTB Cap machine covering IDOR exploitation, PCAP analysis, and Linux capabilities abuse for initial access and privilege escalation.

## Key facts extracted
- IDOR vulnerability allows accessing PCAP files by incrementing sequential IDs
- FTP credentials found in PCAP file: nathan / Buck3tH4TF0RM3!
- Python binary has cap_setuid capability for privilege escalation
- Box runs Ubuntu 20.04 with Flask application on port 80

## Filed into
[[cap]], [[idor]], [[pcap-analysis]], [[linux-capabilities]], [[ftp]], [[ssh]], [[web]], [[privilege-escalation]]
