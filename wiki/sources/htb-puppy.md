---
type: source
title: "HTB Puppy writeup"
raw: raw/htb-puppy.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[puppy]]
---

# Source: HTB Puppy writeup

> Complete writeup for HTB Puppy covering Active Directory ACL abuse, KeePassXC password cracking, website backup credential extraction, and DPAPI credential harvesting for administrative access.

## Key facts extracted

- **Initial Creds**: levi.james / KingofAkron2025! (HR group member)
- **ACL Chain**: HR has GenericWrite over Developers → Developers access DEV share → KeePassXC database
- **KeePassXC Cracking**: Argon2 format requiring modern John, password "liverpool"
- **ACL Chain 2**: ant.edwards (Senior Devs) has GenericAll over adam.silver
- **Website Creds**: steph.cooper / ChefSteph2025! from nms-auth-config.xml.bak
- **Final Privesc**: steph.cooper has DPAPI credential for steph.cooper_adm (Administrator)

## Filed into

[[puppy]], [[acl-genericwrite]], [[dacl-write-members]], [[password-spray]], [[acl-genericall]], [[password-reset]], [[acl-forcechangepassword]], [[file-include]], [[dpapi]]
