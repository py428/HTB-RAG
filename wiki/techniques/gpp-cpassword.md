---
type: technique
title: GPP / cpassword (Group Policy Preferences)
tags: [ad, windows, smb, credential-access, misconfiguration]
platforms: [windows]
mitre: [T1552.006]
updated: 2026-07-09
---

# GPP / cpassword (Group Policy Preferences)

## What it is
Group Policy Preferences let admins embed account passwords in policy XML stored on SYSVOL
(`Policies\{…}\MACHINE\Preferences\Groups\Groups.xml`, and similarly for services, scheduled tasks,
drives, data sources). The password is AES-encrypted as the `cpassword` field — but Microsoft
published the 32-byte key on MSDN, so any domain user (or anonymous reader of a readable share) can
decrypt it. Patched in MS14-025 (2014) to stop *creating* new ones, but **existing cpasswords remain
readable forever**.

## When it works
- Pre-2014 GPP passwords are still sitting in SYSVOL, AND
- You can read the share holding `SYSVOL`/`Policies` — often an anonymous-readable `Replication`
  or `SYSVOL` share, or any authenticated domain user.

## How it's done
```
# grab Groups.xml from a readable share
smbclient //dc/Replication -N
smb: \active.htb\Policies\{…}\MACHINE\Preferences\Groups\> get Groups.xml

# decrypt the cpassword field
gpp-decrypt <cpassword>
```
Also hunt in `Services.xml`, `ScheduledTasks.xml`, `Drives.xml`, `DataSources.xml`. Tools:
`gpp-decrypt`, `Get-GPPPassword` (PowerSploit), Metasploit `smb_enum_gpp`.

## Observed on
- [[active]] — anonymous `Replication` share → `Groups.xml` cpassword → `SVC_TGS` password.

## Variants & pitfalls
- cpassword is base64; an empty cpassword means the account password was set to blank.
- Even patched DCs can be vulnerable — patching only blocks *new* GPP passwords, not old ones.

## See also
[[kerberoasting]], [[smb]]
