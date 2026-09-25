---
type: source
title: "HTB Mischief writeup"
raw: raw/htb-mischief.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[mischief]]
---
# Source: HTB Mischief writeup

> Comprehensive guide to compromising Mischief, an Insane-level Linux box focusing on IPv6 enumeration, SNMP credential harvesting, command injection with output filtering, and ACL exploitation for privilege escalation.

## Key facts extracted
- IPv6 address: dead:beef::250:56ff:feb2:7cff (changes on reset)
- SNMP community string: public (allows unrestricted read access)
- Web credentials: administrator:trickeryanddeceit (from basic auth brute force)
- Command injection filter blocks nc, bash, chown, chmod, perl, find, locate, ls, php, wget, curl, dir, ftp, telnet
- loki credentials: loki:lokiisthebestnorsegod (from /home/loki/credentials)
- loki restricted from running su via ACL: user:loki:r-- on /bin/su
- Original root.txt location: /usr/lib/gcc/x86_64-linux-gnu/7/root.txt

## Filed into
[[mischief]], [[snmp]], [[ipv6-enumeration]], [[command-injection]], [[acl]]
