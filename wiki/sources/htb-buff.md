---
type: source
title: "HTB Buff writeup"
raw: raw/htb-buff.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[buff]]
---
# Source: HTB Buff writeup
> Step-by-step exploitation of an easy Windows box starting with Gym Management System unauthenticated RCE, webshell deployment with filter bypasses, local enumeration revealing CloudMe service, and privilege escalation through CloudMe buffer overflow with custom shellcode.

## Key facts extracted
- Gym Management System 1.0 had unauthenticated file upload RCE vulnerability
- Upload required PNG magic bytes and .php.png double extension to bypass filters
- Windows Defender blocked "system" keyword but could be bypassed with HTML junk
- CloudMe 1.11.2 on localhost:8888 vulnerable to SEH buffer overflow
- Chisel port forwarding required to reach localhost-only CloudMe service
- Custom msfvenom shellcode used for stageless reverse TCP shell

## Filed into
[[buff]], [[file-upload]], [[webshell-upload]], [[port-forwarding]], [[buffer-overflow]]
