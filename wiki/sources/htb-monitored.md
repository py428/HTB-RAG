---
type: source
title: "HTB Monitored writeup"
raw: raw/htb-monitored.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[monitored]]
---
# Source: HTB Monitored writeup

> Complete walkthrough of Nagios XI exploitation featuring SNMP credential harvesting, CVE-2023-40931 SQL injection, API abuse for admin creation, and two distinct privilege escalation paths via sudo misconfigurations.

## Key facts extracted

- Nagios XI 5.11.1 with CVE-2023-40931 SQL injection vulnerability
- SNMP enumeration reveals `sudo` command with credentials in process list
- API accessible at `/nagiosxi/api/v1/` with token-based auth
- Multiple sudo entries for Nagios user including service management
- Two privesc paths: binary replacement in `/usr/local/nagios/bin/nagios` OR symlink attack on `getprofile.sh`

## Filed into

[[monitored]], [[snmp-enum]], [[api-abuse]], [[sql-injection]], [[symlink-abuse]], [[sudo-abuse]]
