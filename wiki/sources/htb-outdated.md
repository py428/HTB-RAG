---
type: source
title: "HTB Outdated writeup"
raw: raw/htb-outdated.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[outdated]]
---

# Source: HTB Outdated writeup
> Comprehensive writeup for HackTheBox Outdated machine covering Microsoft Support Diagnostic Tool (Folina) exploitation via email phishing, shadow credentials abuse for lateral movement, and WSUS malicious update deployment for privilege escalation.

## Key facts extracted
- Windows domain controller (overwatch.htb) with multiple services including SMB, LDAP, Kerberos, WinRM, HTTP, SMTP, DNS, and MSSQL
- Anonymous SMB access to software$ share containing .NET monitoring binary (overwatch.exe) with hardcoded SQL credentials
- CVE-2022-30190 (Folina) exploitation requires >4096 byte msdt:// URLs to bypass warning dialogs
- Shadow credentials abuse using Whisker tool to add certificate-based authentication for sflowers account
- WSUS exploitation via SharpWSUS to push malicious PsExec update for SYSTEM execution
- DNS abuse with CREATE_CHILD permissions on AD-integrated DNS zones for effective credential theft
- MSSQL linked server SQL07 configured with stored credentials that expose cleartext authentication
- Multiple authentication paths including NTLM hash-based WinRM access

## Filed into
[[outdated]], [[cve-2022-30190]], [[shadow-credentials]], [[wsus-abuse]], [[smb-null-auth]], [[net-reverse-engineering]], [[dns-abuse]], [[mssql-linked-server]], [[wcf-command-injection]]
