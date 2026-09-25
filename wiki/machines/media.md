---
type: machine
title: Media
platform: htb
os: windows
difficulty: medium
tags: [windows, web, privesc]
solved: 2026-07-09
sources: [[htb-media]]
related: []
---
# Media
> Windows medium box featuring a PHP video upload service that leaks NTLM hashes via .wax files, then escalates from local service to SYSTEM using FullPowers and GodPotato.

## Attack path
1. Capture [[ntlm-capture]] via .wax file upload to leak net-NTLMv2 hash
2. [[hash-cracking]] to get SSH credentials as enox
3. Abuse file upload system with [[junction-point]] to write webshell for local service shell
4. Use FullPowers to enable SeImpersonatePrivilege via [[privilege-escalation]]
5. Exploit with [[godpotato]] to get SYSTEM

## Techniques used
- [[ntlm-capture]] — NTLM hash capture via .wax file upload to Windows Media Player
- [[hash-cracking]] — Cracking NetNTLMv2 hash with hashcat
- [[junction-point]] — Windows junction point abuse to redirect uploads to web root
- [[webshell-upload]] — PHP webshell upload via junction point
- [[privilege-escalation]] — FullPowers to restore SeImpersonatePrivilege
- [[godpotato]] — GodPotato exploit for SYSTEM shell

## Tools used
- [[nmap]]
- Responder
- hashcat
- sshpass
- FullPowers
- GodPotato
- curl
- scp

## Services / ports
- [[ssh]] (22)
- [[http]] (80)
- [[rdp]] (3389)

## Lessons / notes
- .wax files (Windows Media Player shortcuts) can be used to capture NTLM hashes
- Windows junction points (mklink /J) can redirect file writes to arbitrary directories
- FullPowers restores default privileges for service accounts by creating a scheduled task
- GodPotato exploits SeImpersonatePrivilege to get SYSTEM shell
