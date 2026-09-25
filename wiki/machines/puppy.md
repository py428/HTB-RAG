---
type: machine
title: "HTB Puppy"
platform: htb
os: windows
difficulty: medium
tags: [windows, ad, ldap, kerberos, winrm, smb, privesc]
solved: 2026-07-09
sources: [[htb-puppy]]
related: []
---

# HTB Puppy

> Puppy is a Windows Active Directory pentest simulation. It starts with a set of creds in the HR group, which is a common target of phishing attacks. That user has GenericWrite over the Developers group, so I'll add my user and get access to SMB shares where I'll find a KeePassXC database. I'll crack the secret with John, and get auth as the next user. That user is a member of Senior Devs, which has GenericAll over another user. I'll reset that user's password and get a WinRM session. This user has access to a site backup, where I'll find a password to spray and get WinRM as the next user. Finally, I'll abuse that user's DPAPI access to get a saved credential for an administrator.

## Attack path

1. [[acl-genericwrite]] over Developers group from HR user
2. [[dacl-write-members]] to add user to Developers group for SMB access
3. [[credential-extraction]] from KeePassXC database via master password cracking
4. [[password-spray]] to authenticate as ant.edwards
5. [[acl-genericall]] over adam.silver user from Senior Devs group membership
6. [[password-reset]] and account enablement for adam.silver via GenericAll
7. [[file-include]] to find LDAP bind credentials in website backup
8. [[password-spray]] for steph.cooper authentication
9. [[dpapi]] credential extraction from Windows Credential Manager
10. [[acl-genericall]] to Administrator via steph.cooper_adm group membership

## Techniques used

- [[acl-genericwrite]] — levi.james in HR group has GenericWrite over Developers group, enabling self-add
- [[dacl-write-members]] — Using net rpc group addmem to add user to Developers group
- [[password-spray]] — Testing multiple passwords against multiple users via netexec
- [[acl-genericall]] — Senior Devs group has GenericAll over adam.silver user object
- [[password-reset]] — Using net rpc password to reset adam.silver password
- [[acl-forcechangepassword]] — Using bloodyAD to remove ACCOUNTDISABLE flag
- [[file-include]] — Extracting credentials from nms-auth-config.xml.bak in site backup
- [[dpapi]] — Using impacket dpapi.py to decrypt stored credential with master key
- [[acl-genericall]] — steph.cooper_adm is in Administrators group for SYSTEM access

## Tools used

- [[nmap]], [[netexec]], [[bloodhound]], [[smbclient]], [[net]], [[john]], [[hashcat]], [[evil-winrm]], [[impacket]]

## Services / ports

- [[ldap]] (389/636/3268/3269) — Active Directory LDAP services
- [[kerberos]] (88) — Windows Kerberos  
- [[smb]] (445) — File sharing with DEV share for developers
- [[winrm]] (5985) — Windows Remote Management
- [[dns]] (53) — Domain DNS services
- [[rpc]] (135) — Windows RPC services

## Lessons / notes

- BloodHound analysis is crucial for identifying ACL abuse opportunities in AD environments
- GenericWrite over a group allows adding yourself to that group for privilege escalation
- KeePassXC databases with Argon2 may require specific John versions to crack
- GenericAll over a user object enables password resets and account modifications
- Website backups often contain sensitive configuration files with credentials
- DPAPI master keys can be decrypted with user passwords to extract stored credentials
- Group memberships should be verified after changes as cleanup scripts may revert modifications
