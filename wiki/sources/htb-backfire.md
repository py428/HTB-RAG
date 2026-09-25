---
type: source
title: "HTB Backfire writeup"
raw: raw/htb-backfire.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[backfire]]
---
# Source: HTB Backfire writeup

> Comprehensive writeup for HackTheBox machine Backfire covering C2 framework exploitation, SSRF chaining, websocket attacks, and privilege escalation through iptables abuse.

## Key facts extracted
- Havoc C2 management port 4006 accessible only via localhost with leaked credentials from havoc.yaotl
- CVE-2024-41570: Unauthenticated SSRF in Havoc demon callback handling
- CVE-2024-41571: Authenticated RCE in Havoc teamserver via command injection in service name
- HardHatC2 default JWT secret: "jtee43gt-6543-2iur-9422-83r5w27hgzaq" from GitHub
- Sudo rule allows /usr/sbin/iptables and /usr/sbin/iptables-save as root

## Filed into
[[backfire]], [[ssrf]], [[websocket-exploitation]], [[jwt-forgery]], [[c2-exploitation]], [[iptables-arbitrary-write]]
