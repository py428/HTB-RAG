---
type: source
title: "HTB Smasher2 writeup"
raw: raw/htb-smasher2.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[smasher2]]
---
# Source: HTB Smasher2 writeup
> Advanced binary exploitation guide covering Python C extension reference counting bug analysis, WAF evasion techniques, SSH key injection via API, and kernel driver mmap exploitation for credential structure manipulation and privilege escalation.

## Key facts extracted
- Backup directory protected with admin:clarabibi credentials (now removed in current version)
- Python Flask application with compiled ses.so session manager module containing reference counting bug
- WAF blocking direct command execution but allowing obfuscated variants
- dhid kernel module at /dev/dhid with mmap handler vulnerable to credential structure manipulation
- dzonerzy user in adm group providing access to auth.log and kernel module information

## Filed into
[[smasher2]], [[python-reference-counting-bug]], [[waf-bypass]], [[kernel-mmap-exploitation]]