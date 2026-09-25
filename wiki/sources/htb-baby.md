---
type: source
title: "HTB Baby writeup"
raw: raw/htb-baby.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[baby]]
---
# Source: HTB Baby writeup
> Step-by-step exploitation of a Windows domain controller using anonymous LDAP enumeration, password spraying, and Backup Operator privilege abuse.

## Key facts extracted
- Anonymous LDAP binding enabled revealing all domain users and attributes
- Service account found with default password matching username pattern
- Multiple user accounts vulnerable to password reuse
- Backup Operators group membership provides SeBackupPrivilege
- Local Administrator hash accessible via backup privileges
- Domain Administrator credentials obtainable through local hash dumping

## Filed into
[[baby]], [[ldap-enumeration]], [[password-spray]], [[backup-operator-abuse]], [[credential-dumping]], [[pth]]
