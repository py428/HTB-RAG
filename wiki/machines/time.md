---
type: machine
title: Time
platform: htb
os: linux
difficulty: medium
tags: [linux, web, privesc, ad]
solved: 2026-07-09
sources: [[htb-time]]
related: []
---
# Time
> Time is a straightforward Linux box featuring a Jackson JSON deserialization vulnerability (CVE-2019-12384) in a web application that leads to initial shell access. The root privilege escalation involves exploiting a world-writable Systemd timer script that runs as root.
## Attack path
1. Exploit [[CVE-2019-12384]] via JSON deserialization in the online JSON parser web application to get RCE
2. Escalate to root by abusing [[systemd-timer-hijack]] - the timer_backup.sh script is world-writable
## Techniques used
- [[CVE-2019-12384]] — Jackson JSON deserialization via H2 database SQL injection
- [[systemd-timer-hijack]] — World-writable timer script running as root
## Tools used
[[nmap]], [[linpeas]], [[netcat]], python3
## Services / ports
- [[ssh]] (22)
- [[http]] (80) - Apache with JSON parser application
## Lessons / notes
- The CVE-2019-12384 exploit uses H2 database initialization to execute arbitrary SQL via JDBC URL
- Systemd timers running as root with writable scripts are an immediate privesc vector
- Short-lived shells from timers can be stabilized by injecting SSH keys into authorized_keys
