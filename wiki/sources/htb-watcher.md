---
type: source
title: "HTB Watcher writeup"
raw: raw/htb-watcher.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[watcher]]
---
# Source: HTB Watcher writeup
> Comprehensive guide to exploiting Zabbix CVE-2024-22120 blind SQL injection for session hijacking, SSH tunneling to access TeamCity, credential harvesting through login page modification, and achieving root via CI/CD build pipeline exploitation.

## Key facts extracted
- Zabbix v7.0.0alpha1 vulnerable to CVE-2024-22120 blind SQL injection in audit log clientip parameter
- TeamCity 2024.03.3 running on localhost only port 8111
- Frank user logging in every minute to Zabbix, providing credential harvesting opportunity
- TeamCity build steps execute as root user
- Zabbix database credentials: zabbix:uIy@YyshSuyW%0_puSqA
- Frank credentials: Frank:R%)3S7^Hf4TBobb(gVVs

## Filed into
[[watcher]], [[cve-2024-22120]], [[blind-sql-injection]], [[ssh-tunneling]], [[credential-harvesting]], [[ci-cd-build-exploitation]], [[zabbix]], [[teamcity]]
