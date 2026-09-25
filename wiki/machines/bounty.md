---
type: machine
title: Bounty
platform: htb
os: windows
difficulty: easy
tags: [web, file-upload, windows, privesc]
solved: 2026-07-09
sources: [[htb-bounty]]
related: []
---
# Bounty
> Windows IIS server with file upload vulnerability bypassing extension filtering using web.config with embedded ASP code for initial access, then multiple privilege escalation paths including token impersonation and kernel exploits.

## Attack path
1. Discover upload form at /transfer.aspx on IIS 7.5 server
2. Bypass extension filter with null byte technique (shell.aspx%00.jpg)
3. Upload [[web-config-rce]] payload with ASP code in web.config file
4. Get shell as merlin via PowerShell reverse shell in web.config
5. Identify SeImpersonatePrivilege enabled with whoami /priv
6. Exploit with [[lonely-potato]] or kernel exploits (MS10-092, MS16-014) for SYSTEM

## Techniques used
- [[web-config-rce]] — Embed ASP code in web.config for execution on IIS
- [[null-byte-upload-bypass]] — Bypass extension filters with %00.jpg technique
- [[lonely-potato]] — Token impersonation exploit with SeImpersonatePrivilege
- [[kernel-exploit]] — Multiple unpatched vulnerabilities on Windows Server 2008 R2

## Tools used
- [[nmap]], [[gobuster]], [[nishang]], [[mimikatz]], [[watson]], [[sherlock]], [[metasploit]]

## Services / ports
- 80/tcp — [[http]] — Microsoft IIS 7.5 (ASP.NET)

## Lessons / notes
- IIS web.config can execute ASP code if handlers accessPolicy configured
- User.txt hidden as hidden file on Windows desktop, use -Force flag
- No hotfixes installed indicates multiple kernel exploit opportunities
- SeImpersonatePrivilege allows potato family exploits
- Watson C# binary must target .NET Framework 2.0 for older Windows versions
