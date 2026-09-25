---
type: machine
title: Cascade
platform: htb
os: windows
difficulty: medium
tags: [ad, ldap, smb, winrm, vnc, encryption, privesc]
solved: 2026-07-09
sources: [[htb-cascade]]
related: []
---
# Cascade
> Cascade is a medium Windows Active Directory box focusing on credential recovery from various sources. The exploitation path involves LDAP enumeration for initial credentials, SMB access with TightVNC password extraction, database decryption for service credentials, and AD Recycle Bin exploitation for admin access.

## Attack path
1. [[ldap-enumeration]] → Base64-encoded password in user attributes
2. [[smb-access]] → TightVNC password decryption
3. [[winrm-access]] as s.smith
4. [[database-decryption]] → Service account credentials from SQLite
5. [[winrm-access]] as arksvc (AD Recycle Bin member)
6. [[ad-recycle-bin]] → Deleted admin credentials
7. [[winrm-access]] as administrator

## Techniques used
- [[ldap-enumeration]] — Anonymous LDAP binding reveals cascadeLegacyPwd attribute
- [[password-decryption]] — Base64 decoding for LDAP passwords, VNC password decryption
- [[database-decryption]] — Decrypt encrypted password from SQLite database
- [[ad-recycle-bin]] — Query deleted objects to recover admin credentials

## Tools used
- [[nmap]] — Port scanning and service identification
- [[ldapsearch]] — LDAP enumeration and data extraction
- [[smbclient]] — SMB share access and file retrieval
- evil-winrm — WinRM shell access
- [[crackmapexec]] — Credential validation and enumeration
- vncpwd — TightVNC password decryption
- [[sqlite]] — Database analysis
- Get-ADObject — PowerShell AD Recycle Bin queries

## Services / ports
- 53/tcp — [[dns]] (Microsoft DNS)
- 88/tcp — [[kerberos]] (Microsoft Windows Kerberos)
- 135/tcp — [[rpc]] (Microsoft Windows RPC)
- 389/tcp — [[ldap]] (Microsoft Windows Active Directory)
- 445/tcp — [[smb]] (Microsoft-Ds)
- 636/tcp — [[ldap]] (LDAP SSL)
- 3268/tcp — [[ldap]] (Global Catalog LDAP)
- 3269/tcp — [[ldap]] (Global Catalog LDAP SSL)
- 5985/tcp — [[winrm]] (HTTPAPI)

## Lessons / notes
- LDAP anonymous binding can reveal sensitive user attributes
- Legacy password attributes may contain credential history
- TightVNC passwords encrypted with static key can be cracked
- Service accounts may have credentials stored in databases
- AD Recycle Bin preserves deleted user objects with credentials
- Get-ADObject with -includeDeletedObjects queries recycle bin
- Password reuse is common across accounts
