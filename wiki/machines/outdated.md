---
type: machine
title: Outdated
platform: htb
os: windows
difficulty: medium
tags: [windows, ad, web, rce, privesc, wsus]
solved: 2026-07-09
sources: [[htb-outdated]]
related: []

# Outdated
> Windows domain controller exploiting Microsoft Support Diagnostic Tool (Folina) via email phishing, followed by shadow credentials abuse for lateral movement, and WSUS malicious update for SYSTEM shell.

## Attack path
1. [[smb-null-auth]] to access software share and extract [[net-reverse-engineering]] targets
2. [[cve-2022-30190]] (Folina) exploitation via email phishing to gain initial [[web-rce]] as btables
3. [[shadow-credentials]] abuse using [[whisker]] to compromise sflowers account
4. [[winrm]] authentication as sflowers in [[remote-management-users]] group
5. [[wsus-abuse]] via SharpWSUS to push malicious [[ps-exec]] update for SYSTEM shell

## Techniques used
- [[smb-null-auth]] — Anonymous SMB access to software share containing .NET monitoring binary with hardcoded SQL credentials
- [[net-reverse-engineering]] — Reverse engineer .NET binary (overwatch.exe) to extract SQL Server credentials and identify WCF service with PowerShell command injection sink
- [[cve-2022-30190]] — Microsoft Support Diagnostic Tool (Folina) RCE via msdt:// URL protocol in email, bypassing warnings with >4096 byte payloads
- [[shadow-credentials]] — Abuse KeyCredentialLink (msDS-KeyCredentialLink) with Whisker to create certificate-based authentication for sflowers account
- [[winrm]] — Remote shell access using NTLM hash of sflowers account
- [[wsus-abuse]] — Exploit WSUS (Windows Server Update Services) by creating malicious update with PsExec payload, approving for DC execution
- [[dns-abuse]] — Create DNS records using CREATE_CHILD permissions on AD-integrated DNS zones via bloodyAD
- [[mssql-linked-server]] — Abuse MSSQL linked server SQL07 to capture cleartext SQL authentication credentials with Responder

## Tools used
- [[nmap]] — Port scanning and service enumeration
- [[smbclient]] — Anonymous SMB share access to download files
- [[crackmapexec]] — SMB authentication and share enumeration
- [[bloodhound]] — AD mapping and attack path analysis
- [[swaks]] — Email submission for Folina exploitation
- [[nc]] — Netcat for reverse shell handling
- [[impacket]] — Responder for NTLM relay attacks
- [[evil-winrm]] — WinRM shell access using NTLM hash
- [[whisker]] — Shadow credentials exploitation tool
- [[rubeus]] — Kerberos ticket manipulation and TGT request
- [[certipy]] — Python alternative for shadow credentials (not used in main path)
- [[hashcat]] — Password cracking for PBKDF2 hashes
- [[netexec]] — SMB and MSSQL authentication testing
- [[bloodyAD]] — DNS record creation and ACL enumeration
- [[mssqlclient]] — MSSQL interaction and linked server enumeration
- [[python]] — Payload generation and scripting
- [[ssh]] — SSH access for pivoting

## Services / ports
- [[smb]] (445) — Anonymous access to software$ share
- [[ldap]] (389, 636, 3268, 3269) — Active Directory LDAP services
- [[kerberos]] (88, 464) — Kerberos authentication
- [[winrm]] (5985) — Windows Remote Management
- [[http]] (80, 8530, 8531) — Web services and WSUS
- [[smtp]] (25, 587) — Email services for phishing
- [[dns]] (53) — DNS server
- [[mssql]] (6520) — Microsoft SQL Server 2022

## Lessons / notes
- Folina exploitation requires >4096 byte msdt:// URLs to bypass warning dialogs
- Shadow credentials provide powerful persistence and lateral movement in AD environments
- WSUS abuse allows SYSTEM-level code execution on domain-joined systems
- DNS CREATE_CHILD permissions enable effective phishing and credential theft
- Linked servers with stored credentials expose cleartext authentication when forced to connect to attacker-controlled hosts
- Container environments (Hyper-V) may have different IP addressing and require pivoting techniques
