---
type: machine
title: Vintage
platform: htb
os: windows
difficulty: hard
tags: [ad, bloodhound, gmsa, kerberoasting, dpapi, rbcd, dcsync]
solved: 2026-07-09
sources: [[htb-vintage]]
related: []
---
# Vintage
> Pure Active Directory exploitation starting with low-privilege credentials. Chain involves BloodHound analysis for Pre-Windows 2000 password guessing, GMSA password extraction, targeted Kerberoasting on service accounts, DPAPI credential extraction, and resource-based constrained delegation for domain compromise.

## Attack path
1. [[bloodhound]] — Identify computer object in Pre-Windows 2000 Compatible Access group
2. [[pre-windows-2000-password]] — Guess computer password (lowercase hostname) for authentication
3. [[gmsa-password-read]] — Read GMSA password as Domain Computer member
4. [[targeted-kerberoast]] — Enable service account and Kerberoast to recover password
5. [[password-spray]] — Reuse cracked service password for user access
6. [[dpapi-extraction]] — Extract Windows Credential Manager data using DPAPI
7. [[rbcd]] — Abuse resource-based constrained delegation via computer object
8. [[dcsync]] — DCSync domain as Domain Controller computer account

## Techniques used
- [[bloodhound]] — Identify FS01$ in Pre-Windows 2000 Compatible Access group
- [[pre-windows-2000-password]] — Computer password is lowercase hostname without `$`
- [[gmsa-password-read]] — FS01$ has ReadGMSAPassword on gMSA01$ service account
- [[targeted-kerberoast]] — Add self to ServiceManagers, enable SVC_SQL, Kerberoast with targetedKerberoast.py
- [[password-spray]] — Cracked Kerberos password `Zer0the0ne` works for C.Neri user
- [[dpapi-extraction]] — Extract credential using DPAPI with master key and password
- [[rbcd]] — Add FS01$ to DelegatedAdmins group for RBCD abuse
- [[dcsync]] — Use S4U2self/S4U2proxy as FS01$ impersonating DC01$ for DCSync

## Tools used
- [[nmap]]
- [[netexec]]
- [[bloodhound-ce-python]]
- [[kinit]]
- [[ldapsearch]]
- [[bloodyad]]
- [[targetedKerberoast]]
- [[hashcat]]
- [[evil-winrm]]
- [[dpapi]] (Impacket)
- [[getTGT]]
- [[getST]]
- [[secretsdump]]

## Services / ports
- 53/tcp — [[dns]] — Simple DNS Plus
- 88/tcp — [[kerberos]] — Microsoft Windows Kerberos
- 389/tcp — [[ldap]] — Microsoft Windows Active Directory LDAP
- 445/tcp — [[smb]] — Microsoft-ds
- 5985/tcp — [[http]] — Microsoft HTTPAPI 2.0 (WinRM/WinRS)

## Lessons / notes
- Pre-Windows 2000 Compatible Access members have predictable passwords
- GMSA passwords readable by Domain Computers (and FS01$ specifically)
- NTLM auth disabled, Kerberos required
- DPAPI credential extraction requires master key and user password
- RBCD via AllowedToAct on DelegatedAdmins group
- Administrator account restricted from WinRM logon
- Cleanup script periodically resets changes (account enabling, group membership)

## AD structure
- Domain: vintage.htb
- Domain Controller: DC01
- File Server: FS01.vintage.htb
- Key groups: ServiceManagers, DelegatedAdmins, Domain Admins
- Service accounts: gMSA01$, SVC_SQL, SVC_LDAP, SVC_ARK
