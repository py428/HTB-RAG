---
type: machine
title: DarkZero
platform: htb
os: windows
difficulty: hard
tags: [windows, ad, mssql, adcs, kerberos, relay, insane, privesc, delegation, ntlm, cve, dcsync]
solved: 2026-07-09
sources: [[htb-darkzero]]
related: []
---
# DarkZero

> Hard difficulty Windows AD box with cross-forest trust, starting with MSSQL linked server enumeration and xp_cmdshell exploitation, then multiple privilege escalation paths on DC02 including token impersonation, ADCS abuse, NTLM authentication reflection with CVE-2025-58726, and CVE-2024-30088, finally achieving DCSync for complete domain compromise.

## Attack path

1. [[nmap]] port scan → [[smb]], [[ldap]], [[kerberos]], [[mssql]], and other DC services
2. [[netexec]] enumeration with given credentials → discover linked MSSQL server
3. [[mssqlclient]] → [[xp-cmdshell]] enablement and execution → shell as svc_sql on DC02
4. Multiple privilege escalation paths:
   - [[token-impersonation]] → recover SeImpersonatePrivilege via named pipe → [[godpotato]] → SYSTEM
   - [[adcs]] → certificate enrollment → NT hash recovery → [[runascs]] with full token → SYSTEM  
   - [[ntlm-relay]] with CVE-2025-58726 → create malicious DNS record → coerce authentication → [[ntlmrelayx]] with MIC removal → SYSTEM
   - [[cve-2024-30088]] → Metasploit exploit for SYSTEM
5. Cross-forest TGT delegation → capture DC01 machine account TGT → [[dcsync]] → complete domain compromise

## Techniques used

- [[mssql-linked-servers]] — Enumerated linked server DC02.darkzero.ext with sysadmin mapping for john.w
- [[xp-cmdshell]] — Enable and exploit MSSQL xp_cmdshell for command execution as svc_sql
- [[token-impersonation]] — Recover SeImpersonatePrivilege from original logon token via named pipe impersonation
- [[adcs]] — Certificate enrollment via Rubeus TGT delegation and Certipy for NT hash recovery
- [[runascs]] — Service logon type with full token to spawn process with SeImpersonatePrivilege
- [[ntlm-relay]] — CVE-2025-58726 authentication reflection using CMTI DNS record and modified ntlmrelayx
- [[kerberos-delegation]] — Cross-forest TGT delegation abuse to capture DC01 machine account TGT
- [[dcsync]] — DSRUAPI abuse using DC01 machine account TGT for credential dumping
- [[godpotato]] — SeImpersonatePrivilege abuse for SYSTEM-level code execution

## Tools used

- [[nmap]] — Comprehensive port scanning and service detection
- [[netexec]] — SMB/LDAP enumeration, BloodHound collection, DCsync credential dumping
- [[mssqlclient]] — MSSQL interaction and xp_cmdshell exploitation
- [[rubeus]] — TGT delegation, Kerberos ticket manipulation
- [[certipy]] — ADCS certificate enrollment and authentication
- [[chisel]] — SOCKS proxy tunneling through Linux host
- [[krbrelayx]] — Kerberos relay to ADCS for silver ticket generation
- [[ntlmrelayx]] — Modified Impacket for NTLM relay with MIC removal (CVE-2025-58726)
- [[dnstool]] — DNS record manipulation for CMTI attacks
- [[godpotato]] — Privilege escalation using SeImpersonatePrivilege
- [[runascs]] — Service logon exploitation with full token privileges
- [[psexec]] — Remote service execution for shell access

## Services / ports

- 53/tcp [[dns]] — Simple DNS Plus (DC-01)
- 88/tcp [[kerberos]] — Microsoft Windows Kerberos
- 135/tcp [[msrpc]] — Microsoft Windows RPC
- 139/tcp [[netbios-ssn]] — Microsoft Windows NetBIOS
- 389/tcp [[ldap]] — Microsoft Windows Active Directory LDAP
- 445/tcp [[smb]] — Microsoft Windows SMB
- 464/tcp [[kpasswd]] — Kerberos password changing
- 593/tcp [[ncacn_http]] — Microsoft Windows RPC over HTTP
- 636/tcp [[ldapssl]] — Microsoft Windows Active Directory LDAP over SSL
- 1433/tcp [[mssql]] — Microsoft SQL Server 2022
- 2179/tcp [[vmrdp]] — Hyper-V RDP
- 3268/tcp [[globalcatldap]] — Microsoft Windows Active Directory Global Catalog LDAP
- 3269/tcp [[globalcatldapssl]] — Microsoft Windows Active Directory Global Catalog LDAP over SSL
- 5985/tcp [[winrm]] — Microsoft HTTPAPI httpd 2.0

## Lessons / notes

- Cross-forest trusts provide interesting delegation opportunities for TGT relay attacks
- Multiple privilege escalation paths demonstrate the importance of enumeration and flexibility
- CVE-2025-58726 (NTLM reflection) requires unpatched systems and specific DNS manipulation
- ADCS certificate enrollment via Kerberos relay is a powerful silver ticket generation method
- Token impersonation attacks can recover lost privileges from service logons
- GodPotato provides reliable SeImpersonatePrivilege exploitation when available
- DCSync via cross-forest TGT delegation allows complete credential compromise
- MSSQL linked servers can provide unexpected paths to domain compromise