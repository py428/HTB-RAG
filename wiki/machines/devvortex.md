---
type: machine
title: DevVortex
platform: htb
os: linux
difficulty: easy
tags: [linux, web, joomla, mysql, sudo, privilege-escalation]
solved: 2026-07-09
sources: [[htb-devvortex]]
related: []
---
# DevVortex
> Joomla 4.2.6 server vulnerable to CVE-2023-23752 information disclosure, exposing database credentials and user list. Initial access via template modification or plugin webshell, then password cracking from database hashes. Privilege escalation via CVE-2023-1326 in apport-cli pager escape.

## Attack path
1. [[cve-2023-23752]] — Exploit Joomla information disclosure to leak database credentials and user list
2. [[joomla-rce]] — Modify template or upload plugin webshell for code execution
3. [[hash-cracking]] — Crack bcrypt hashes from Joomla database
4. [[cve-2023-1326]] — Escape apport-cli pager to get root shell

## Techniques used
- [[cve-2023-23752]] — Joomla API access bypass via public parameter override exposes configuration and users
- [[webshell]] — Edit Joomla error.php template or upload plugin for persistent code execution
- [[sql]] — Query Joomla database to extract password hashes
- [[hash-cracking]] — Crack bcrypt hashes with hashcat using rockyou.txt
- [[cve-2023-1326]] — apport-cli less pager escape when viewing crash reports with sudo

## Tools used
[[nmap]], [[ffuf]], [[feroxbuster]], [[curl]], [[mysql]], [[hashcat]], [[ssh]], [[python]]

## Services / ports
- [[ssh]] (22) — OpenSSH 8.2p1 Ubuntu
- [[http]] (80) — nginx 1.18.0
- MySQL — localhost only

## Lessons / notes
- CVE-2023-23752 affects Joomla 4.0.0-4.2.7, exposing APIs without authentication
- Database credentials often reused between applications and user accounts
- Template modification provides persistent webshell access to CMS systems
- apport-cli pager escape similar to other less-based privilege escalations
- Virtual host fuzzing essential for finding admin interfaces on shared hosts
