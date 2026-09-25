---
type: source
title: "HTB Jab writeup"
raw: raw/htb-jab.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[jab]]
---
# Source: HTB Jab writeup
> Windows medium difficulty Active Directory box featuring XMPP/Jabber services. Initial access through AS-REP roasting on 2600+ users discovered via Pidgin, followed by DCOM abuse for execution and OpenFire plugin upload for privilege escalation to SYSTEM.

## Key facts extracted
- XMPP server (OpenFire) on multiple ports (5222, 5223, 5262, 5263, 5269, 5270, 5275, 5276, 7070, 7443)
- Pidgin client used to enumerate 2,684 domain users via directory search
- Three users vulnerable to AS-REP roasting (jmontgomery, lbradford, mlowe)
- jmontgomery password cracked: "Midnight_121"
- Private chat room "pentest" contains svc_openfire Kerberoast discussion and password: "!@#$%^&*(1qazxsw"
- svc_openfire has DCOM privileges (MMC20 abuse)
- OpenFire admin panel on localhost:9090 accessible via port forwarding
- CVE-2023-32315: malicious OpenFire plugin leads to SYSTEM execution

## Filed into
[[jab]], [[as-rep-roasting]], [[dcom-abuse]], [[kerberos-username-enumeration]]
