---
type: machine
title: Multimaster
platform: htb
os: windows
difficulty: insane
tags: [windows, ad, sqli, privesc, hard]
solved: 2026-07-09
sources: [[htb-multimaster]]
related: []
---
# Multimaster
> Insane-difficulty Windows Active Directory box featuring SQL injection bypass, CEF debugging exploitation, complex AD privilege escalation chains, and multiple paths to SYSTEM.

## Attack path
1. Identify and bypass WAF to exploit [[sqli]] in colleague finder
2. Dump database and crack hashes to obtain credentials
3. Use MSSQL to enumerate domain users via `SUSER_SNAME`
4. Authenticate via [[winrm]] to gain initial foothold
5. Exploit CEF debug socket in Visual Studio Code for [[cef-debugging]]
6. Find database credentials in custom DLL and pivot to second user
7. Use [[bloodhound]] to identify ACL-based privilege escalation path
8. Enable [[as-rep-roasting]] and crack hash to get third user
9. Exploit [[server-operators]] membership to modify service and gain SYSTEM
10. Alternative path: Use [[zerologon]] or [[backup-privileges]]

## Techniques used
- [[waf-bypass]] — Unicode encoding to bypass SQL injection filtering
- [[sqli]] — SQL injection in colleague finder with unicode evasion
- [[mssql-enumeration]] — Use MSSQL `SUSER_SNAME` function to enumerate domain users
- [[cef-debugging]] — Exploit open Chrome DevTools Protocol socket in VS Code
- [[dll-analysis]] — Extract database connection string from .NET assembly
- [[acl-genericwrite]] — GenericWrite on jorden user to modify userAccountControl
- [[as-rep-roasting]] — Enable DONT_REQ_PREAUTH flag and crack AS-REP hash
- [[service-permission-abuse]] — Server Operators can modify service binPath for SYSTEM

## Tools used
[[nmap]], [[wfuzz]], [[sqlmap]], [[hashcat]], [[crackmapexec]], [[evil-winrm]], [[cefdebug]], [[bloodhound]], [[RunasCs]]

## Services / ports
[[smb]] (445), [[ldap]] (389), [[kerberos]] (88), [[winrm]] (5985), [[http]] (80), [[mssql]] (1433)

## Lessons / notes
- WAF blocked common SQL injection characters but allowed unicode-encoded payloads
- Domain users could be enumerated via MSSQL by building SIDs and calling `SUSER_SNAME`
- CEF debugging sockets in VS Code can allow code execution as the running user
- Custom .NET DLLs may contain hardcoded credentials in connection strings
- GenericWrite on user account allows enabling AS-REP roasting by flipping userAccountControl bit 4194304
- Server Operators group has extensive service manipulation privileges on domain controllers
- Multiple unintended paths available including NTLM relay and ZeroLogon