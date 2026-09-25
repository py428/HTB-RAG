---
type: source
title: "HTB VulnCicada writeup"
raw: raw/htb-vulncicada.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[vulncicada]]
---
# Source: HTB VulnCicada writeup
> 0xdf's complete writeup for HTB VulnCicada covering NFS enumeration, credential extraction from image, ADCS ESC8 exploitation via Kerberos relay using malicious DNS records and PetitPotam coercion, and final privilege escalation through DCSync.

## Key facts extracted
- NFS share /profiles exposed with user profile directories
- Password found in marketing.png image: Cicada123 for Rosie.Powell
- ADCS ESC8 vulnerability on web enrollment HTTP endpoint
- Linux exploitation path: Malicious DNS record with serialized SPN + PetitPotam coercion
- Kerberos relay trick: DC authenticates via Kerberos to malicious record, relayed to ADCS
- Machine account certificate: Provides TGT and NT hash for DC-JPQ225$ account
- Alternative Windows path: RemoteKrbRelay.exe on domain-joined Windows machine

## Filed into
[[vulncicada]], [[nfs-enumeration]], [[credential-from-image]], [[adcs-esc8]], [[kerberos-relay]], [[petitpotam]], [[dcsync]]
