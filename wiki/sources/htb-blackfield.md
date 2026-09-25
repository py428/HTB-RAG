---
type: source
title: "HTB Blackfield writeup"
raw: raw/htb-blackfield.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[blackfield]]
---
# Source: HTB Blackfield writeup
> Comprehensive Active Directory exploitation guide covering AS-REP roasting, BloodHound ACL analysis, RPC password reset, memory forensics for credential extraction, backup operator privilege abuse, VSS shadow copy creation, and DCSync domain compromise.

## Key facts extracted
- Domain controller BLACKFIELD.local with hostname DC01
- Support account vulnerable to AS-REP roasting (no pre-auth required)
- BloodHound reveals support has ForceChangePassword privilege over audit2020
- Forensic share contains memory dumps including lsass.exe with svc_backup credentials
- svc_backup member of Backup Operators group with SeBackupPrivilege
- EFS protects root.txt from being read even with backup privileges
- ntds.dit accessible via VSS shadow copy using DiskShadow
- SYSTEM registry hive required for ntds.dit hash extraction

## Filed into
[[blackfield]], [[as-rep-roasting]], [[bloodhound]], [[rpc-password-reset]], [[memory-forensics]], [[backup-privilege]], [[diskshadow]], [[dcsync]]
