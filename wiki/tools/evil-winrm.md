---
type: tool
title: Evil-WinRM
category: post-exploit
tags: [ad, windows, winrm, shell]
updated: 2026-07-09
---

# Evil-WinRM

## What it does
Interactive PowerShell shell over WinRM (5985/5986) for Windows targets. Supports password, NT hash (`-H`), and Kerberos (`-r`/ccache) auth, plus conveniences like file upload/download and loading in-memory assemblies/PS modules.

## Common usage
```
evil-winrm -i <ip> -u <user> -H <ntlm_hash>                       # pass-the-hash
KRB5CCNAME=./user.ccache evil-winrm -i dc.<domain> -r <domain>     # Kerberos
```

## Used on
- [[absolute]] — both shells (as `winrm_user` via Kerberos ccache, and as `Administrator` via pass-the-hash after [[dcsync]]).
- [[forest]] — foothold as `svc-alfresco`, and shell as `Administrator` (hash).
