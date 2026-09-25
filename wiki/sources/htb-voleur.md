---
type: source
title: "HTB Voleur writeup"
raw: raw/htb-voleur.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[voleur]]
---
# Source: HTB Voleur writeup
> 0xdf's comprehensive writeup for HTB Voleur covering assume breach credentials, Excel password cracking, targeted Kerberoasting, AD recycle bin recovery, DPAPI credential extraction, WSL pivoting, and NTDS.dit hash dumping.

## Key facts extracted
- Assume breach start: ryan.naylor / HollowOct31Nyt (Kerberos only, NTLM disabled)
- Excel workbook Access_Review.xlsx on IT share contains service account passwords
- Targeted Kerberoasting path: svc_ldap (WriteSPN on svc_winrm) → crack TGS → WinRM access
- AD recycle bin recovery: Restore-ADObject for deleted todd.wolfe account
- DPAPI credentials: Archived home directories in C:\IT contain encrypted credential files
- WSL pivot: svc_backup SSH key provides access to Ubuntu WSL on port 2222
- Registry access: WSL mounts Windows C: drive at /mnt/c for SYSTEM/SECURITY hives
- Alternative path: NetExec tombstone module can recover deleted accounts directly

## Filed into
[[voleur]], [[kerberoasting]], [[ad-recycle-bin]], [[dpapi]], [[ssh-key-auth]], [[wsl-pivot]], [[dcsync]]
