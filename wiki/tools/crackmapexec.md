---
type: tool
title: CrackMapExec (CME / NetExec)
category: enumeration
tags: [ad, windows, smb, ldap, spray]
updated: 2026-07-09
---

# CrackMapExec (CME / NetExec)

## What it does
Swiss-armyknife for SMB/WinRM/LDAP/MSSQL: credential validation, spraying, share/user enumeration, module-based exploitation, and hash dumping. **Actively maintained fork: [NetExec](https://github.com/Pennyw0rth/NetExec)** (`nxc`) — prefer it; CME is deprecated.

## Common usage
```
cme smb <ip> -u <user> -p '<pw>' -k               # validate creds (Kerberos)
cme smb <ip> -u <user> -p '<pw>' -k --shares      # enumerate shares
cme ldap <ip> -u <user> -p '<pw>' -k --users      # dump users + descriptions
cme smb <ip> -u 'DC$' -H <hash> --ntds            # DCSync via machine account
```

## Used on
- [[absolute]] — cred checks, share/user enumeration (leaked `svc_smb`'s description → [[ldap-description-credential]]), and the DCSync (`--ntds`) via the `DC$` hash.
