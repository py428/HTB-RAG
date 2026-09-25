---
type: tool
title: BloodHound
category: enumeration
tags: [ad, graph, attack-path]
updated: 2026-07-09
---

# BloodHound

## What it does
Maps Active Directory relationships (users/groups/computers/GPOs and the ACL edges between them) as a graph, then finds attack paths (e.g. "owned user X → AdminTest on Y"). The collector is `bloodhound-python` (Linux) or SharpHound (Windows); the GUI visualises and gives abuse commands.

## Common usage
```
bloodhound-python -u <user> -p '<pw>' -k -d <domain> -dc <dc> -c ALL --zip
# drag the zip into the BloodHound GUI; mark owned principals; run queries
```

## Used on
- [[absolute]] — revealed `m.lovegod`'s ownership of "Network Audit" and that group's `GenericWrite` on `winrm_user`, which drove [[dacl-write-members]] → [[shadow-credentials]].
- [[forest]] — SharpHound surfaced the Account Operators → Exchange Windows Permissions → domain `WriteDacl` path.
