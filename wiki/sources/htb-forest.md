---
type: source
title: "HTB Forest writeup"
raw: raw/htb-forest.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[forest]]
---

# Source: HTB Forest writeup

> 0xdf's walkthrough of **Forest** (easy Exchange/AD DC). RPC null enum → AS-REP roast
> `svc-alfresco` (`s3rvice`) → WinRM → Exchange Windows Permissions `WriteDacl` → grant DCSync
> rights → dump hashes. Beyond-root covers the DCSync ports (445/135/49xxx) and the revert task.

## Key facts extracted
- Domain `htb.local`, 2016 DC, WinRM open.
- RPC null session enumerates users (`svc-alfresco`, `andy`, `lucinda`, `mark`, `santi`, `sebastien`) and groups (incl. Exchange groups).
- `svc-alfresco` is AS-REP-roastable → `s3rvice`; in Remote Management Users → WinRM foothold.
- Escalation: Account Operators → `GenericAll` on "Exchange Windows Permissions" → `WriteDacl` on domain → DCSync rights (`Add-DomainObjectAcl -Rights DCSync`) → `secretsdump.py`.
- A `restore` scheduled task reverts `svc-alfresco` every ~60s (resets password, strips groups/DCSync rights).

## Filed into
[[forest]], [[rpc-null-session]], [[as-rep-roasting]], [[writedacl-grant-dcsync]], [[dcsync]]
