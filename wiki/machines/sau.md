---
type: machine
title: Sau
platform: htb
os: linux
difficulty: easy
tags: [linux, web, ssrf, command-injection, privesc]
solved: 2026-07-09
sources: [[htb-sau]]
related: []
---
# Sau

> Easy Linux box with request-baskets service vulnerable to SSRF, allowing exploitation of internal Maltrail service via command injection, then abusing systemctl with less pager for privilege escalation.

## Attack path

1. [[ssrf]] — Exploit CVE-2023-27163 in request-baskets for internal access
2. [[command-injection]] — Exploit Maltrail login username parameter for RCE
3. [[less-pager-escape]] — Abuse systemctl status with less pager to get root shell

## Techniques used

- [[ssrf]] — CVE-2023-27163 in request-baskets 1.2.1 allows accessing internal services
- [[command-injection]] — Maltrail v0.53 login page username parameter vulnerable to OS command injection
- [[less-pager-escape]] — systemctl status output piped to less, `!sh` command executes as root

## Tools used

- [[nmap]] — Port scanning identifying filtered ports and services
- [[feroxbuster]] — Directory brute force on web services
- curl — HTTP requests and SSRF exploitation
- [[netcat]] — Reverse shell listener
- CVE-2023-27163 exploit script — SSRF automation

## Services / ports

- [[ssh]] — 22/tcp
- [[http]] — 55555/tcp — Request-baskets service vulnerable to SSRF
- Filtered [[http]] — 80/tcp — Internal Maltrail service
- Filtered unknown — 8338/tcp — Internal Maltrail service

## Lessons / notes

- SSRF allows accessing internal Maltrail service on localhost ports 80 and 8338
- Maltrail login vulnerable: username parameter injected with backticks for command execution
- Base64 encoded reverse shell payload to avoid special characters
- `sudo systemctl status trail.service` triggers less pager in small terminal
- Less pager `!sh` command spawns shell with pager's privileges (root)
- Service restarts every time status is checked, making exploitation reliable
