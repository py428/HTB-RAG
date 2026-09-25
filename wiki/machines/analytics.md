---
type: machine
title: Analytics
platform: htb
os: linux
difficulty: easy
tags: [web, docker, container, linux, privesc, kernel]
solved: 2026-07-09
sources: [[htb-analytics]]
related: []
---
# Analytics

> Analytics is a data analytics firm running Metabase that can be exploited via a pre-auth RCE vulnerability to gain access to a Docker container, then escape using the GameOver(lay) kernel vulnerability.

## Attack path

1. [[metabase-cve-2023-38646]] — Exploit pre-auth RCE in Metabase via setup token leak
2. [[container-escape]] — Find credentials in container environment variables
3. [[container-escape-gameoverlay]] — Exploit OverlayFS vulnerability to escalate to root

## Techniques used

- [[metabase-cve-2023-38646]] — Pre-authentication RCE in Metabase via setup token leak and H2 database trigger injection
- [[container-enumeration]] — Identifying Docker container environment and extracting credentials from environment variables
- [[container-escape-gameoverlay]] — Kernel exploit for OverlayFS to gain root privileges via user namespace manipulation

## Tools used

- [[nmap]] — Port scanning and service identification
- [[ffuf]] — Subdomain fuzzing to discover data.analytical.htb
- curl — HTTP requests and API interaction
- [[netcat]] — Reverse shell listener
- [[chisel]] — Port forwarding and tunneling
- linpeas — Privilege enumeration script
- python3 — Shell upgrade and exploit execution

## Services / ports

- 22/tcp — [[ssh]] — OpenSSH 8.9p1
- 80/tcp — [[http]] — nginx 1.18.0 redirecting to analytical.htb

## Lessons / notes

- Always check for subdomains when doing web fuzzing — data subdomain contained the vulnerable application
- Metabase setup tokens can leak in API responses even after setup is complete
- Docker containers often have sensitive credentials in environment variables
- GameOver(lay) is a compact kernel exploit that fits in a tweet and affects OverlayFS
- Container kernel exploits can provide full system access when the container runs on the host kernel
