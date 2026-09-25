---
type: source
title: "HTB Time writeup"
raw: raw/htb-time.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[time]]
---
# Source: HTB Time writeup
> Complete walkthrough for HackTheBox Time machine covering exploitation of a Jackson JSON deserialization vulnerability (CVE-2019-12384) for initial access and Systemd timer script hijacking for privilege escalation.
## Key facts extracted
- Jackson JSON deserialization via H2 database SQL initialization (CVE-2019-12384)
- Systemd timer running world-writable script as root
- Ubuntu 20.04 target with OpenSSH 8.2p1 and Apache 2.4.41
- SSH 22, HTTP 80 open
## Filed into
[[time]], [[CVE-2019-12384]], [[systemd-timer-hijack]]
