---
type: source
title: "HTB Absolute writeup"
raw: raw/htb-absolute.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[absolute]]
---

# Source: HTB Absolute writeup

> Walkthrough of the Insane Windows AD box **Absolute** (0xdf's writeup). Covers a full
> Kerberos-constrained kill chain: image-metadata user enum → AS-REP roast → LDAP-description
> creds → dynamic analysis of a Nim binary → DACL/`GenericWrite` abuse → shadow credentials →
> Kerberos relay (KrbRelay/KrbRelayUp) → DCSync. Heavy emphasis on the friction of doing
> everything over Kerberos because NTLM is disabled for all user accounts.

## Key facts extracted
- Domain `absolute.htb`, DC `dc.absolute.htb`; ~7h clock skew to handle before any Kerberos auth.
- Username format is `[first-initial].[lastname]`, recovered from `exiftool` Author fields.
- AS-REP-roastable user: `d.klay` → `Darkmoonsky248girl`.
- `svc_smb` password (`AbsoluteSMBService123!`) leaked via its LDAP description attribute.
- `m.lovegod` creds (`AbsoluteLDAP2022!`) embedded in a Nim-compiled `test.exe` on the `Shared` share.
- Priv esc path: `m.lovegod` owns "Network Audit" → grant self `WriteMembers` → join group (`GenericWrite` on `winrm_user`) → shadow credential.
- KrbRelay requires an **interactive** session; achieved under WinRM via [[runascs]] with logon type **9** (`-l 9`).
- Final leap: forge a shadow credential for the `DC$` machine account → PKINIT TGT → `DC$` NT hash → DCSync (machine accounts are *not* in Protected Users).

## Filed into
[[absolute]], [[kerberos-username-enumeration]], [[as-rep-roasting]], [[ntlm-disabled-protected-users]], [[ldap-description-credential]], [[dacl-write-members]], [[shadow-credentials]], [[kerberos-relay]], [[dcsync]]
