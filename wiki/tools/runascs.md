---
type: tool
title: RunasCs
category: post-exploit
tags: [ad, windows, execution, logon]
updated: 2026-07-09
---

# RunasCs

## What it does
Run a process as another user from a non-interactive (e.g. WinRM/webshell) Windows session where built-in `runas` is unavailable or blocked. Critically, lets you choose the **logon type** (`-l`), which matters when NTLM/network logons are restricted.

## Common usage
```
RunasCs.exe <user> '<pw>' -d <domain> -l 9 "cmd /c <command>"   # logon type 9 (NewCredentials)
```

## Used on
- [[absolute]] — gave the **interactive** context that [[kerberos-relay]] needs by running KrbRelay/KrbRelayUp with **logon type 9** (`-l 9`) from the WinRM session.
