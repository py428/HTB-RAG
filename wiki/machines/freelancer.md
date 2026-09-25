---
type: machine
title: Freelancer
platform: htb
os: windows
difficulty: hard
tags: [windows, ad, web, mssql, rce, memory-analysis, delegation]
solved: 2026-07-09
sources: [[htb-freelancer]]
related: []
---
# Freelancer
> Freelancer is a hard Active Directory box involving Django website exploitation, MSSQL impersonation for RCE, memory dump analysis with MemProcFS to extract credentials, and resource-based constrained delegation to compromise the domain controller.

## Attack path
1. [[idor]] in QR-code login to access admin account  
2. MSSQL impersonation to enable [[xp-cmdshell]] and get RCE
3. Extract MSSQL credentials from configuration files
4. Password spray to find mikasaAckerman credentials
5. Extract memory dump and analyze with [[memprocfs]]
6. Find LSA secrets for lorra199 user
7. Use [[bloodhound]] to identify delegation privileges
8. [[rbcd-exploit]] to get DC hash and administrator access

## Techniques used
- [[idor]] — Insecure direct object reference in QR-code login tokens
- [[mssql-impersonation]] — Using EXECUTE AS to impersonate sa user
- [[xp-cmdshell]] — Enabling and abusing xp_cmdshell for command execution
- [[memory-analysis]] — Analyzing Windows memory dump with MemProcFS
- [[lsa-secrets]] — Extracting credentials from LSA secrets in memory dump
- [[rbcd-exploit]] — Resource-based constrained delegation to compromise DC
- [[password-spray]] — Testing found passwords against multiple users

## Tools used
[[nmap]], [[netexec]], [[ffuf]], [[feroxbuster]], [[zbarimg]], python, RunasCs, [[smbclient]], MemProcFS, [[bloodhound]], certipy, evil-winrm

## Services / ports
- 53/tcp — dns
- 80/tcp — [[http]] (nginx)
- 88/tcp — [[kerberos]]
- 135/tcp — msrpc
- 139/tcp — [[netbios-ssn]]
- 389/tcp — [[ldap]]
- 445/tcp — [[smb]]
- 636/tcp — ldaps
- 3268/tcp — [[ldap]] (Global Catalog)
- 3269/tcp — ldaps (Global Catalog)
- 5985/tcp — [[winrm]]
- 9389/tcp — .NET Message Framing
- 47001/tcp — [[winrm]]
- 55297/tcp — mssql

## Lessons / notes
- Django debug page leaked critical user ID information
- MSSQL impersonation chain: webapp user → sa → xp_cmdshell
- Memory dumps contain valuable credential information in LSA secrets
- RBCD is a powerful AD exploitation technique for DC compromise
- The intended path used memory analysis instead of credential spraying

## Alternative paths
- WinDbg with Mimikatz plugin on memory dump to extract credentials
- Password spraying variations found multiple valid user credentials
