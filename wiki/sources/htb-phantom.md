---
type: source
title: "HTB Phantom writeup"
raw: raw/htb-phantom.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[phantom]]
---
# Source: HTB Phantom writeup
> Windows Domain Controller exploitation featuring guest SMB access, password spraying with leaked default credentials, VeraCrypt volume cracking, and BloodHound-guided RBCD abuse without computer object quota for domain compromise.

## Key facts extracted
- Domain: phantom.vl with DC.phantom.vl as Domain Controller
- Default password: Ph4nt0m@5t4rt! found in welcome template PDF
- User enumeration: 30 users via RID cycle as guest
- Valid creds: ibryant@phantom.vl:Ph4nt0m@5t4rt! (password spray)
- VeraCrypt password: Phantom2023! cracked from IT_BACKUP_201123.hc
- Service account: svc_sspr@gB6XTcqVP5MlP7Rc from VyOS backup
- Attack path: ForceChangePassword → AddAllowedToAct → RBCD → DCSync

## Filed into
[[phantom]], [[smb-guest-access]], [[rid-cycle]], [[password-spray]], [[veracrypt-cracking]], [[bloodhound]], [[rbcd]]
