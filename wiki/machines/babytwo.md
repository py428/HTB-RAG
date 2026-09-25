---
type: machine
title: BabyTwo
platform: htb
os: windows
difficulty: medium
tags: [ad, windows, gpo, privesc]
solved: 2026-07-09
sources: [[htb-babytwo]]
related: []
---
# BabyTwo is a medium Windows Active Directory box where username-as-password credentials provide initial access, SYSVOL logon script poisoning grants a user shell, and abuse of GPO management permissions leads to domain administration.

## Attack path
1. [[password-spray]] using username-as-password pattern
2. [[logon-script-poisoning]] by modifying SYSVOL login script
3. [[acl-abuse]] to grant GPO administration permissions
4. [[gpo-abuse]] to gain membership in Administrators group

## Techniques used
- [[password-spray]] — Username-as-password pattern tested against all users, finding two valid accounts
- [[logon-script-poisoning]] — Modifying logon scripts in SYSVOL to execute reverse shells on user login
- [[acl-abuse]] — WriteOwner and WriteDacl permissions used to grant control over service accounts
- [[gpo-abuse]] — GPO management abused to add users to privileged groups via scheduled tasks

## Tools used
[[nmap]], [[netexec]], [[smbclient]], [[bloodhound]], [[evil-winrm]], [[pygpoabuse]]

## Services / ports
[[smb]] (445), [[ldap]] (389), [[kerberos]] (88), [[winrm]] (5985)

## Lessons / notes
- Password spraying with username patterns often succeeds in AD environments
- SYSVOL is a powerful target for privilege escalation via logon scripts
- ACL analysis with BloodHound can reveal non-obvious privilege escalation paths
- GPO management permissions are equivalent to domain administration in practice
- pyGPOAbuse automates GPO-based privilege escalation
