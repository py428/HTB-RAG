---
type: source
title: "HTB Certified writeup"
raw: raw/htb-certified.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[certified]]
---
# Source: HTB Certified writeup

> Detailed walkthough for HTB Certified assume-breach box featuring ACL abuse chains, shadow credential attacks, and ESC9 ADCS exploitation.

## Key facts extracted
- First HTB assume-breach box starting with low-privileged user (judith.mader)
- judith.mader has WriteOwner on Management group (not patched after release)
- Management group has GenericWrite over management_svc user
- management_svc has GenericAll over ca_operator user
- ca_operator can enroll in CertifiedAuthentication template vulnerable to ESC9
- ESC9 exploitation requires modifying target UPN to "Administrator" for certificate request
- StrongCertificateBindingEnforcement not set to 2 allows ESC9 attack
- BloodHound CE requires bloodhound-python collector from specific branch

## Filed into
[[certified]], [[acl-abuse]], [[shadow-credentials]], [[adcs-esc9]], [[writeowner]], [[genericall]]
