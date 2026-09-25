---
type: technique
title: RPC Null Session Enumeration
tags: [ad, windows, rpc, smb, reconnaissance]
platforms: [windows]
mitre: [T1087.002]
updated: 2026-07-09
---

# RPC Null Session Enumeration

## What it is
Bind to a Windows host's RPC interface over SMB (445) with an empty session (null credentials) and
enumerate users, groups, RIDs, shares, and password policy — no credentials needed when null
sessions are permitted. The SMB-era analogue of anonymous LDAP/RPC enumeration.

## When it works
- The target permits null-session RPC binds — common on older or default-config DCs; disabled where
  `RestrictAnonymous` / SMB signing+enforcement is tightened.

## How it's done
```
rpcclient -U "" -N <ip>
rpcclient $> enumdomusers        # users + RIDs
rpcclient $> enumdomgroups       # groups
rpcclient $> querygroup 0x200    # group detail
rpcclient $> querygroupmem 0x200 # members of a group
rpcclient $> queryuser 0x1f4     # user detail
```
Also: `enum4linux -a`, `crackmapexec smb --users`, `lookupsid.py` (RID cycling → usernames).

## Observed on
- [[forest]] — null session enumerated the full user list (`svc-alfresco`, `andy`, `lucinda`, …) and
  groups (incl. Exchange groups), seeding the AS-REP roast.

## Variants & pitfalls
- Often disabled on modern/hardened hosts (contrast [[absolute]], where even authenticated NTLM was
  blocked) — a live null session signals a loosely-configured legacy DC.
- RID cycling (`lookupsid.py`) can recover usernames even when `enumdomusers` is restricted.

## See also
[[kerberos-username-enumeration]], [[as-rep-roasting]], [[smb]]
