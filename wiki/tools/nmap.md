---
type: tool
title: Nmap
category: network
tags: [recon, scanning]
updated: 2026-07-09
---

# Nmap

## What it does
Network/port scanner and service fingerprinter — the default first step to map a target's open ports, services, and OS.

## Common usage
```
nmap -p- --min-rate 10000 <ip>            # all TCP ports, fast
nmap -sCV -p <ports> <ip>                 # service/version + default scripts on found ports
```

## Used on
- [[absolute]] — mapped the DC's port set (DNS/Kerberos/LDAP/SMB/WinRM).
