---
type: source
title: "HTB Mirage writeup"
raw: raw/htb-mirage.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[mirage]]
---
# Source: HTB Mirage writeup

> Detailed walkthrough of compromising Mirage, a Hard-level Windows Active Directory box involving DNS hijacking, NATS enumeration, Kerberoasting, cross-session relay attacks, account manipulation, GMSA password reading, and ESC10 certificate abuse for Domain Admin access.

## Key facts extracted
- Domain name: mirage.htb with Domain Controller DC01
- Missing DNS record nats-svc.mirage.htb allows DNS hijacking attack
- NATS service on port 4222 stores authentication logs with domain credentials
- Default pi/raspberry credentials allowed SSH access to Mirai Raspberry Pi (separate device)
- Multiple escalation paths including Kerberoasting, cross-session relay, and ESC10
- Escalation chain: david.jjackson → nathan.aadam → mark.bbond → javier.mmarshall → Mirage-Service$ → Administrator

## Filed into
[[mirage]], [[dns-hijacking]], [[nats]], [[kerberoasting]], [[cross-session-relay]], [[password-reset]], [[account-manipulation]], [[gmsa]], [[adcs]], [[shadow-credentials]], [[rbcd]], [[dcsync]]
