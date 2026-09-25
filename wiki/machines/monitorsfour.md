---
type: machine
title: MonitorsFour
platform: htb
os: windows
difficulty: easy
tags: [cacti, php, web, rce, docker, privesc, windows]
solved: 2026-07-09
sources: [[htb-monitorsfour]]
related: []
---
# MonitorsFour

> Windows host running Docker Desktop with Cacti, exploited via PHP type juggling, rrdtool injection, and Docker API access for container escape.

## Attack path

1. [[subdomain-enumeration]] — find `cacti.monitorsfour.htb` virtual host
2. [[php-type-juggling]] — bypass authentication in `/user?token=0` (loose comparison)
3. [[credential-cracking]] — dump MD5 password hashes and crack admin password
4. [[rce]] — exploit CVE-2025-24367 (rrdtool command injection) for webshell
5. [[container-escape]] — abuse CVE-2025-9074 (Docker Desktop API exposure) from container
6. [[docker-mount]] — create container mounting host `C:` drive and read root flag

## Techniques used

- [[php-type-juggling]] — Loose string comparison (`==`) bypasses token validation with `"0"` matching `"0e..."` strings
- [[rce]] — CVE-2025-24367: newline injection in `cacti_escapeshellarg()` to break out of rrdtool arguments
- [[container-escape]] — CVE-2025-9074: Docker Desktop API accessible from container on 192.168.65.7:2375
- [[docker-mount]] — Bind mount host filesystem into container via Docker API

## Tools used

- [[nmap]], [[netexec]], [[ffuf]], [[curl]], [[hashcat]], [[feroxbuster]]

## Services / ports

- 80/tcp — [[http]] — nginx 1.18.0
- 443/tcp — [[http]] — Apache 2.4.56 (HTTPS, Nagios XI on monitored)
- 5985/tcp — [[winrm]] — Microsoft HTTPAPI 2.0

## Lessons / notes

- PHP type juggling: `"0" == "0e123456789"` evaluates to true (both parse as 0.0 in numeric context)
- CVE-2025-24367: Cacti's custom `cacti_escapeshellarg()` doesn't strip newlines on Windows
- Docker Desktop WSL2 backend exposes API at 192.168.65.7:2375 from containers
- Docker container running privileged allows host filesystem mount via `Binds` in `HostConfig`
