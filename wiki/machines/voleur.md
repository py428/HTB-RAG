---
type: machine
title: Voleur
platform: htb
os: windows
difficulty: medium
tags: [windows, ad, kerberos, adcs, ssh, wsl, dpapi, dcsync]
solved: 2026-07-09
sources: [[htb-voleur]]
related: []
---
# Voleur
> Voleur is an Active Directory box starting with assume breach credentials. I'll find credentials in an encrypted Excel workbook on a SMB share, then use targeted Kerberoasting to gain WinRM access. From there, I'll recover a deleted user from the AD recycle bin, exfiltrate DPAPI encrypted credentials from an archived home directory backup, and use an SSH key to access a WSL instance where I can dump the NTDS.dit file and recover the Administrator hash.

## Attack path
1. Authenticate with assume breach credentials and enumerate [[ldap]] and [[smb]] shares
2. Download and crack encrypted Excel workbook to find service account credentials
3. Perform [[kerberoasting]] with targeted SPN addition to get svc_winrm password
4. Access [[winrm]] as svc_winrm and switch to svc_ldap using [[runascs]]
5. Use AD recycle bin to recover deleted todd.wolfe account
6. Access archived home directory via SMB and exfiltrate DPAPI credentials
7. Extract SSH key for svc_backup and access WSL instance on port 2222
8. Dump registry hives and NTDS.dit from WSL-mounted C: drive to get Administrator hash

## Techniques used
- [[kerberoasting]] — Targeted Kerberoasting by adding SPN to svc_winrm account
- [[ad-recycle-bin]] — Recovering deleted todd.wolfe account using Restore-ADObject
- [[dpapi]] — Decrypting Windows credential files using master keys and user passwords
- [[ssh-key-auth]] — Using exfiltrated SSH key to access WSL instance
- [[wsl-pivot]] — Accessing Windows filesystem via WSL mount point for registry/NTDS access
- [[dcsync]] — Extracting Administrator hash from NTDS.dit using secretsdump

## Tools used
- [[nmap]] — Port scanning and service identification
- [[netexec]] — SMB/LDAP enumeration and Kerberos authentication
- smbclient — SMB share access with Kerberos
- hashcat — Cracking Excel encryption and Kerberos tickets
- office2john — Converting encrypted Office documents to hash format
- rusthound-ce — Bloodhound-style AD enumeration
- bloodyAD — LDAP modifications for targeted Kerberoasting
- [[kinit]] — Kerberos ticket initialization
- [[evil-winrm]] — WinRM shell access with Kerberos auth
- runascs — Alternate credential execution for user switching
- [[dpapi]] — DPAPI credential/master key decryption (impacket)
- [[ssh]] — Access to WSL instance using exfiltrated key
- [[secretsdump]] — NTDS.dit hash extraction (impacket)
- [[wmiexec]] — Command execution as Administrator

## Services / ports
- 53/tcp — dns
- 88/tcp — [[kerberos]]
- 135/tcp — [[rpc]]
- 139/tcp — [[smb]] (NetBIOS Session Service)
- 389/tcp — [[ldap]]
- 445/tcp — [[smb]]
- 464/tcp — kpasswd5
- 636/tcp — ldapssl
- 2222/tcp — [[ssh]] (WSL Ubuntu)
- 3268/tcp — globalcatLDAP
- 3269/tcp — globalcatLDAPssl
- 5985/tcp — [[winrm]] (HTTP)
- 9389/tcp — ADWS

## Lessons / notes
- Assume breach scenarios: Start with credentials and focus on credential expansion and privilege escalation
- Encrypted Office documents can be cracked with office2john and hashcat
- Targeted Kerberoasting: Add SPN to accounts with WriteSPN rights for controlled ticket requests
- AD recycle bin: Deleted users can be recovered if you have restore permissions
- DPAPI credentials: Encrypted Windows credentials can be decrypted with the user's password
- WSL instances: May expose Windows filesystem via /mnt/c mount point for registry/NTDS access
- SSH key authentication: Comments in keys can reveal target usernames; brute force if unknown
