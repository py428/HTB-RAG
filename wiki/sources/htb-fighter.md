---
type: source
title: "HTB Fighter writeup"
raw: raw/htb-fighter.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[fighter]]
---
# Source: HTB Fighter writeup
> 0xdf writeup covering SQL injection, AppLocker bypass techniques, script hijacking, Capcom driver exploitation, and binary reverse engineering. Shows multiple alternative paths and exploitation methods.
## Key facts extracted
- ASP.NET application with SQL injection vulnerable to stacked queries and WAF bypass via case manipulation
- Multiple AppLocker bypass techniques available including 32-bit PowerShell and extensionless executables
- Capcom driver provides reliable SYSTEM privilege escalation
- Custom executable requires reverse engineering to extract hardcoded password
## Filed into
[[fighter]], [[sqli]], [[applocker]], [[script-hijack]], [[capcom-sys]], [[binary-reverse-engineering]]
