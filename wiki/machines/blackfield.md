---
type: machine
title: Blackfield
platform: htb
os: windows
difficulty: hard
tags: [ad, windows, privesc, kerberos, ldap, forensics]
solved: 2026-07-09
sources: [[htb-blackfield]]
related: []
---
# Blackfield
> Active Directory domain controller box featuring AS-REP roasting, BloodHound-enumerated privilege escalation, memory forensics, and backup operator abuse. Attack path: AS-REP roast support user, enumerate ACLs with BloodHound, reset audit2020 password via RPC, extract svc_backup hash from lsass memory dump, abuse SeBackupPrivilege with DiskShadow for ntds.dit access, DCSync for domain compromise.

## Attack path
1. [[as-rep-roasting]] — Crack support user hash via AS-REP roasting
2. [[bloodhound]] — Identify audit2020 ForceChangePassword privilege via BloodHound analysis  
3. [[rpc-password-reset]] — Reset audit2020 password using rpcclient setuserinfo2
4. [[memory-forensics]] — Extract svc_backup NTLM hash from lsass.exe memory dump with pypykatz
5. [[backup-privilege]] — Access forensic share and abuse SeBackupPrivilege as svc_backup
6. [[diskshadow]] — Use DiskShadow VSS shadow copy to access locked ntds.dit file
7. [[dcsync]] — Dump domain password hashes with secretsdump using SYSTEM registry hive

## Techniques used
- [[as-rep-roasting]] — Request Kerberos tickets for users without pre-authentication
- [[bloodhound]] — Analyze ACLs to find privilege escalation paths (ForceChangePassword on audit2020)
- [[rpc-password-reset]] — Reset AD user passwords via rpcclient setuserinfo2 over RPC
- [[memory-forensics]] — Extract credential hashes from process memory dumps using pypykatz
- [[backup-privilege]] — Abuse SeBackupPrivilege to read sensitive files bypassing DACLs
- [[diskshadow]] — Create VSS shadow copies to access locked files like ntds.dit
- [[dcsync]] — Use DCSync rights to dump all domain password hashes

## Tools used
[[nmap]], smbmap, ldapsearch, [[GetNPUsers]], [[hashcat]], bloodhound-python, rpcclient, pypykatz, evil-winrm, diskshadow, secretsdump

## Services / ports
[[dns]] (53), [[kerberos]] (88), [[ldap]] (389), [[smb]] (445), [[winrm]] (5985)

## Lessons / notes
- AS-REP roasting effective for users with UF_DONT_REQUIRE_PREAUTH flag set
- BloodHound can identify ACL-based privilege escalation paths like ForceChangePassword
- RPC interfaces can be used to reset AD passwords without existing credentials
- Memory dumps from forensic investigations often contain valuable credential material
- Backup Operators can use DiskShadow to create VSS shadow copies for accessing otherwise locked files
- EFS (Encrypting File System) can prevent backup privs from reading sensitive files even with SeBackupPrivilege
- DCSync requires special privileges but provides complete domain hash dump
