---
type: source
title: "HTB Forge writeup"
raw: raw/htb-forge.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[forge]]
---
# Source: HTB Forge writeup
> Detailed analysis of SSRF exploitation, FTP file access through internal admin interface, and Python debugger abuse for privilege escalation.

## Key facts extracted
- URL blacklist bypass using HTTP redirect chain
- Admin site supports FTP protocol for internal file access
- Python remote management script with pdb post_mortem on exceptions
- FTP credentials: user:heightofsecurity123!

## Filed into
[[forge]], [[ssrf]], [[ftp-enum]], [[python-debugger-abuse]]
