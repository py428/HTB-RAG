---
type: machine
title: Sauna
platform: htb
os: windows
difficulty: easy
tags: [windows, ad, kerberos, privesc, bloodhound]
solved: 2026-07-09
sources: [[htb-sauna]]
related: []
---
# Sauna

> Windows Active Directory domain controller featuring Kerberos username enumeration, AS-REP roasting for initial access, AutoLogon credentials for privilege escalation, and BloodHound-guided DCSync attack for domain compromise.

## Attack path

1. [[kerberos-username-enumeration]] — Identify valid domain users with kerbrute
2. [[as-rep-roasting]] — Get and crack fsmith hash via AS-REP roasting
3. [[ldap-description-credential]] — Find svc_loanmgr credentials in AutoLogon registry
4. [[dcsync]] — Use BloodHound to identify DCSync privileges and dump NTDS

## Techniques used

- [[kerberos-username-enumeration]] — Kerbrute user enumeration against domain EGOTISTICAL-BANK.LOCAL
- [[as-rep-roasting]] — GetNPUsers.py to request hash for user with UF_DONT_REQUIRE_PREAUTH set
- [[ldap-description-credential]] — WinPEAS reveals AutoLogon credentials in registry
- [[bloodhound]] — SharpHound enumeration and analysis to find DCSync privileges
- [[dcsync]] — secretsdump.py to replicate domain controller and extract all hashes

## Tools used

- [[nmap]] — Port scanning identifying Active Directory services
- [[kerbrute]] — Kerberos username enumeration
- GetNPUsers.py — AS-REP roasting hash extraction
- [[hashcat]] — Password cracking with rockyou wordlist
- [[evil-winrm]] — Windows remote shell access
- WinPEAS — Windows privilege escalation enumeration
- [[bloodhound]] — AD privilege analysis
- SharpHound.exe — BloodHound data collection
- [[impacket]] — secretsdump.py for DCSync attack
- [[mimikatz]] — Alternative DCSync implementation

## Services / ports

- [[dns]] — 53/tcp
- [[http]] — 80/tcp — IIS 10.0
- [[kerberos]] — 88/tcp
- [[ldap]] — 389/tcp
- [[smb]] — 445/tcp
- [[kpasswd]] — 464/tcp
- [[ldap]] — 3268/tcp — Global Catalog LDAP

## Lessons / notes

- Domain name: EGOTISTICAL-BANK.LOCAL
- AS-REP roasting works on fsmith@EGOTISTICAL-BANK.LOCAL
- Password cracked: `Thestrokes23`
- AutoLogon credentials: svc_loanmgr / `Moneymakestheworldgoround!`
- BloodHound shows svc_loanmgr has GetChanges/GetChangesAll privileges on domain
- DCSync provides all domain hashes including administrator
- Administrator NTLM hash: `d9485863c1e9e05851aa40cbb4ab9dff`
- Multiple shell options: evil-winrm, psexec, wmiexec with hash authentication
