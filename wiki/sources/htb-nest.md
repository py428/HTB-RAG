---
type: source
title: "HTB Nest writeup"
raw: raw/htb-nest.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[nest]]
---
# Source: HTB Nest writeup
> Easy-difficulty Windows box with SMB enumeration, .NET reverse engineering, custom service exploitation, and multiple privilege escalation paths.

## Key facts extracted
- Anonymous SMB access to Data share with HR documents containing credentials  
- TempUser credentials: welcome2019 found in welcome email template
- Notepad++ config revealed path to normally inaccessible directory inside restricted share
- Visual Basic .NET project contained password decryption functions with hardcoded key
- Custom HQK Reporting Service on TCP 4386 with debug mode password in alternate data stream
- Administrator credentials stored encrypted in LDAP configuration used by custom service
- .NET binary HqkLdap.exe could be debugged to extract decrypted password from process memory
- Multiple unintended privilege escalation paths existed due to service misconfigurations

## Filed into
[[nest]], [[smb-enumeration]], [[dotnet-reversing]], [[custom-service]], [[binary-debugging]], [[ads-alternate-data-stream]]