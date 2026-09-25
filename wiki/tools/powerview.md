---
type: tool
title: PowerView
category: enumeration
tags: [ad, windows, powershell, acl]
updated: 2026-07-09
---

# PowerView

## What it does
PowerShell module (PowerSploit) for AD reconnaissance and ACL/object manipulation from a Windows
session: enumerate users/groups/OU/GPO, query ACL edges, and abuse them (`Add-DomainObjectAcl`,
`Add-DomainGroupMember`, `Set-DomainObject`). The non-graphical counterpart to BloodHound's edges —
the engine behind most DACL-abuse one-liners. (Created here on its **2nd sighting**, per the
page-creation policy.)

## Common usage
```
Add-DomainGroupMember -Identity '<group>' -Members '<you>' -Credential $cred
Add-DomainObjectAcl -Credential $cred -PrincipalIdentity '<you>' -TargetIdentity '<DOMAIN>' -Rights DCSync
```

## Used on
- [[absolute]] — Windows-side group/ACL edits in the shadow-credential chain.
- [[forest]] — joined "Exchange Windows Permissions" and granted DCSync rights.
