---
type: machine
title: Snoopy
platform: htb
os: linux
difficulty: hard
tags: [linux, web, dns, cve, ad, privesc]
solved: 2026-07-09
sources: [[htb-snoopy]]
related: []
---
# Snoopy
> Hard Linux box featuring a file read vulnerability to leak DNS configuration, DNS TSIG hijacking to intercept Mattermost password resets, SSH honeypot to capture credentials, and two CVEs (git apply arbitrary file write and ClamAV XXE) for privilege escalation.

## Attack path
1. File read / directory traversal via [[path-traversal]] to leak Bind DNS configuration and TSIG key
2. DNS spoofing via [[dns-tsig]] to intercept Mattermost password reset emails
3. Access Mattermost and abuse slash command to connect to SSH honeypot
4. Capture credentials via [[ssh-honeypot]] and SSH as cbrown
5. Exploit [[cve-2023-23946]] in git apply for arbitrary file write to get SSH as sbrown
6. Exploit [[cve-2023-20052]] (XXE in ClamAV) to read root SSH key

## Techniques used
- [[path-traversal]] — Bypass filtering using ....// in download.php
- [[dns-tsig]] — Use nsupdate with leaked TSIG key to poison DNS
- [[ssh-honeypot]] — Deploy cowrie to capture provisioning credentials
- [[cve-2023-23946]] — Git apply symlink creation for arbitrary file write
- [[cve-2023-20052]] — XXE in DMG files processed by ClamAV

## Tools used
- [[nmap]]
- [[feroxbuster]]
- ffuf
- [[nsupdate]] (dnsutils)
- aiosmtpd
- cowrie
- [[exiftool]]
- [[git]]
- docker
- bbe
- clamscan

## Services / ports
- [[ssh]] (22)
- [[dns]] (53) — Bind 9.18.12 with zone transfer enabled
- [[http]] (80) — nginx with PHP download.php

## Lessons / notes
- Directory traversal can sometimes be bypassed with encoded sequences like ....//
- TSIG keys in DNS configs allow dynamic updates with nsupdate
- Git apply <2.39.1 vulnerable to symlink-based arbitrary writes
- XXE in DMG parsing can leak files via ClamAV debug output
- Mattermost slash commands can be abused for server provisioning
