---
type: machine
title: Blazorized
platform: htb
os: windows
difficulty: hard
tags: [ad, windows, web, privesc, dotnet, blazor]
solved: 2026-07-09
sources: [[htb-blazorized]]
related: []
---
# Blazorized
> Blazor.NET application exploitation box featuring DLL reverse engineering, JWT secret extraction, SQL injection, targeted Kerberoasting, and logon script abuse. Attack path: extract JWT secret from Blazorized.Helper.dll, forge admin JWT, SQL injection for RCE, targeted Kerberoast via WriteSPN privilege, abuse logon script permissions with BloodHound-enumerated ACLs, DCSync for domain compromise.

## Attack path
1. [[dll-reverse-engineering]] — Extract JWT signing key from Blazorized.Helper.dll
2. [[jwt-forgery]] — Forge Super_Admin JWT for admin panel access  
3. [[sqli]] — SQL injection in duplicate check form for xp_cmdshell RCE
4. [[targeted-kerberoast]] — Assign SPN to RSA_4810 via WriteSPN privilege, kerberoast for hash
5. [[acl-abuse]] — Abuse WriteProperty on ScriptPath attribute to plant logon script
6. [[logon-script-abuse]] — Set reverse shell as SSA_6010 logon script for automatic execution
7. [[dcsync]] — Use Mimikatz DCSync as SSA_6010 with GetChangesAll permission

## Techniques used
- [[dll-reverse-engineering]] — Reverse engineer .NET DLL with DotPeek to extract hardcoded secrets
- [[jwt-forgery]] — Forge HS512 JWT tokens using extracted symmetric key
- [[sqli]] — Stack-based SQL injection enabling xp_cmdshell for command execution
- [[targeted-kerberoast]] — Assign SPN to user account and kerberoast to crack password
- [[acl-abuse]] — Abuse WriteProperty on AD object attributes like ScriptPath
- [[logon-script-abuse]] — Plant malicious logon scripts that execute on user login
- [[dcsync]] — Use DCSync privileges to dump all domain password hashes

## Tools used
[[nmap]], ffuf, netexec, feroxbuster, DotPeek, Python jwt library, PowerView, PowerSploit, hashcat, accesschk, mimikatz, evil-winrm

## Services / ports
[[dns]] (53), [[kerberos]] (88), [[ldap]] (389), [[smb]] (445), [[http]] (80), MSSQL (1433), [[winrm]] (5985)

## Lessons / notes
- Blazor WebAssembly sends DLLs to browser for client-side execution, allowing reverse engineering
- Hardcoded secrets in compiled assemblies can be extracted for authentication bypass
- SQL injection in web applications can lead to RCE via xp_cmdshell on MSSQL
- BloodHound effective for identifying ACL-based privilege escalation like WriteSPN and WriteProperty
- Targeted Kerberoasting possible by assigning SPN to accounts without existing service tickets
- Logon scripts stored in SYSVOL scripts directory execute automatically on user login
- GetChangesAll permission enables DCSync attacks for complete domain compromise
- Multiple valid privilege escalation paths from different users showing layered security model
