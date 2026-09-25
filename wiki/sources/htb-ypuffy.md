---
type: source
title: "HTB Ypuffy writeup"
raw: raw/htb-ypuffy.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[ypuffy]]
---
# Source: HTB Ypuffy writeup
> Complete walkthrough of Ypuffy HackTheBox machine covering LDAP enumeration, pass-the-hash SMB access, SSH certificate authority abuse, and multiple privilege escalation paths including doas and Xorg vulnerability.
## Key facts extracted
- Anonymous LDAP access revealing user Samba NT hashes
- SMB share access using NTLM hash authentication
- SSH certificate authority with TrustedUserCAKeys configuration
- doas configuration allowing alice1978 to run ssh-keygen as userca
- HTTP service providing SSH principal enumeration via curl
- CVE-2018-14665 Xorg privilege escalation available
## Filed into
[[ypuffy]], [[ldap-enumeration]], [[pass-the-hash]], [[ssh-certificate-signing]], [[doas-abuse]], [[linux]], [[ad]]
