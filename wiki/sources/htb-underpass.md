---
type: source
title: "HTB UnderPass writeup"
raw: raw/htb-underpass.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[underpass]]
---
# Source: HTB UnderPass writeup
> Comprehensive walkthrough of UnderPass exploitation from SNMP enumeration to root via Mosh server abuse.

## Key facts extracted
- SNMP accessible on UDP 161 with community string "public"
- daloRADIUS discovered via SNMP data and found at /daloradius path
- Default operator credentials: administrator/radius
- User svcMosh with hash 412DD4759978ACFCC81DEAB01B382403 cracked to "underwaterfriends"
- svcMosh has full sudo on mosh-server binary
- Mosh server requires MOSH_KEY environment variable for authentication

## Filed into
[[underpass]], [[snmp-enumeration]], [[default-credentials]], [[hash-cracking]], [[sudo-abuse]]
