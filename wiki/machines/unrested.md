---
type: machine
title: Unrested
platform: htb
os: linux
difficulty: medium
tags: [linux, web, zabbix, sqli, medium]
solved: 2026-07-09
sources: [[htb-unrested]]
related: []
---
# Unrested
> Medium Zabbix monitoring server box featuring SQL injection in the user API, session hijacking, and sudo nmap wrapper abuse for privilege escalation.

## Attack path
1. [[sqli]] in Zabbix `user.get` API via `selectRole` parameter (CVE-2024-42327)
2. [[session-hijacking]] — extract admin session token from database via SQL injection
3. [[rce-zabbix-item]] — create malicious Zabbix item to execute system commands
4. [[sudo-nmap-abuse]] — bypass restrictive nmap wrapper using `-script` instead of `--script`

## Techniques used
- [[sqli]] — SQL injection in Zabbix CUser.get function via `selectRole` parameter with subquery injection
- [[session-hijacking]] — Extract admin session from `sessions` table using group_concat subquery
- [[rce-zabbix-item]] — Zabbix item.create API allows executing system commands via webhook/item configuration
- [[sudo-nmap-abuse]] — Custom nmap wrapper can be bypassed using `-script` flag instead of `--script`

## Tools used
- [[nmap]] — port scanning and service version detection
- [[curl]] — API testing and interaction with Zabbix JSON-RPC API
- netcat — reverse shell listener
- sqlmap — automated SQL injection exploitation

## Services / ports
- [[ssh]] — 22/tcp
- [[http]] — 80/tcp (Apache, Zabbix frontend)
- zabbix-agent — 10050/tcp
- zabbix-trapper — 10051/tcp

## Lessons / notes
- Zabbix 7.0.0 has multiple CVEs including SQLi (CVE-2024-42327) and privilege escalation (CVE-2024-36467)
- SQL injection can be used to extract session tokens for authentication bypass
- Zabbix API allows RCE through item creation when authenticated as admin
- Custom security wrappers can often be bypassed with alternative flag syntax
- MySQL group_concat useful for extracting multiple values in single query
