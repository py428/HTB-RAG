---
type: machine
title: Heist
platform: htb
os: windows
difficulty: easy
tags: [windows, web, privesc]
solved: 2026-07-09
sources: [[htb-heist]]
related: []
---
# Heist
> Windows box featuring a Cisco router configuration exposed on a website containing password hashes. After cracking the hashes, use RPC to enumerate users, gain WinRM access, and dump Firefox process memory to obtain the administrator password.
## Attack path
1. Enumerate [[http]] service and find Cisco router configuration attachment
2. Extract and crack Cisco Type 5 (MD5) and Type 7 (reversible) password hashes using [[john]]
3. Use [[rpc-null-session]] via [[rpcclient]] to enumerate additional domain users
4. Authenticate to [[winrm]] using found credentials (chase)
5. Dump Firefox process memory using procdump to extract admin password from POST data
6. Authenticate as administrator via [[winrm]]
## Techniques used
- [[password-cracking]] — Cracked Cisco Type 5 hash with john and Type 7 with custom XOR decryption script
- [[rpc-null-session]] — Used rpcclient with credentials to brute force SIDs and enumerate domain users
- [[process-memory-dump]] — Dumped Firefox process memory with procdump to extract credentials
- [[password-reuse]] — Web admin password reused for local administrator account
## Tools used
- [[nmap]]
- [[smbmap]]
- crackmapexec
- [[rpcclient]]
- [[evil-winrm]]
- [[john]]
- procdump
- [[grep]]
## Services / ports
- [[http]] (80) — IIS 10.0 with login page
- [[rpc]] (135, 49669) — Windows RPC for user enumeration
- [[smb]] (445) — Microsoft-DS
- [[winrm]] (5985) — WinRM for remote shell access
## Lessons / notes
- Cisco Type 7 passwords use a simple XOR with a static key: "tfd;kfoA,.iyewrkldJKD"
- Firefox process memory can contain POST data with passwords even after login
- Procdump can create full memory dumps of running processes for analysis
- User agent filtering on websites can affect directory enumeration results
