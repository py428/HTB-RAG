---
type: source
title: "HTB Chatterbox writeup"
raw: raw/htb-chatterbox.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[chatterbox]]
---
# Source: HTB Chatterbox writeup
> Detailed exploitation of AChat buffer overflow on Windows with multiple shellcode generation methods, Meterpreter migration techniques, and ACL abuse for file read access.

## Key facts extracted
- AChat runs on non-standard ports 9255/9256
- SEH-based buffer overflow in AChat beta v0.150
- Multiple payload options: meterpreter, reverse shell, PowerShell
- AutoRunScript migration required for stable shell
- Alfred user has ACL modify permissions on Administrator's Desktop

## Filed into
[[chatterbox]], [[buffer-overflow]], [[seh-based-exploit]], [[acl-genericwrite]]
