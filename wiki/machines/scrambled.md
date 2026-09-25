---
type: machine
title: Scrambled
platform: htb
os: windows
difficulty: medium
tags: [ad, windows, kerberos, mssql]
solved: 2026-07-09
sources: [[htb-scrambled]]
related: []
---
# Scrambled
> Scrambled is a medium Windows Active Directory box where NTLM authentication is disabled, forcing Kerberos-only tooling. The path involves web-based credential discovery, silver ticket generation, MSSQL access, custom .NET deserialization exploitation, and JuicyPotato for SYSTEM privilege escalation.

## Attack path
1. Enumerate web application and find user credentials in hints
2. Access file shares with discovered credentials  
3. [[kerberoasting]] to get service account challenge/response
4. Generate [[silver-ticket]] for MSSQL service access
5. Access MSSQL instance, find additional credentials
6. Use credentials for share access with custom .NET executables
7. Reverse engineer .NET binaries to find [[deserialization]] vulnerability
8. Exploit deserialization for user shell
9. [[juicy-potato]] for SYSTEM privilege escalation

## Techniques used
- [[kerberoasting]] — Service account ticket cracking for silver ticket
- [[silver-ticket]] — Forge MSSQL service ticket for database access
- [[mssql-xp-cmdshell]] — SQL Server command execution
- [[deserialization]] — .NET deserialization vulnerability in custom executables
- [[juicy-potato]] — COM abuse for SYSTEM privilege escalation
- [[ntlm-disabled-protected-users]] — Kerberos-only authentication requirement

## Tools used
[[nmap]], [[kerbrute]], [[impacket]], [[rubeus]], [[netexec]], [[mssql-client]], dnSpy, JuicyPotatoNG

## Services / ports
- [[kerberos]] (88) — Kerberos authentication required (NTLM disabled)
- [[smb]] (445) — File shares with credential hints
- [[mssql]] (1433) — SQL Server with xp_cmdshell enabled
- [[winrm]] (5985) — WinRM access with Kerberos authentication

## Lessons / notes
- Protected Users group and NTLM disabled require Kerberos tooling
- Silver tickets bypass KDC but require service account hash
- Custom .NET applications may contain deserialization vulnerabilities
- JuicyPotato works on recent Windows versions for SYSTEM escalation
- Web application hints provide initial credential discovery

## Beyond Root
- Alternative MSSQL file read techniques for credential discovery  
- JuicyPotatoNG usage for privilege escalation
- Windows vs Linux tooling differences for same exploits
