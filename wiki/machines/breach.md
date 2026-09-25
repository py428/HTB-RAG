---
type: machine
title: Breach
platform: htb
os: windows
difficulty: medium
tags: [ad, windows, web, privesc]
solved: 2026-07-09
sources: [[htb-breach]]
related: []
---
# Breach
> Windows domain controller featuring NTLM theft via SMB lure files, Kerberoasting, Silver Ticket forgery for MSSQL access, and GodPotato privilege escalation.
## Attack path
1. [[ntlm-theft]] — Drop lure files on writable SMB share to capture NetNTLMv2 hash
2. [[kerberoasting]] — Crack Kerberoastable service account hash with BloodHound enumeration
3. [[silver-ticket]] — Forge MSSQL service ticket as Administrator using svc_mssql NTLM hash
4. [[mssql-xp-cmdshell]] — Enable xp_cmdshell for command execution as svc_mssql
5. [[godpotato]] — Escalate to SYSTEM using SeImpersonatePrivilege abuse
## Techniques used
- [[ntlm-theft]] — SMB share write access with ntlm_theft lure files triggering authentication
- [[kerberoasting]] — BloodHound identifies Kerberoastable MSSQL service account
- [[silver-ticket]] — Forge TGS for MSSQLSvc/spn using service account NT hash
- [[mssql-xp-cmdshell]] — Enable and abuse xp_cmdshell for system command execution
- [[godpotato]] — SeImpersonatePrivilege abuse to escalate to SYSTEM
## Tools used
- [[nmap]] — Full port scan and service enumeration
- [[netexec]] — SMB enumeration, RID brute force, and Kerberoasting
- smbclient — SMB share access and file operations
- responder — Capture NetNTLMv2 hashes from SMB authentication
- [[hashcat]] — Crack NetNTLMv2 and Kerberoast hashes
- bloodhound — AD enumeration and privilege escalation path analysis
- rusthound-ce — BloodHound data collection
- [[mssqlclient.py]] (impacket) — MSSQL interaction and xp_cmdshell abuse
- ticketer.py (impacket) — Silver ticket generation
- godpotato — Privilege escalation via COM/DCOM exploitation
## Services / ports
- [[smb]] (445) — Writable share for lure file placement
- [[ldap]] (389/3268/636) — AD enumeration and BloodHound data collection
- [[kerberos]] (88/464) — Kerberoasting and Silver Ticket operations
- [[mssql]] (1433) — SQL Server with xp_cmdshell for RCE
- [[http]] (80) — IIS default page, no exploitation
- [[winrm]] (5985) — Available but not used for shell access
## Lessons / notes
- Writable SMB shares provide excellent NTLM theft opportunities with lure files
- BloodHound is essential for identifying Kerberoastable service accounts
- Silver Tickets are powerful for service-specific access when you have the service account hash
- MSSQL sysadmin privileges enable xp_cmdshell for command execution
- GodPotato exploits SeImpersonatePrivilege which is common for service accounts