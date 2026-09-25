---
type: source
title: "HTB Signed writeup"
raw: raw/htb-signed.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[signed]]
---
# Source: HTB Signed writeup
> Comprehensive MSSQL exploitation guide covering NTLM coercion, silver ticket forgeries, and three privilege escalation paths.
## Key facts extracted
- Initial creds: scott / Sm230#C5NatH (local MSSQL auth)
- Cracked mssqlsvc password: purPLE9795!@
- IT group RID: 1105 (has sysadmin on MSSQL)
- Administrator password found in PowerShell history: Th1s889Rabb!t
- mssqlsvc has GenericAll over DNS zone
- SeImpersonatePrivilege removed from MSSQLSERVER service
## Filed into
[[signed]], [[ntlm-coercion]], [[silver-ticket]], [[openrowset-bulk]], [[ntlm-relay]], [[mssql-command-execution]], [[acl-genericall]]
