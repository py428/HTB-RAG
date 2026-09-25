---
type: machine
title: Meta
platform: htb
os: linux
difficulty: medium
tags: [linux, web, imagemagick, privesc]
solved: 2026-07-09
sources: [[htb-meta]]
related: []
---
# Meta
> Linux medium box focusing on image processing, featuring ExifTool CVE exploitation, ImageMagick command injection via polyglot file, and neofetch configuration abuse for root.

## Attack path
1. Exploit [[exiftool-cve]] (CVE-2021-22204) via DjVu file upload for www-data shell
2. [[command-injection]] via ImageMagick CVE-2020-29599 using SVG/MSL polyglot file
3. Use [[cronjob-hijack]] to exploit mogrify cron running as thomas
4. Abuse neofetch [[configuration-escalation]] with XDG_CONFIG_HOME for root shell

## Techniques used
- [[exiftool-cve]] — CVE-2021-22204 arbitrary code execution via DjVu metadata
- [[command-injection]] — ImageMagick CVE-2020-29599 via SVG/MSL polyglot file
- [[cronjob-hijack]] — Abusing ImageMagick processing cron for user escalation
- [[ssh-key-reuse]] — Using SSH private key found in thomas' home directory
- [[configuration-escalation]] — Neofetch config file abuse for privilege escalation

## Tools used
- [[nmap]]
- [[exiftool]]
- [[wfuzz]]
- [[feroxbuster]]
- exploit-CVE-2021-22204.py
- [[pspy]]
- [[ssh]]
- [[curl]]

## Services / ports
- [[ssh]] (22)
- [[http]] (80)

## Lessons / notes
- ExifTool processes DjVu files and is vulnerable to CVE-2021-22204
- SVG/MSL polyglot files can inject commands into ImageMagick processing
- Pspy detects cron jobs and background processes
- Neofetch reads config from XDG_CONFIG_HOME which can be set via sudo
- Sudo rules can preserve environment variables (env_keep) for exploitation
