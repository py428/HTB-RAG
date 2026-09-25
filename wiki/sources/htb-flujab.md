---
type: source
title: "HTB FluJab writeup"
raw: raw/htb-flujab.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[flujab]]
---
# Source: HTB FluJab writeup
> Hard Linux box with complex web exploitation, SSH attacks, and local privilege escalation. Features cookie manipulation, SQL injection via SMTP, deprecated SSH keys, and screen binary exploitation.

## Key facts extracted
- Multi-domain host acting as CloudFlare-like proxy (ClownWare Proxy)
- Cookie manipulation required to access /?smtp_config and /?whitelist pages
- SMTP reconfiguration to point to attacker server for SQL injection exfiltration
- SQL injection on cancellation form with results sent via email
- Database credentials: sysadm / th3doct0r for Ajenti admin panel
- SSH access via CVE-2008-0166 deprecated Debian OpenSSL keys
- TCP Wrappers (/etc/hosts.allow) controlling SSH access
- screen 4.5.0 SUID binary vulnerable to arbitrary file write exploit

## Filed into
[[flujab]], [[cookie-manipulation]], [[parameter-tampering]], [[sqli]], [[cve-2008-0166]], [[tcp-wrapper]], [[rbash]], [[suid-binary]], [[ld.so.preload]]
