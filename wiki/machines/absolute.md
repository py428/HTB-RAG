---
type: machine
title: Absolute
platform: htb
os: windows
difficulty: insane
tags: [ad, active-directory, windows, kerberos, adcs, kerberos-relay]
solved: 2026-07-09
sources: [[htb-absolute]]
related: [[as-rep-roasting]], [[shadow-credentials]], [[kerberos-relay]], [[dcsync]]
---

# Absolute

> Insane Windows AD box (retired 2023-05-27, domain `absolute.htb`, DC `dc.absolute.htb`).
> A long enumeration chain that starts from **full names hidden in image metadata**, walks
> through four sets of credentials, and ends with a **Kerberos relay → machine-account shadow
> credential → DCSync**. The defining twist: **every user account is in the Protected Users
> group, so NTLM is disabled end-to-end** — nearly everything must be done over Kerberos.

## Attack path
1. **Recon** — `nmap` shows a Windows DC. SMB/LDAP need auth; DNS zone transfer fails; the site on 80 is a static image gallery.
2. **Usernames** — `exiftool` on the hero images reveals "Author" names; `username-anarchy` permutes them; `kerbrute userenum` confirms the `[first-initial].[lastname]` format (technique: [[kerberos-username-enumeration]]).
3. **First creds** — `GetNPUsers.py` finds `d.klay` is AS-REP-roastable; `hashcat -m 18200` cracks it (technique: [[as-rep-roasting]]).
4. **Kerberos-only** — NTLM is disabled (`STATUS_ACCOUNT_RESTRICTION`); auth with `-k` + `kinit` (concept: [[ntlm-disabled-protected-users]]).
5. **Second creds** — `crackmapexec ldap --users` leaks `svc_smb`'s password from its **description field** (technique: [[ldap-description-credential]]).
6. **Third creds** — `svc_smb` reads the `Shared` share → a Nim binary (`test.exe`); dynamic analysis with Wireshark reveals an embedded LDAP bind for `m.lovegod`.
7. **Group/ACL abuse** — `m.lovegod` owns the "Network Audit" group → grant self `WriteMembers` via `dacledit.py`, add self to the group, which has `GenericWrite` on `winrm_user` (technique: [[dacl-write-members]]).
8. **Foothold** — `GenericWrite` → shadow credential on `winrm_user` via `certipy shadow auto` → `evil-winrm` shell (technique: [[shadow-credentials]]).
9. **Root** — `KrbRelay` (over LDAP) adds `winrm_user` to Administrators; alternatively `KrbRelayUp` forges a shadow cred for the **DC$ machine account** → `Rubeus asktgt` (PKINIT) → DC$ NT hash → DCSync (techniques: [[kerberos-relay]], [[dcsync]]).

## Techniques used
- [[kerberos-username-enumeration]] — valid-user discovery via image metadata + kerbrute
- [[as-rep-roasting]] — `d.klay` had preauth disabled; cracked offline
- [[ntlm-disabled-protected-users]] — the whole box pivots on Kerberos-only auth
- [[ldap-description-credential]] — `svc_smb` password in LDAP description
- [[dacl-write-members]] — `m.lovegod` writes itself into "Network Audit"
- [[shadow-credentials]] — shadow cred on `winrm_user` for the foothold
- [[kerberos-relay]] — KrbRelay + KrbRelayUp for privesc
- [[dcsync]] — DC$ hash dumps NTDS

## Tools used
[[nmap]], [[exiftool]], [[kerbrute]], [[impacket]], [[hashcat]], [[bloodhound]], [[crackmapexec]], [[certipy]], [[evil-winrm]], [[runascs]], [[rubeus]]

## Services / ports
53 DNS, 80 HTTP (IIS), 88 Kerberos, 135 RPC, 389/636/3268/3269 LDAP, 445 SMB, 464 kpasswd, 5985 WinRM, 9389 ADWS — see [[kerberos]], [[ldap]], [[smb]]

## Lessons / notes
- **Clock skew matters under Kerberos** — the DC was ~7h off; `ntpdate` against the DC was required or `kinit` failed.
- **`/etc/hosts` ordering matters for Kerberos** — `dc.absolute.htb` must resolve before `absolute.htb` (reverse-lookup quirk that breaks GSSAPI binds; Ippsec's catch).
- **The machine account is the prize** — Protected Users blocked NTLM for every *user*, but `DC$` is not in that group, so a forged machine-account hash unlocks DCSync and the final shell.
