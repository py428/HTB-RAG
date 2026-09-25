---
type: technique
title: NTLM Disabled / Protected Users (Kerberos-only environments)
tags: [ad, windows, kerberos, authentication, concept]
platforms: [windows]
updated: 2026-07-09
---

# NTLM Disabled / Protected Users (Kerberos-only)

## What it is
A recurring constraint, not an exploit: the target has disabled NTLM (domain-wide policy, or per-user via membership in the **Protected Users** group). NTLM auth fails with `STATUS_ACCOUNT_RESTRICTION`; only **Kerberos** binds work. This is the spine of "hard" modern AD boxes — it blocks pass-the-hash, null sessions, and plaintext SMB binds, forcing every step through Kerberos ticketing.

## When it applies
- SMB/LDAP logins fail with `STATUS_ACCOUNT_RESTRICTION` (NTLM refused) but `-k` (Kerberos) succeeds.
- BloodHound/`klist` show the target principals in the **Protected Users** group.
- A plaintext password you cracked (e.g. via [[as-rep-roasting]]) still works — but only with a Kerberos ticket.

## How to work within it
```
# Get a TGT (mind clock skew — ntpdate against the DC first)
kinit d.klay
export KRB5CCNAME=/tmp/krb5cc_1000

# Every tool gets -k (and the ccache) instead of -p
crackmapexec smb dc.absolute.htb -k --use-kcache
smbclient.py 'absolute.htb/d.klay@dc.absolute.htb' -k -no-pass
ldapsearch -H ldap://dc.absolute.htb -Y GSSAPI ...
```
- Fix clock skew first (`ntpdate dc.absolute.htb`; on VirtualBox stop `vboxadd-service`).
- Put `dc.absolute.htb` before `absolute.htb` in `/etc/hosts` (GSSAPI reverse-lookup quirk).
- Delete & re-`kinit` whenever your effective identity/permissions change.

## Observed on
- [[absolute]] — every *user* account was in Protected Users, so the entire chain (LDAP binds, SMB, group edits) ran over Kerberos. The decisive exception: **machine accounts (e.g. `DC$`) and built-in `Administrator` are NOT in Protected Users**, so a forged `DC$` hash enabled [[dcsync]] and the final pass-the-hash shell.

## See also
[[as-rep-roasting]], [[dcsync]], [[kerberos-relay]], [[shadow-credentials]], [[crackmapexec]]
