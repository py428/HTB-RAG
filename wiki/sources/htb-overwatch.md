---
type: source
title: "HTB Overwatch writeup"
raw: raw/htb-overwatch.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[overwatch]]
---

# Source: HTB Overwatch writeup
> In-depth writeup for HackTheBox Overwatch machine covering anonymous SMB access, .NET reverse engineering, DNS abuse for credential theft, linked server exploitation, and WCF service command injection for privilege escalation.

## Key facts extracted
- Windows domain controller (overwatch.htb) with comprehensive services including SMB, LDAP, Kerberos, WinRM, HTTP, DNS, and MSSQL
- Anonymous SMB access to software$ share with .NET monitoring binary containing SQL credentials
- DNS abuse using CREATE_CHILD permissions on AD-integrated zones for effective credential phishing
- MSSQL linked server SQL07 with stored credentials exposing cleartext authentication
- WCF monitoring service with PowerShell command injection vulnerability in KillProcess function
- Multiple authentication methods including NTLM hash-based WinRM access
- Complex Active Directory environment with multiple users and services
- Credential theft and abuse patterns demonstrating common Windows AD exploitation techniques

## Filed into
[[overwatch]], [[smb-null-auth]], [[net-reverse-engineering]], [[dns-abuse]], [[mssql-clear-text]], [[mssql-linked-server]], [[wcf-command-injection]]
