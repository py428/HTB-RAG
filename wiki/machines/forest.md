---
type: machine
title: Forest
platform: htb
os: windows
difficulty: easy
tags: [ad, active-directory, windows, exchange, as-rep-roasting, dcsync]
solved: 2026-07-09
sources: [[htb-forest]]
related: [[as-rep-roasting]], [[writedacl-grant-dcsync]], [[dcsync]]
---

# Forest

> Easy Windows Server 2016 DC (domain `htb.local`, retired 2020-03-21). An Exchange-themed AD box:
> RPC null-session user enum → **AS-REP roast** svc-alfresco → WinRM shell → abuse Exchange
> permissions to **grant self DCSync rights** → dump the Administrator hash. Clean proof that
> DCSync needs the replication ACL, not Domain Admin.

## Attack path
1. **Recon** — `nmap` → 2016 DC, WinRM (5985) open. SMB needs creds; DNS zone transfer fails.
2. **User enum** — `rpcclient` null session → `enumdomusers` / `enumdomgroups` (technique: [[rpc-null-session]]).
3. **AS-REP roast** — `GetNPUsers.py` finds `svc-alfresco` has preauth disabled; `hashcat -m 18200` → `s3rvice` (technique: [[as-rep-roasting]]).
4. **Foothold** — `svc-alfresco` is in Remote Management Users → `evil-winrm` shell.
5. **Privilege escalation** — `svc-alfresco` → Account Operators (nested groups) → `GenericAll` on "Exchange Windows Permissions" → join it → `WriteDacl` on the domain → grant self DCSync rights (technique: [[writedacl-grant-dcsync]]).
6. **DCSync** — `secretsdump.py` dumps the Administrator hash → `wmiexec`/`evil-winrm` as admin (technique: [[dcsync]]).

## Techniques used
- [[rpc-null-session]] — null RPC session → users/groups
- [[as-rep-roasting]] — `svc-alfresco` preauth disabled → `s3rvice`
- [[writedacl-grant-dcsync]] — Exchange Windows Permissions → DCSync rights on the domain
- [[dcsync]] — dumped the Administrator hash

## Tools used
[[nmap]], [[impacket]] (`GetNPUsers.py`, `secretsdump.py`, `wmiexec.py`, `smbserver.py`), [[hashcat]], [[bloodhound]] (SharpHound), [[powerview]], [[evil-winrm]], `rpcclient`, `aclpwn`

## Services / ports
53 DNS, 88 Kerberos, 135 RPC, 139/445 SMB, 389/3268 LDAP, 5985 WinRM, 9389 ADWS — see [[kerberos]], [[ldap]], [[smb]]

## Lessons / notes
- **DCSync ≠ Domain Admin.** `svc-alfresco` reached DCSync purely through ACL abuse (Exchange perms) — never via DA.
- **A revert script fights you.** A scheduled task (`revert.ps1`) resets `svc-alfresco`'s password and strips its group/DCSync rights every ~60s — chain the grant + `secretsdump` into a single command.
- The nested-group edge BloodHound surfaced: `svc-alfresco` → Service Accounts → Privileged IT Accounts → Account Operators → `GenericAll` on Exchange Windows Permissions.
