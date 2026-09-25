---
type: machine
title: Race
platform: htb
os: linux
difficulty: hard
tags: [web, linux, privesc, grav, php, cms, ssti]
solved: 2026-07-09
sources: [[htb-race]]
related: []
---
# Race
> Grav CMS-based racing technology box with phpSysInfo credential exposure, password reset manipulation, and multiple RCE paths via CVE-2024-28116 SSTI or malicious theme injection, culminating in a time-of-check/time-of-use (TOCTOU) race condition using named pipes for privilege escalation.

## Attack path
1. Exposed [[phpsysinfo]] reveals backup credentials in process list
2. Access Grav admin panel as backup user, generate site backup to extract password reset tokens
3. Reset patrick user password via token manipulation to gain admin access
4. RCE via [[ssti]] in Twig templates (CVE-2024-28116) or malicious theme upload with proxy interception
5. Pivot to max user using credentials from backup script
6. Exploit [[toctou]] vulnerability in cron script using [[named-pipe]] to replace script between hash check and execution, achieving root

## Techniques used
- [[password-reset-abuse]] — Extract reset tokens from Grav backups to manipulate user passwords
- [[ssti]] — Twig template injection bypassing sandbox to execute system commands
- [[toctou]] — Race condition between MD5 hash verification and script execution using named pipes
- [[named-pipe]] — Hang md5sum process to allow file replacement during TOCTOU window

## Tools used
- [[nmap]] — Port scanning and service detection
- [[feroxbuster]] — Directory brute forcing
- [[netexec]] — SSH credential testing
- [[curl]] — Web requests and payload delivery
- [[john]] — Password hash cracking (attempted)
- [[nc]] — Reverse shell connections
- [[pspy]] — Process monitoring for cron jobs

## Services / ports
- SSH (22) — OpenSSH 8.9p1 Ubuntu
- HTTP (80) — Apache 2.4.52 with Grav CMS and phpSysInfo

## Lessons / notes
- Grav CMS backup files contain sensitive user configuration including password reset tokens
- CVE-2024-28116 allows bypassing Twig sandbox by modifying safe_functions array
- TOCTOU vulnerabilities can be exploited reliably using named pipes to control timing
- Background process execution in containers ran as different user (UID 1000 vs 1337) allowing for process-based jailbreak