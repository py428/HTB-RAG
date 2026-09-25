---
type: source
title: "HTB Bamboo writeup"
raw: raw/htb-bamboo.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[bamboo]]
---
# Source: HTB Bamboo writeup

> Comprehensive writeup for HackTheBox machine Bamboo covering Squid proxy enumeration, PaperCut NG exploitation, CVE-2023-27350 authentication bypass, and binary hijacking for privilege escalation.

## Key facts extracted
- Squid proxy 5.9 on port 3128 allowing access to internal services
- PaperCut NG 22.0 on ports 9191/9192/9195 with authentication bypass vulnerability
- CVE-2023-27350: Authentication bypass in SetupCompleted class (CVSS 9.8)
- Root process executes /home/papercut/server/bin/linux-x64/server-command
- Papercut user has full control over server-command binary and directory

## Filed into
[[bamboo]], [[proxy-enumeration]], [[cve-2023-27350]], [[papercut-rce]], [[binary-hijack]], [[setuid-exploitation]]
