---
type: source
title: "HTB Cicada writeup"
raw: raw/htb-cicada.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[cicada]]
---
# Source: HTB Cicada writeup
> Pure Active Directory easy box demonstrating password spraying, LDAP enumeration, credential discovery, and Backup Operators privilege escalation for domain controller compromise.

## Key facts extracted
- Anonymous SMB access to HR share reveals default password
- RID cycling (netexec --rid-brute) enumerates all domain users
- michael.wrightson still using default Cicada$M6Corpb*@Lp#nZp!8 password
- david.orelious password in LDAP description: aRt$Lp#7t*VQ!3
- DEV share contains backup script with emily.oscars credentials
- emily.oscars in Backup Operators with SeBackupPrivilege
- Domain hashes extractable via diskshadow or NTDSutil

## Filed into
[[cicada]], [[password-spray]], [[rid-cycling]], [[ldap-description-credential]], [[sebackupprivilege]]
