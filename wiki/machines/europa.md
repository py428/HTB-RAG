---
type: machine
title: Europa
platform: htb
os: linux
difficulty: medium
tags: [linux, web, sqli]
solved: 2026-07-09
sources: [[htb-europa]]
related: []
---
# Europa
> Linux box featuring SQL injection authentication bypass on admin portal, PHP preg_replace RCE via /e modifier for code execution, and cron job abuse for privilege escalation to root.

## Attack path
1. [[sqli-auth-bypass]] on login.php to access admin panel
2. [[preg-replace-rce]] via tools.php using /e modifier to execute PHP code
3. [[cronjob-hijack]] — Create malicious logcleared.sh executed by root cron

## Techniques used
- [[sqli-auth-bypass]] — Bypassing login by injecting SQL comments after username
- [[sqlmap]] — Automated SQL injection to dump database and extract credentials
- [[preg-replace-rce]] — Abusing PHP preg_replace /e modifier to execute arbitrary code
- [[cronjob-hijack]] — Creating script in writable directory executed by root cron job

## Tools used
- [[nmap]], [[sqlmap]], [[wfuzz]], [[netcat]]

## Services / ports
- [[ssh]] (22), [[http]] (80/443)

## Lessons / notes
- SQL injection can often bypass authentication without valid credentials
- PHP preg_replace with /e modifier evaluates replacement string as PHP code
- Multi-stage exploitation: SQLi → auth bypass → code execution → privilege escalation
- Cron jobs calling scripts from writable directories are privilege escalation vectors
- Apache virtual hosts may reveal additional subdomains via SSL certificates
- Default Apache pages indicate presence; require further enumeration
