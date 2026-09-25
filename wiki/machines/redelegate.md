---
type: machine
title: Redelegate
platform: htb
os: windows
difficulty: hard
tags: [windows, ad, kerberos, ftp, delegation, acl]
solved: 2026-07-09
sources: [[htb-redelegate]]
related: []
---
# Redelegate
> Active Directory box starting with anonymous FTP access, KeePass cracking, MSSQL enumeration, password spraying, and delegation abuse for domain compromise.

## Attack path
1. Access anonymous [[ftp]] to download audit files and KeePass database
2. Crack KeePass with seasonal password pattern to get SQLGuest credentials
3. Enumerate domain users via MSSQL RID cycling and password spray for Marie.Curie
4. Use [[acl-forcechange-password]] as Helpdesk member to reset Helen.Frost
5. Abuse [[seenabledelegationprivilege]] to configure constrained delegation on FS01$
6. Perform [[constrained-delegation]] S4U2Proxy attack to impersonate DC and [[dcsync]]

## Techniques used
- [[ftp-anonymous]] — Anonymous FTP access provided files and KeePass database
- [[keepass-crack]] — Cracked with seasonal passwords (Fall2024!) using hint from training agenda
- [[mssql-enumeration]] — Used SUSER_SNAME RID cycling to enumerate domain users via SQLGuest
- [[password-spray]] — Tested seasonal passwords against enumerated users
- [[acl-forcechange-password]] — Helpdesk group member could reset other user passwords
- [[constrained-delegation]] — Used SeEnableDelegationPrivilege to configure FS01$ with TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION

## Tools used
[[nmap]], [[ftp]], [[keepassxc-cli]], [[hashcat]], [[netexec]], [[impacket]], [[bloodhound]], [[certipy]], [[evil-winrm]]

## Services / ports
[[ftp]] (21), [[dns]] (53), [[http]] (80), [[kerberos]] (88), [[ldap]] (389), [[smb]] (445), [[mssql]] (1433), [[winrm]] (5985)

## Lessons / notes
- TrainingAgenda.txt hint about "SeasonYear!" password pattern was critical for KeePass crack
- MSSQL RID cycling provides alternative to LDAP for user enumeration when limited access
- SeEnableDelegationPrivilege allows configuring delegation on computer objects
- Constrained delegation with S4U2Proxy can impersonate any user to configured SPNs
- MachineAccountQuota of 0 prevented standard computer account creation attacks