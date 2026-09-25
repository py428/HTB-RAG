---
type: source
title: "HTB Unrested writeup"
raw: raw/htb-unrested.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[unrested]]
---
# Source: HTB Unrested writeup
> Detailed writeup for HTB Unrested covering SQL injection in Zabbix 7.0.0 API, session hijacking through database extraction, RCE via Zabbix item creation, and sudo nmap wrapper bypass.

## Key facts extracted
- Zabbix 7.0.0 vulnerable to SQLi in user.get API (CVE-2024-42327)
- Admin session tokens stored in `sessions` table accessible via injection
- Zabbix item.create API allows command execution with admin privileges
- Custom nmap wrapper script can be bypassed with alternative syntax

## Filed into
[[unrested]], [[sqli]], [[session-hijacking]], [[rce-zabbix-item]], [[sudo-nmap-abuse]]
