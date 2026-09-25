---
type: source
title: "HTB MonitorsFour writeup"
raw: raw/htb-monitorsfour.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[monitorsfour]]
---
# Source: HTB MonitorsFour writeup

> Windows Docker Desktop exploitation walkthrough featuring PHP type juggling authentication bypass, CVE-2025-24367 rrdtool injection, and CVE-2025-9074 Docker API container escape.

## Key facts extracted

- PHP application with type juggling vulnerability in token validation
- Cacti 1.2.28 with CVE-2025-24367 rrdtool command injection vulnerability
- Docker Desktop 4.44.2 running on WSL2 backend with exposed API (CVE-2025-9074)
- Container can reach Docker API at 192.168.65.7:2375 to create containers with host mounts

## Filed into

[[monitorsfour]], [[php-type-juggling]], [[rce]], [[container-escape]], [[docker-mount]]
