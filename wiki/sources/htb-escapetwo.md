---
type: source
title: "HTB EscapeTwo writeup"
raw: raw/htb-escapetwo.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[escapetwo]]
---
# Source: HTB EscapeTwo writeup

> Detailed walkthrough of EscapeTwo Windows domain controller box covering Excel file analysis, MSSQL exploitation, Active Directory privilege escalation through ACL abuse, and ADCS ESC4 template hijacking.

## Key facts extracted
- Initial credentials: rose / KxEPkKe6R8su (assume breach scenario)
- Excel files on SMB share contain embedded credentials (including sa: MSSQLP@ssw0rd!)
- MSSQL sa access enables xp_cmdshell for command execution as sql_svc
- Password reuse (WqSZAF6CysDQbGb3) grants access to ryan user via WinRM
- BloodHound reveals WriteOwner privilege on ca_svc for ryan
- Shadow credentials + ESC4 abuse yields Administrator access
- Domain: sequel.htb, DC: DC01

## Filed into
[[escapetwo]], [[mssql-xp-cmdshell]], [[shadow-credentials]], [[adcs-template-abuse]], [[acl-genericall]]
