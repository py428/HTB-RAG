---
type: machine
title: Signed
platform: htb
os: windows
difficulty: medium
tags: [windows, ad, kerberos, privesc]
solved: 2026-07-09
sources: [[htb-signed]]
related: []
---
# Signed
> MSSQL server assume breach scenario with NTLM hash coercion, silver ticket forgeries, and multiple privilege escalation paths including OPENROWSET BULK, NTLM relay, and SeImpersonate restoration.
## Attack path
1. [[ntlm-coercion]] → Coerce authentication from MSSQL service via xp_dirtree → Capture NetNTLMv2 hash
2. [[hash-cracking]] → Crack mssqlsvc NetNTLMv2 hash → Service account password (purPLE9795!@)
3. [[silver-ticket]] → Forge silver ticket with IT group RID (1105) → sysadmin on MSSQL
4. [[mssql-command-execution]] → Enable xp_cmdshell → Command execution as mssqlsvc
5. [[openrowset-bulk]] → Read Administrator PowerShell history via OPENROWSET BULK → Find Administrator password
6. [[winrm]] → WinRM access as Administrator → Or: [[ntlm-relay]] via crafted DNS record → WinRM shell
## Techniques used
- [[ntlm-coercion]] — Using xp_dirtree in MSSQL to force SMB authentication and capture NetNTLMv2 hash
- [[silver-ticket]] — Forging Kerberos service tickets with custom group memberships
- [[openrowset-bulk]] — MSSQL OPENROWSET with BULK keyword impersonates ticket groups for file access
- [[ntlm-relay]] — Relay DC authentication via crafted DNS record to WinRM for shell
- [[acl-genericall]] — mssqlsvc has GenericAll over DNS zone for record manipulation
## Tools used
[[nmap]], [[netexec]], [[hashcat]], [[impacket]], [[mssqlclient]], [[responder]], [[ntlmrelayx]], [[chisel]], [[evil-winrm]]
## Services / ports
- [[mssql]] (1433) - Microsoft SQL Server 2022
## Lessons / notes
- MSSQL service accounts often run with high privileges that can be abused
- Silver tickets with forged group memberships enable operations beyond normal user access
- OPENROWSET BULK uses ticket groups for file access even when spawned process doesn't
- DNS records with empty CREDENTIAL_TARGET_INFORMATION structures enable relay attacks
- Multiple privesc paths available: OPENROWSET, NTLM relay, SeImpersonate restoration
