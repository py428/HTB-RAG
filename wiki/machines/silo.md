---
type: machine
title: Silo
platform: htb
os: windows
difficulty: medium
tags: [windows, oracle, privesc, web]
solved: 2026-07-09
sources: [[htb-silo]]
related: []
---
# Silo
> Oracle database exploitation with webshell upload, memory forensics for password extraction, and multiple paths to SYSTEM via pass-the-hash or direct Oracle execution.
## Attack path
1. [[oracle-enumeration]] → SID enumeration with ODAT → Database credentials (SCOTT:tiger with SYSDBA)
2. [[oracle-webshell]] → Upload ASPX webshell via utl_file → IIS webshell access
3. [[powershell-reverse-shell]] → PowerShell reverse shell from webshell → Shell as low-priv user
4. [[memory-forensics]] → Volatility analysis of memory dump → Extract Administrator NTLM hash
5. [[pass-the-hash]] → psexec with NTLM hash → SYSTEM shell
6. Alternative: [[oracle-direct-execution]] → ODAT externaltable execution → Direct SYSTEM shell
## Techniques used
- [[oracle-enumeration]] — ODAT for SID guessing and user enumeration, SYSDBA privilege escalation
- [[oracle-webshell]] — File upload via utl_file or dbmsadvisor to IIS webroot for webshell access
- [[memory-forensics]] — Volatility framework for hashdump on Windows memory dump
- [[pass-the-hash]] — NTLM hash reuse with impacket psexec for system access
- [[oracle-direct-execution]] — ODAT externaltable for direct command execution as SYSTEM
## Tools used
[[nmap]], [[odat]], [[sqlplus]], [[metasploit]], [[netcat]], [[volatility]], [[impacket]], [[msfvenom]]
## Services / ports
- [[http]] (80) - IIS 8.5
- [[oracle-tns]] (1521) - Oracle TNS listener 11.2.0.2.0
- [[smb]] (445) - Microsoft-ds
- [[winrm]] (5985) - WinRM/HTTP
## Lessons / notes
- Oracle databases often run with SYSTEM privileges on Windows
- SYSDBA privilege bypasses database access controls entirely
- Memory dumps from Dropbox links contain password hashes
- Multiple paths to root: pass-the-hash or direct Oracle execution
- Alternative RottenPotato/LonelyPotato exploit possible with SeImpersonatePrivilege
