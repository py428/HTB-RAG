---
type: machine
title: Resolute
platform: htb
os: windows
difficulty: medium
tags: [windows, ad, privesc]
solved: 2026-07-09
sources: [[htb-resolute]]
related: []
---
# Resolute
> An Active Directory domain controller where RPC enumeration reveals user information and default passwords. The attack path involves password spraying, WinRM access, PowerShell transcript analysis, and DnsAdmins privilege escalation.

## Attack path
1. [[nmap]] reveals extensive AD services including [[ldap]], [[kerberos]], [[winrm]]
2. [[rpc-null-session]] enumeration to list users and find password in comments
3. [[password-spray]] with Welcome123! across all users
4. [[winrm]] access as melanie user
5. [[powershell-transcript]] analysis reveals ryan's credentials
6. WinRM access as ryan who is in DnsAdmins group
7. [[dnsadmins-dnscmd-abuse]] to load malicious DLL and get SYSTEM

## Techniques used
- [[rpc-null-session]] — Enumerate AD users and attributes without authentication
- [[password-spray]] — Test single password across multiple user accounts
- [[powershell-transcript]] — PowerShell logging may expose credentials in command history
- [[dnsadmins-dnscmd-abuse]] — Load arbitrary DLL via dnscmd for SYSTEM privilege

## Tools used
[[nmap]] | [[rpcclient]] | [[crackmapexec]] | [[evil-winrm]] | [[msfvenom]]

## Services / ports
[[ldap]] (389) | [[kerberos]] (88) | [[smb]] (445) | [[winrm]] (5985) | dns (53)

## Lessons / notes
- RPC null session can enumerate AD users and descriptions
- User comments in AD may contain default passwords
- PowerShell transcripts log all commands and may expose credentials
- DnsAdmins group members can load arbitrary DLLs via dnscmd
- System changes revert within 1 minute due to change freeze
- Contractors group membership may grant WinRM access
- msfvenom DLL payloads hang DNS service when loaded
