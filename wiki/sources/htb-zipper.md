---
type: source
title: "HTB Zipper writeup"
raw: raw/htb-zipper.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[zipper]]
---
# Source: HTB Zipper writeup
> Comprehensive writeup covering Zipper Zabbix server exploitation including multiple paths to shell via API abuse and agent communication, SUID binary path hijacking, and systemd service manipulation for privilege escalation.

## Key facts extracted
- Zabbix API allows script creation and execution on monitored hosts
- Multiple exploitation paths: API direct execution, GUI access, agent communication
- SUID binary zabbix-service calls systemctl without absolute path
- Writable systemd service file purge-backups.service for root execution
- Database credentials in Zabbix config grant admin GUI access

## Filed into
[[zipper]], [[zabbix-api-abuse]], [[zabbix-script-execute]], [[zabbix-agent-communication]], [[path-hijacking]], [[systemd-service-hijack]]