---
type: source
title: "HTB BabyTwo writeup"
raw: raw/htb-babytwo.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[babytwo]]
---
# Source: HTB BabyTwo writeup
> Complete walkthrough of exploiting an AD environment through password spraying, SYSVOL manipulation, and GPO abuse for privilege escalation.

## Key facts extracted
- Guest authentication enabled for SMB share enumeration
- Username-as-password credentials work for multiple accounts
- SYSVOL scripts writable and execute on user login
- BloodHound analysis reveals ACL abuse opportunities
- GPO management accounts have GenericAll over critical GPOs
- pyGPOAbuse can inject commands into GPO scheduled tasks

## Filed into
[[babytwo]], [[password-spray]], [[logon-script-poisoning]], [[acl-abuse]], [[gpo-abuse]]
