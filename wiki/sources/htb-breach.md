---
type: source
title: "HTB Breach writeup"
raw: raw/htb-breach.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[breach]]
---
# Source: HTB Breach writeup
> Windows domain controller featuring NTLM theft via SMB lure files, Kerberoasting, Silver Ticket forgery for MSSQL access, and GodPotato privilege escalation.
## Key facts extracted
- Guest access to writable SMB share (share/transfer/) for NTLM theft
- Julia.Wong NetNTLMv2 hash cracked: "Computer1"
- svc_mssql Kerberoastable service account cracked: "Trustno1"  
- Silver ticket forged for MSSQLSvc/breachdc.breach.vl:1433 as Administrator
- Domain SID: S-1-5-21-2330692793-3312915120-706255856
- User flag in non-standard location: C:\share\transfer\julia.wong\user.txt
## Filed into
[[breach]], [[ntlm-theft]], [[kerberoasting]], [[silver-ticket]], [[mssql-xp-cmdshell]], [[godpotato]]