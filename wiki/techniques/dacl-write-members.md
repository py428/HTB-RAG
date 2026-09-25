---
type: technique
title: Self-Add to Group via DACL Write (WriteMembers / GenericWrite)
tags: [ad, windows, acl-abuse, privilege-escalation]
platforms: [windows]
mitre: [T1484, T1222]
updated: 2026-07-09
---

# Self-Add to Group via DACL Write

## What it is
When you control (own) a group but aren't a member, or hold `WriteDacl`/`WriteOwner`/`GenericWrite` on a group object, you can grant yourself the **`WriteMembers`** (add-self) permission and then add your account to the group — inheriting whatever privileges that group carries (often `GenericWrite` on a high-value user, enabling [[shadow-credentials]]).

## When it works
- You own the group (`WriteDacl` / `WriteOwner` / `GenericAll`), **or**
- You have `WriteMembers` already, **or**
- BloodHound shows an inherited `AddMember`/`GenericWrite` edge.

## How it's done
Linux path (Impacket + samba):
```
# Grant m.lovegod WriteMembers on "Network Audit" (uses creds, no ticket)
dacledit.py -k 'absolute.htb/m.lovegod:<pw>' -dc-ip dc.absolute.htb \
  -principal m.lovegod -target "Network Audit" -action write -rights WriteMembers

# Then add self to the group
net rpc group addmem "Network Audit" m.lovegod -U 'm.lovegod' --use-kerberos=required -S dc.absolute.htb
```
Windows path (PowerView): `Add-DomainObjectAcl -Rights All` then `Add-DomainGroupMember`.

Tools: [[impacket]] `dacledit.py` (ShutdownRepo `dacledit` branch), samba `net`, PowerView.

## Observed on
- [[absolute]] — `m.lovegod` owned "Network Audit" → wrote `WriteMembers` → joined the group, which held `GenericWrite` on `winrm_user` → chained straight into [[shadow-credentials]].

## Variants & pitfalls
- On this box a **reversion script** periodically reset group memberships; if a step failed, restart from the DACL write.
- When using a Kerberos ticket for the `net` commands, delete & re-`kinit` between identity changes or you hit stale-credential errors.
- `dacledit.py` auto-backs up the original DACL (`.bak`) — restore after.

## See also
[[shadow-credentials]], [[ntlm-disabled-protected-users]], [[impacket]]
