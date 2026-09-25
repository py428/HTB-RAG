---
type: source
title: "HTB Active writeup"
raw: raw/htb-active.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[active]]
---

# Source: HTB Active writeup

> 0xdf's walkthrough of **Active**, an easy AD DC. Classic chain: anonymous SMB `Replication` share →
> GPP cpassword (SYSVOL `Groups.xml`) → Kerberoast Administrator → admin. Also a solid SMB-enumeration
> reference (`smbmap`, `enum4linux`).

## Key facts extracted
- Domain `active.htb`, 2008 R2 DC; anonymous read on the `Replication` share.
- GPP `Groups.xml` cpassword → `SVC_TGS` : `GPPstillStandingStrong2k18`.
- Kerberoast the Administrator SPN (`active/CIFS:445`) → `Ticketmaster1968` (`hashcat -m 13100`).
- Final access over SMB / `psexec.py`.

## Filed into
[[active]], [[gpp-cpassword]], [[kerberoasting]]
