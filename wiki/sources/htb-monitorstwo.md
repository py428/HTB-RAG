---
type: source
title: "HTB MonitorsTwo writeup"
raw: raw/htb-monitorstwo.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[monitorstwo]]
---
# Source: HTB MonitorsTwo writeup

> Cacti exploitation walkthrough featuring CVE-2022-46169 command injection, credential cracking, and Docker privilege escalation via SetUID binary abuse.

## Key facts extracted

- Cacti 1.2.22 with CVE-2022-46169 unauthenticated command injection vulnerability
- Authentication bypass via X-Forwarded-For: 127.0.0.1 header
- Docker 20.10.5 vulnerable to CVE-2021-41091/CVE-2021-41103 (container SetUID binary execution)
- MySQL database accessible from container with hashed credentials
- Overlay filesystem allows host execution of container binaries

## Filed into

[[monitorstwo]], [[rce]], [[hash-cracking]], [[docker-privesc]], [[setuid-abuse]]
