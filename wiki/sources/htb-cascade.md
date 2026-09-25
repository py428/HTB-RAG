---
type: source
title: "HTB Cascade writeup"
raw: raw/htb-cascade.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[cascade]]
---
# Source: HTB Cascade writeup
> 0xdf's writeup for HTB Cascade covering Active Directory credential recovery, TightVNC decryption, database exploitation, and AD Recycle Bin enumeration.

## Key facts extracted
- Ryan Thompson LDAP attribute contains base64 password: rY4n5eva
- TightVNC registry password decrypts to: sT333ve2
- Encrypted SQLite password decrypts to: w3lc0meFr31nd (arksvc)
- TempAdmin deleted object contains base64 password: baCT3r1aN00dles
- Domain: cascade.local
- Windows Server 2008 R2 SP1

## Filed into
[[cascade]], [[ldap-enumeration]], [[password-decryption]], [[database-decryption]], [[ad-recycle-bin]], [[smb]], [[winrm]], [[vnc]], [[ad]], [[encryption]], [[privesc]]
