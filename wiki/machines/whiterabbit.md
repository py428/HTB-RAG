---
type: machine
title: WhiteRabbit
platform: htb
os: linux
difficulty: insane
tags: [linux, web, sqli, wifi, container, prng-prediction, command-injection, docker]
solved: 2026-07-09
sources: [[htb-whiterabbit]]
related: []
---
# WhiteRabbit
> WhiteRabbit is an insane Linux box featuring a complex web application stack with Uptime Kuma, WikiJS, and n8n automation. The attack path involves bypassing Uptime Kuma login, discovering WikiJS documentation that reveals SQL injection in an n8n webhook, using mitmproxy to add required signatures for sqlmap exploitation, recovering SSH keys from restic backups, exploiting container escape via restic command injection, and PRNG prediction to generate passwords based on leaked timestamps.

## Attack path
1. [[websocket-manipulation]] on Uptime Kuma login response → admin session bypass
2. [[status-page-enumeration]] via feroxbuster → discover additional subdomains
3. [[sql-injection]] in n8n webhook with [[signature-bypass]] via mitmproxy → database access
4. [[backup-forensics]] in restic backup → recover SSH keys for container
5. [[container-escape]] via restic command injection → root on container, find morpheus SSH keys
6. [[prng-prediction]] using leaked timestamp from command log → generate neo's password
7. [[sudo-abuse]] as neo → root on host

## Techniques used
- [[websocket-manipulation]] — Intercepted and modified Uptime Kuma login websocket response to bypass authentication
- [[sql-injection]] — Exploited n8n webhook email parameter vulnerable to time-based blind SQL injection
- [[signature-bypass]] — Used mitmproxy to automatically add HMAC-SHA256 signatures to bypass webhook validation
- [[backup-forensics]] — Analyzed restic backup commands found in database to recover SSH key archive
- [[command-injection]] — Exploited restic --password-command parameter for arbitrary command execution
- [[container-escape]] — Escaped Docker container via restic SUID binary to access host SSH keys
- [[prng-prediction]] — Predicted password generator output using leaked timestamp and C rand() implementation
- [[sudo-abuse]] — Neo user has full sudo access (ALL : ALL) ALL for privilege escalation

## Tools used
- [[nmap]], [[ffuf]], [[feroxbuster]], [[sqlmap]], [[mitmproxy]], [[curl]], [[hydra]], [[john]], [[hashcat]], [[7z]], [[ssh]], [[netcat]]

## Services / ports
- 22/tcp — [[ssh]] (OpenSSH 9.6)
- 80/tcp — [[http]] (Caddy) → Uptime Kuma v1.23.13, WikiJS
- 2222/tcp — [[ssh]] (container)
- 53/udp — [[dns]]

## Lessons / notes
- Websocket responses can be manipulated to bypass authentication even when intercepted
- Webhook signature validation can be bypassed with automated proxy tools
- Database logs may contain sensitive backup commands and timestamps
- Restic SUID binary can be exploited for command execution despite being a backup tool
- PRNG using system time as seed can be predicted if timestamp is known
- Container breakouts often involve finding credentials for the host system
- Multiple privilege escalation paths may exist (container + host)
- Complex application stacks require thorough enumeration of all components
