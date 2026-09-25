---
type: machine
title: Monteverde
platform: htb
os: windows
difficulty: medium
tags: [windows, ad, azure, privesc]
solved: 2026-07-09
sources: [[htb-monteverde]]
related: []
---
# Monteverde
> Windows Active Directory box with Azure AD Connect services, requiring RPC enumeration, password reuse, and Azure database credential extraction.

## Attack path
1. Enumerate users via [[rpc-null-session]]
2. Find credentials via [[password-spray]]
3. Access [[smb]] shares and find Azure credentials in XML file
4. Authenticate via [[winrm]] to get user shell
5. Exploit Azure AD Connect database to extract [[administrator]] credentials

## Techniques used
- [[rpc-null-session]] — Anonymous RPC access to enumerate domain users via `querydispinfo`
- [[password-spray]] — Username as password attack with crackmapexec
- [[azure-ad-connect-database]] — Query ADSync LocalDB to extract replication credentials via PowerShell

## Tools used
[[nmap]], [[rpcclient]], [[crackmapexec]], [[smbmap]], [[smbclient]], [[evil-winrm]]

## Services / ports
[[smb]] (445), [[ldap]] (389), [[kerberos]] (88), [[winrm]] (5985)

## Lessons / notes
- Azure AD Connect stores replication credentials in a LocalDB instance at `C:\Users\<user>\AppData\Local\Microsoft\SQL Server Local DB Artifacts`
- The database `ADSync` contains tables `mms_server_configuration` and `mms_management_agent` with encrypted credentials
- PowerShell script using `mcrypt.dll` can decrypt the configuration and extract the replication account password
- Modern Azure AD instances require access to the ADSync service account context to decrypt credentials
- Service account `SABatchJobs` had username as password: `SABatchJobs:SABatchJobs`