---
type: machine
title: Certificate
platform: htb
os: windows
difficulty: hard
tags: [ad, windows, web, privesc, adcs]
solved: 2026-07-09
sources: [[htb-certificate]]
related: []
---
# Certificate

> Hard Windows Active Directory box featuring web upload bypasses, Kerberoasting, ESC3 ADCS exploitation, and SeManageVolumePrivilege abuse for privilege escalation.

## Attack path
1. [[file-upload-bypass]] via null byte injection and zip stacking → [[webshell]] → www-data
2. [[password-reuse]] from dumped database hashes → [[smb]]/[[winrm]] access as sara.b
3. PCAP [[kerberoasting]] with hashcat → Lion.SK user
4. ESC3 [[adcs-exploitation]] via Delegated-CRA template → Ryan.K user
5. [[semanagevolume-privilege]] abuse → arbitrary file read → [[adcs-exploitation]] (Golden Certificate) → administrator

## Techniques used
- [[file-upload-bypass]] — PHP webshell upload via zip archive manipulation and null byte injection to bypass file extension checks
- [[password-reuse]] — Cracked bcrypt hash from web database reused for domain authentication
- [[kerberoasting]] — Extracted AS-REQ hash from PCAP file and cracked with rockyou.txt
- [[adcs-exploitation]] — ESC3 attack using Certificate Request Agent EKU to request certificate on behalf of Ryan.K
- [[semanagevolume-privilege]] — Abused SeManageVolumePrivilege to modify disk ACLs and read encrypted files

## Tools used
- [[nmap]] — Port scanning and service enumeration
- [[feroxbuster]] — Directory brute forcing on web server
- [[hashcat]] — Cracked bcrypt and Kerberos AS-REQ hashes
- [[netexec]] — SMB/WinRM authentication testing and BloodHound collection
- [[bloodhound]] — AD privilege escalation path analysis
- [[certipy]] — ADCS enumeration and ESC3 exploitation
- [[evil-winrm]] — Windows remote shell access
- RsaCtfTool — RSA private key reconstruction

## Services / ports
- [[smb]] (445) — Domain controller file sharing
- [[ldap]] (389/636/3268/3269) — Active Directory services
- [[kerberos]] (88) — Domain authentication
- [[winrm]] (5985) — Windows remote management
- [[http]] (80) — XAMPP web server with PHP application

## Lessons / notes
- Multiple file upload bypass techniques can bypass the same filter (null bytes + zip stacking)
- Kerberos AS-REQ hashes in PCAPs can be extracted and cracked with hashcat mode 19900
- ESC3 allows requesting certificates on behalf of other users using Certificate Request Agent EKU
- SeManageVolumePrivilege allows direct disk access and can be abused for arbitrary file read
- EFS-encrypted files can be accessed by modifying ACLs with SeManageVolumePrivilege
- Golden Certificate attack allows forging certificates as any user if CA private key is compromised
