---
type: machine
title: Minion
platform: htb
os: windows
difficulty: insane
tags: [windows, web, icmp, scheduled-task, privesc]
solved: 2026-07-09
sources: [[htb-minion]]
related: []
---
# Minion
> Windows insane box with firewall restrictions forcing ICMP-only exfiltration, featuring blind command execution, ICMP shell construction, and scheduled task hijacking for privilege escalation.

## Attack path
1. Discover [[ssrf]] via test.asp allowing localhost access
2. Find [[webshell]] at cmd.aspx with blind command execution
3. Build [[icmp-tunnel]] shell due to firewall restrictions
4. Hijack [[scheduled-task]] (c.ps1) for SYSTEM shell
5. Extract password from [[alternative-data-stream]] on backup.zip
6. Reverse engineer root.exe or use [[pscredential]] for Administrator access

## Techniques used
- [[ssrf]] — Server-side request forgery via test.asp to access localhost
- [[webshell]] — ASP webshell at cmd.aspx with blind execution
- [[icmp-tunnel]] — ICMP-based shell due to outbound firewall restrictions
- [[scheduled-task]] — PowerShell script hijacking via world-writable c.ps1
- [[alternative-data-stream]] — NTFS alternate data stream for credential storage
- [[reverse-engineering]] — Binary analysis of root.exe flag protector
- [[pscredential]] — PowerShell credential object for elevated execution

## Tools used
- [[nmap]]
- [[wfuzz]]
- [[feroxbuster]]
- Scapy
- sqlmap (alternative method)
- [[john]]

## Services / ports
- [[http]] (62696)

## Lessons / notes
- Firewall blocking all outbound except ICMP requires custom shell implementation
- ASP webshells can have blind execution requiring ICMP exfiltration
- Scheduled tasks running PowerShell scripts can be hijacked if world-writable
- NTFS alternate data streams can hide passwords in files
- Reverse engineering can extract flags from protected executables
- PScredential objects enable running commands as other users
