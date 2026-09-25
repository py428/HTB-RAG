---
type: machine
title: "HTB Querier"
platform: htb
os: windows
difficulty: medium
tags: [windows, ad, mssql, smb, privesc]
solved: 2026-07-09
sources: [[htb-querier]]
related: []
---

# HTB Querier

> Querier was a fun medium box that involved some simple document forensics, MSSQL access, responder, and some very basic Windows privesc steps. I'll show how to grab the Excel macro-enabled workbook from an open SMB share, and find database credentials in the macros. I'll use those credentials to connect to the host's MSSQL as a limited user. I can use that limited access to get a Net-NTLMv2 hash with responder, which provides enough database access to run commands. That's enough to provide a shell. For privesc, running PowerUp.ps1 provides administrator credentials from a GPP file.

## Attack path

1. [[rpc-null-session]] enumeration to find open SMB share
2. [[smb]] file download from Reports share
3. [[credential-extraction]] from Excel VBA macro source code
4. [[ntlm-relay]] via xp_dirtree MSSQL command to capture Net-NTLMv2 hash
5. [[hash-cracking]] Net-NTLMv2 hash with hashcat
6. [[mssql-xp-cmdshell]] for command execution as mssql-svc
7. [[gpp-cpassword]] extraction from Groups.xml file
8. [[password-reuse]] for Administrator access

## Techniques used

- [[rpc-null-session]] — smbclient with -N flag allows anonymous SMB session enumeration
- [[smb]] — Accessing open Reports share using smbclient to download Excel file
- [[credential-extraction]] — Extracting MSSQL credentials from VBA macro code in .xlsm file using olevba
- [[ntlm-relay]] — Using xp_dirtree with UNC path to trigger NTLM authentication to responder
- [[hash-cracking]] — Cracking Net-NTLMv2 hash (mode 5600) with hashcat and rockyou.txt
- [[mssql-xp-cmdshell]] — Enabling and using xp_cmdshell for command execution via mssqlclient.py
- [[gpp-cpassword]] — Extracting plaintext Administrator password from cached GPP Groups.xml file
- [[password-reuse]] — Using discovered Administrator credentials for system access

## Tools used

- [[nmap]], [[smbclient]], [[olevba]], [[mssqlclient]], [[responder]], [[hashcat]], [[wmiexec]], [[powershell]]

## Services / ports

- [[smb]] (135/139/445) — Windows file sharing with open Reports share
- [[mssql]] (1433) — Microsoft SQL Server 2017
- [[winrm]] (5985) — Windows Remote Management
- [[rpc]] (135) — Windows RPC services

## Lessons / notes

- Anonymous SMB sessions can sometimes enumerate shares when authenticated access fails
- Excel .xlsm files contain VBA macros that may store hardcoded credentials
- MSSQL xp_dirtree can be abused for NTLM relay attacks even with limited database permissions
- Net-NTLMv2 hashes can be cracked relatively quickly compared to NTLM hashes
- PowerUp.ps1 is excellent for Windows privilege escalation enumeration
- GPP cpassword is a classic AD misconfiguration that stores encrypted passwords
- The Groups.xml file location is predictable: C:\ProgramData\Microsoft\Group Policy\History\{GUID}\Machine\Preferences\Groups\

## CVEs / exploits

- GPP cpassword vulnerability (MS14-025) - AES-256 key publicly disclosed
