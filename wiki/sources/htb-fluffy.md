---
type: source
title: "HTB Fluffy writeup"
raw: raw/htb-fluffy.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[fluffy]]
---
# Source: HTB Fluffy writeup
> Easy Windows AD box with assume-breach scenario. Exploiting recent Windows library-ms vulnerability for initial access, then shadow credentials and ADCS ESC16 for privilege escalation.

## Key facts extracted
- Start with credentials: j.fleischman / J0elTHEM4n1990!
- CVE-2025-24071 / CVE-2025-24054 library-ms vulnerability in Windows Explorer
- p.agila NetNTLMv2 hash capture and crack (prometheusx-303)
- BloodHound analysis reveals GenericWrite over service accounts via Service Account Managers group membership
- winrm_svc and ca_svc service accounts vulnerable to shadow credential attacks
- ESC16 ADCS vulnerability on fluffy-DC01-CA (security extension disabled)

## Filed into
[[fluffy]], [[cve-2025-24071]], [[password-cracking]], [[acl-genericwrite]], [[shadow-credentials]], [[esc16]], [[adcs-template-abuse]]
