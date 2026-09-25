---
type: machine
title: Support
platform: htb
os: windows
difficulty: easy
tags: [ad, windows, web, ldap, smb, kerberos]
solved: 2026-07-09
sources: [[htb-support]]
related: []
---
# Support
> Windows Domain Controller with open SMB share containing custom .NET tool that embeds LDAP credentials. After extracting creds, find password in LDAP info field for shared account with WinRM access, then abuse RBCD (Resource-Based Constrained Delegation) to get Domain Admin access.

## Attack path
1. [[smb-share-access]] — Download UserInfo.exe from open SMB share
2. [[dotnet-reversing]] — Extract LDAP credentials from .NET binary (static/dynamic analysis)
3. [[ldap-password-reuse]] — Find shared support account password in LDAP info field
4. [[winrm-access]] — Login as support user via WinRM
5. [[rbcd]] — Abuse Resource-Based Constrained Delegation to impersonate Domain Administrator
6. [[kerberos-ticket]] — Use S4U2proxy to get Administrator service ticket
7. [[psexec]] — Access DC as Administrator using forged ticket

## Techniques used
- [[dotnet-reversing]] — Static analysis with dnSpy or dynamic via Wireshark to extract encrypted LDAP credentials
- [[ldap-password-reuse]] — Password stored in LDAP info field for shared support account
- [[rbcd]] — Resource-Based Constrained Delegation abuse to create fake computer and impersonate Administrator
- [[kerberos-ticket]] — S4U2self and S4U2proxy delegation to obtain Administrator service ticket

## Tools used
[[nmap]], [[smbclient]], [[crackmapexec]], dnSpy, [[wireshark]], [[evil-winrm]], [[bloodhound]], [[powerview]], PowerMad, [[rubeus]], [[impacket]]

## Services / ports
[[smb]] (445), [[ldap]] (389), [[winrm]] (5985), [[kerberos]] (88)

## Lessons / notes
- .NET binaries can be easily reversed with dnSpy to find hardcoded credentials
- LDAP info fields sometimes contain passwords for shared accounts
- RBCD requires: machine account quota > 0, 2012+ DC, and GenericAll on DC object
- Bloodhound Python (bloodhound-python) works without a GUI shell