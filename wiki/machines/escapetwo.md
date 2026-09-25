---
type: machine
title: EscapeTwo
platform: htb
os: windows
difficulty: easy
tags: [windows, ad, mssql, adcs, web]
solved: 2026-07-09
sources: [[htb-escapetwo]]
related: []
---
# EscapeTwo
> Windows Active Directory box starting with domain credentials, requiring MSSQL exploitation for initial access, AD pivoting via password reuse, and ADCS ESC4 template abuse for privilege escalation to Administrator.

## Attack path
1. Initial access via [[mssql-xp-cmdshell]] using credentials found in corrupted Excel files on SMB share
2. Credential reuse and pivoting to user with WinRM access
3. [[shadow-credentials]] abuse via [[acl-genericall]] from WriteOwner privilege
4. [[adcs-template-abuse]] (ESC4) to obtain Domain Administrator certificate

## Techniques used
- [[password-spray]] — Validating credentials extracted from Excel files against SMB and MSSQL
- [[mssql-xp-cmdshell]] — Enabling xp_cmdshell as sa to execute system commands and get reverse shell
- [[acl-genericall]] — Using BloodyAD to grant GenericAll on ca_svc after setting owner
- [[shadow-credentials]] — Using Certipy to add Key Credential for authentication as ca_svc
- [[adcs-template-abuse]] — Modifying ESC4-vulnerable certificate template to issue Administrator certificate

## Tools used
- [[nmap]], [[netexec]], [[smbclient]], [[mssqlclient]] (impacket), [[certipy]], [[bloodyad]], evil-winrm

## Services / ports
- [[smb]] (445), [[ldap]] (389/636), [[kerberos]] (88), [[mssql]] (1433), [[winrm]] (5985)

## Lessons / notes
- Excel file corruption can be identified and analyzed using unzip or by fixing file signatures
- MSSQL sa credentials may exist as local accounts separate from domain accounts
- WriteOwner privilege can be abused to become owner and grant full control
- ESC4 template abuse involves modifying template configuration then requesting certificates for higher-privileged users
- BloodHound is valuable for identifying AD privilege escalation paths like WriteOwner
