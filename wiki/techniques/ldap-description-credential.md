---
type: technique
title: Credentials in LDAP Attributes (description)
tags: [ad, windows, ldap, credential-access, misconfiguration]
platforms: [windows]
mitre: [T1552.004]
updated: 2026-07-09
---

# Credentials in LDAP Attributes (description)

## What it is
Operators frequently stash service-account passwords in the **`description`** (or `info`, `comment`) attribute of a user/computer object "so they don't forget it." A single authenticated LDAP query dumps them for every account. A perennial AD misconfiguration.

## When it works
- You have **any** valid bind to LDAP (even a low-priv user — the `description` attribute is readable by default to authenticated users).

## How it's done
```
# crackmapexec surfaces the description column automatically
crackmapexec ldap 10.10.11.181 -u d.klay -p '<pw>' -k --users

# or raw ldapsearch — pull the description field
ldapsearch -H ldap://dc.absolute.htb -Y GSSAPI -b "dc=absolute,dc=htb" description
```
Anything that looks like a password in a description (`AbsoluteSMBService123!`) is one. Validate with [[crackmapexec]] against SMB.

## Observed on
- [[absolute]] — `crackmapexec ldap --users` exposed `svc_smb`'s description (`AbsoluteSMBService123!`), which was its actual password, granting access to the `Shared` SMB share.

## Variants & pitfalls
- Kerberos-only environments: bind with `-Y GSSAPI` (after `kinit`), and ensure `dc.absolute.htb` is the first hosts entry for the reverse-lookup the GSSAPI bind performs.
- Don't stop at `description` — check `info`, `userPassword`, `unixUserPassword`, and GPP/sysvol too.

## See also
[[ntlm-disabled-protected-users]], [[crackmapexec]], [[ldap]]
