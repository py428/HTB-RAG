---
type: source
title: "HTB Resolute writeup"
raw: raw/htb-resolute.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[resolute]]
---
# Source: HTB Resolute writeup
> Comprehensive guide for the Resolute HackTheBox machine covering RPC enumeration, password spraying, PowerShell transcript analysis, and DNSAdmins privilege escalation.

## Key facts extracted
- RPC null session enables full user enumeration without credentials
- User account marcus has default password in description field
- PowerShell transcripts enabled system-wide in C:\PSTranscripts
- ryan's credentials found in transcript mapping network drive
- ryan is member of DnsAdmins and Contractors groups
- Contractors group has Remote Management Users permissions
- dnscmd /config /serverlevelplugindll allows DLL loading

## Filed into
[[resolute]], [[rpc-null-session]], [[password-spray]], [[powershell-transcript]], [[dnsadmins-dnscmd-abuse]]
