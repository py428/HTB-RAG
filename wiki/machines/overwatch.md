---
type: machine
title: Overwatch
platform: htb
os: windows
difficulty: medium
tags: [windows, ad, smb, net-reverse-engineering, dns, mssql, wcf, rce, privesc]
solved: 2026-07-09
sources: [[htb-overwatch]]
related: []

# Overwatch
> Windows domain controller featuring anonymous SMB access, .NET reverse engineering, DNS abuse for credential theft, and WCF service exploitation for privilege escalation.

## Attack path
1. [[smb-null-auth]] to access software$ share and extract monitoring binary
2. [[net-reverse-engineering]] of .NET binary to extract SQL credentials and identify WCF vulnerability
3. [[dns-abuse]] using CREATE_CHILD permissions on AD-integrated DNS zones to capture linked server credentials
4. [[mssql-clear-text]] credentials capture from linked server authentication attempt with [[responder]]
5. [[winrm]] access as sqlmgmt in Remote Management Users group
6. [[wcf-command-injection]] in MonitorService KillProcess function for SYSTEM shell

## Techniques used
- [[smb-null-auth]] — Anonymous SMB access to software$ share with monitoring binary
- [[net-reverse-engineering]] — Reverse engineer .NET binary to extract hardcoded SQL credentials and identify WCF service vulnerability
- [[dns-abuse]] — Create DNS records using CREATE_CHILD permissions on AD-integrated DNS zones to redirect linked server
- [[mssql-clear-text]] — Capture cleartext SQL authentication from linked server using Responder when SQL07 attempts connection
- [[mssql-linked-server]] — Abused SQL07 linked server configuration to force outbound connection and capture credentials
- [[winrm]] — Remote shell access using NTLM hash of sqlmgmt account
- [[wcf-command-injection]] — PowerShell command injection in KillProcess function via SOAP endpoint
- [[group-abuse]] — Add sqlmgmt to Administrators group via command injection

## Tools used
- [[nmap]] — Port scanning and service enumeration
- [[netexec]] — SMB authentication and share enumeration
- [[spider_plus]] — SMB file download automation
- [[dnstop]] — .NET binary decompilation and analysis
- [[bloodyAD]] — DNS record creation and ACL enumeration
- [[mssqlclient]] — MSSQL interaction and linked server testing
- [[responder]] — NTLM relay and credential capture
- [[evil-winrm]] — WinRM shell access and command execution
- [[python]] — SOAP payload generation and automation
- [[powershell]] — Command execution and privilege escalation
- [[curl]] — HTTP client for WCF service interaction
- [[secretsdump]] — NTDS credential dumping (optional path)

## Services / ports
- [[smb]] (445) — Anonymous access to software$ share
- [[ldap]] (389, 636, 3268, 3269) — Active Directory LDAP services
- [[kerberos]] (88, 464) — Kerberos authentication
- [[dns]] (53) — DNS server with AD-integrated zones
- [[http]] (8000, 5985, 6520) — WCF monitoring service, WinRM, MSSQL
- [[winrm]] (5985) — Windows Remote Management
- [[mssql]] (6520) — Microsoft SQL Server 2022

## Lessons / notes
- Anonymous SMB access can provide valuable binaries for reverse engineering
- .NET binaries often contain hardcoded credentials in connection strings
- DNS zones with CREATE_CHILD permissions enable effective credential phishing attacks
- Linked servers with stored credentials expose cleartext authentication when forced to connect
- WCF services with basic HTTP binding and command injection sinks provide powerful exploitation opportunities
- Local service enumeration is crucial even when remote access is limited
- Multiple paths to SYSTEM exist (WCF injection, token manipulation, service abuse)
- DISM logs can contain sensitive information including passwords from deployment scripts
