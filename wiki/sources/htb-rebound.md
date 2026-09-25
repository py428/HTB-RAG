---
type: source
title: "HTB Rebound writeup"
raw: raw/htb-rebound.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[rebound]]
---
# Source: HTB Rebound writeup
> Active Directory marathon with AS-REP roasting enabling Kerberoasting, ACL abuse for group modification, shadow credentials, Kerberos relay attacks, and delegation chains to DC sync.

## Key facts extracted
- jjones account had DONT_REQUIRE_PREAUTH flag enabling AS-REP roasting
- ldap_monitor Kerberoast hash cracked to "1GR8t@$$4u" reused by oorend
- oorend had Self ACL on ServiceMGMT group allowing self-add
- ServiceMGMT had GenericAll over Service Users OU containing winrm_svc
- tbrady could read gmsa_delegator$ password for constrained delegation abuse
- Combined constrained delegation and RBCD to impersonate DC01$ and run DCSync

## Filed into
[[rebound]], [[as-rep-roasting]], [[kerberoasting]], [[acl-self-add]], [[shadow-credentials]], [[kerberos-relay]], [[constrained-delegation]], [[rbcd]], [[dcsync]]