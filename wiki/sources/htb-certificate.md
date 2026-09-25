---
type: source
title: "HTB Certificate writeup"
raw: raw/htb-certificate.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[certificate]]
---
# Source: HTB Certificate writeup

> Comprehensive writeup for HTB Certificate box covering web exploitation, Kerberos cracking, ADCS ESC3, and privilege escalation via SeManageVolumePrivilege.

## Key facts extracted
- PHP web application with assignment submission feature accepting zip archives
- Two file upload bypass techniques: null byte injection and zip stacking  
- Database credentials exposed in configuration file with bcrypt-hashed passwords
- PCAP file contains Kerberos AS-REQ for Lion.SK user
- Lion.SK has enrollment rights in Delegated-CRA template vulnerable to ESC3
- Ryan.K obtained via ESC3 has SeManageVolumePrivilege for volume maintenance
- Administrator flag encrypted with EFS, accessible via ACL modification
- ADCS CA private key exportable for Golden Certificate attack

## Filed into
[[certificate]], [[file-upload-bypass]], [[password-reuse]], [[kerberoasting]], [[adcs-exploitation]], [[semanagevolume-privilege]]
