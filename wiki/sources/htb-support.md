---
type: source
title: "HTB Support writeup"
raw: raw/htb-support.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[support]]
---
# Source: HTB Support writeup
> Windows Domain Controller box featuring a custom .NET tool (UserInfo.exe) in an open SMB share containing hardcoded LDAP credentials. After extracting credentials, find a shared account password stored in LDAP info field, use it for WinRM access, then abuse Resource-Based Constrained Delegation (RBCD) to impersonate the Domain Administrator and gain full control.

## Key facts extracted
- SMB share `support-tools` contains UserInfo.exe with encrypted LDAP credentials
- .NET binary analysis (dnSpy or Wireshark) reveals credentials for support\ldap user
- Shared `support` account has password in LDAP info field: "Ironside47pleasure40Watchful"
- Support user is member of "Remote Management Users" for WinRM access
- "Shared Support Accounts" group has GenericAll on DC computer object
- RBCD abuse allows creating fake computer and impersonating Administrator via S4U2proxy

## Filed into
[[support]], [[dotnet-reversing]], [[ldap-password-reuse]], [[rbcd]], [[kerberos-ticket]], [[smb-share-access]], [[winrm-access]]