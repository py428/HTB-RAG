---
type: source
title: "HTB Json writeup"
raw: raw/htb-json.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[json]]
---
# Source: HTB Json writeup
> Comprehensive 0xdf writeup covering Json's .NET deserialization vulnerability and three distinct privilege escalation paths (FileZilla admin, custom binary decryption, and JuicyPotato).

## Key facts extracted
- Windows Server 2012 R2 with IIS 8.5, FileZilla FTP, and WinRM
- .NET deserialization via JSON API using ysoserial.net WindowsIdentity gadget
- Three separate priv esc paths documented (FileZilla admin interface, custom .NET binary reversal, JuicyPotato)
- FileZilla admin interface accessible on localhost TCP 14147

## Filed into
[[json]], [[deserialization]], [[port-forwarding]], [[juicypotato]]
