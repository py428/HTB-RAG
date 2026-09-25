---
type: machine
title: Cicada
platform: htb
os: windows
difficulty: easy
tags: [windows, ad, ldap, smb, winrm, ad-privesc]
solved: 2026-07-09
sources: [[htb-cicada]]
related: []
---
# Cicada
> Easy Windows Active Directory box with anonymous SMB access revealing default password, RID cycling for user enumeration, LDAP password discovery, and Backup Operators abuse for domain controller hash dumping.

## Attack path
1. [[smb]] anonymous access finds HR share with default password
2. [[rid-cycling]] via netexec enumerates domain users
3. [[password-spray]] default password to find michael.wrightson
4. [[ldap]] query finds david.orelious password in description field
5. [[smb]] DEV share access reveals emily.oscars credentials in backup script
6. [[winrm]] shell as emily.oscars with Backup Operators privileges
7. Dump registry hives and extract Administrator hash with [[sebackupprivilege]]

## Techniques used
- [[password-spray]] — Default password from HR notice across enumerated users
- [[rid-cycling]] — SMB RID brute force for user enumeration
- [[ldap-description-credential]] — Password stored in LDAP user description attribute
- [[sebackupprivilege]] — Backup Operators privilege to exfiltrate registry hives
- [[dcsync]] — Domain hash dumping via NTDS (Beyond Root)

## Tools used
[[nmap]], [[netexec]], smbclient, evil-winrm, [[secretsdump]], robocopy

## Services / ports
- TCP 53 — DNS
- TCP 88 — Kerberos
- TCP 135 — RPC
- TCP 139/445 — SMB
- TCP 389/636/3268/3269 — LDAP/LDAPS
- TCP 5985 — WinRM

## Lessons / notes
- Default passwords often work for at least one user in organizations
- RID cycling provides complete user enumeration without credentials
- LDAP description fields sometimes contain credentials
- Backup Operators can dump local and domain hashes via registry/NTDS
- Multiple methods for NTDS extraction: diskshadow, robocopy, ntdsutil

## CVEs
None
