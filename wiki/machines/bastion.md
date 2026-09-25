---
type: machine
title: "HTB Bastion"
platform: htb
os: windows
difficulty: easy
tags: [windows, smb, vhd, credential-recovery, privesc]
solved: 2026-07-09
sources: [[htb-bastion]]
related: []
---
# HTB Bastion
> Bastion was an easy Windows box featuring SMB share enumeration with VHD backup files. Mounting the VHD reveals registry hives for hash dumping, and password reuse from mRemoteNG configuration files leads to administrator access via SSH.
## Attack path
1. Enumerate [[smb]] shares to find Backups directory containing WindowsImageBackup VHD files
2. Mount VHD using [[guestmount]] to access offline Windows filesystem
3. Dump [[registry-hashes]] from mounted SAM/SYSTEM files using [[secretsdump]] to get l4mpje hash
4. Crack hash and [[ssh]] as l4mpje using recovered password  
5. Find mRemoteNG configuration in AppData with encrypted administrator password
6. Decrypt mRemoteNG password using [[mremoteng-decrypt]] and SSH as administrator
## Techniques used
- [[vhd-mount]] — Mount Windows VHD backup files from SMB shares using guestmount to access offline filesystem
- [[registry-hashes]] — Dump password hashes from Windows registry hives (SAM, SYSTEM, SECURITY) using secretsdump
- [[mremoteng-decrypt]] — Decrypt mRemoteNG saved passwords from confCons.xml configuration files
- [[password-cracking]] — Crack NTLM hashes using hashcat and crackstation
## Tools used
[[nmap]], [[smbmap]], [[smbclient]], [[guestmount]], [[secretsdump]], [[hashcat]], [[netcat]]
## Services / ports
- [[smb]] (445) - Windows shares including Backups with VHD files
- [[ssh]] (22) - OpenSSH for Windows 7.9
- rpc (135, 139) - Windows RPC and NetBIOS services
## Lessons / notes
- VHD backups often contain credential material in registry hives
- mRemoteNG stores encrypted passwords that can be decrypted with default password "mR3m"
- SSH on Windows is unusual but provides convenient shell access
- Password reuse between services is common for administrative access
