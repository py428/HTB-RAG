---
type: source
title: "HTB Redelegate writeup"
raw: raw/htb-redelegate.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[redelegate]]
---
# Source: HTB Redelegate writeup
> Domain compromise via anonymous FTP, KeePass cracking, MSSQL enumeration, HelpDesk ACL abuse, and constrained delegation for DCSync.

## Key facts extracted
- Anonymous FTP provided CyberAudit.txt, TrainingAgenda.txt with password hints, and Shared.kdbx
- KeePass database cracked with Fall2024! from seasonal password pattern
- MSSQL SQLGuest access enabled domain user enumeration via SUSER_SNAME RID cycling
- Marie.Curie in Helpdesk group had ForceChangePassword privilege over Helen.Frost
- Helen.Frost had SeEnableDelegationPrivilege used to configure FS01$ for delegation
- Constrained delegation S4U2Proxy abuse allowed DC impersonation and DCSync

## Filed into
[[redelegate]], [[ftp-anonymous]], [[keepass-crack]], [[mssql-enumeration]], [[password-spray]], [[acl-forcechange-password]], [[constrained-delegation]], [[dcsync]]