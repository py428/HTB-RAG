---
type: machine
title: Active
platform: htb
os: windows
difficulty: easy
tags: [ad, active-directory, windows, smb, gpp, kerberoasting]
solved: 2026-07-09
sources: [[htb-active]]
related: [[gpp-cpassword]], [[kerberoasting]]
---

# Active

> Easy Windows Server 2008 R2 DC (domain `active.htb`, retired 2024-05-04). A textbook AD box:
> anonymous SMB → Group Policy Preferences **cpassword** → **Kerberoast** the Administrator → done.
> Shows that pre-2014 GPP passwords and weak service-account passwords are still live on legacy DCs.

## Attack path
1. **Recon** — `nmap` → 2008 R2 DC. `smbmap` shows anonymous READ on the `Replication` share.
2. **GPP password** — `Groups.xml` under `active.htb\Policies\{…}\MACHINE\Preferences\Groups\` carries a `cpassword`; `gpp-decrypt` recovers `GPPstillStandingStrong2k18` for `SVC_TGS` (technique: [[gpp-cpassword]]).
3. **Kerberoasting** — with `SVC_TGS` creds, `GetUserSPNs.py -request` pulls the Administrator's TGS; `hashcat -m 13100` cracks it to `Ticketmaster1968` (technique: [[kerberoasting]]).
4. **Admin** — read `root.txt` straight over SMB (no shell needed), or `psexec.py` for SYSTEM.

## Techniques used
- [[gpp-cpassword]] — `SVC_TGS` password from SYSVOL `Groups.xml`
- [[kerberoasting]] — Administrator SPN (`active/CIFS:445`) cracked offline

## Tools used
[[nmap]], [[smb]] (`smbmap` / `smbclient` / `enum4linux`), [[impacket]] (`GetUserSPNs.py`, `psexec.py`), [[hashcat]], `gpp-decrypt`

## Services / ports
53 DNS, 88 Kerberos, 135 RPC, 139/445 SMB, 389/3268 LDAP, 9389 ADWS — see [[smb]], [[kerberos]], [[ldap]]

## Lessons / notes
- **No shell required** — `root.txt` was pulled over SMB once Administrator creds were in hand.
- Old DC (2008 R2) ⇒ NTLM works freely, no Protected-Users friction (contrast [[absolute]]).
