---
type: source
title: "HTB Antique writeup"
raw: raw/htb-antique.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[antique]]
---
# Source: HTB Antique writeup

> Complete walkthrough for HTB Antique box covering HP printer simulation, SNMP password extraction, Telnet command execution, and multiple CUPS vulnerabilities for privilege escalation.

## Key facts extracted

- **Target**: HP JetDirect printer simulation with SNMP and Telnet exposed
- **Initial access**: Password leaked via SNMP OID 1.3.6.1.4.1.11.2.3.9.1.1.13.0
- **Execution**: HP JetDirect exec command provides shell as lp user
- **Privilege escalation**: Multiple paths via CUPS vulnerabilities and PwnKit
- **UDP importance**: Critical SNMP service only visible via UDP scanning

## Filed into

[[antique]], [[snmp-password-leak]], [[cups-cve-2012-5519]], [[pwnkit-cve-2021-4034]]
