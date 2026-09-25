---
type: machine
title: Titanic
platform: htb
os: linux
difficulty: easy
tags: [linux, web, privesc, ad]
solved: 2026-07-09
sources: [[htb-titanic]]
related: []
---
# Titanic
> Titanic is an easy Linux box featuring a Flask booking application with a file read vulnerability that allows accessing the Gitea database. After cracking hashes, the root privilege escalation is achieved through exploiting an ImageMagick vulnerability (CVE-2024-41817) in a cron job.
## Attack path
1. Exploit [[directory-traversal]] in /download endpoint to read arbitrary files including user flag
2. Download and crack Gitea user hashes to get SSH access as developer
3. Analyze ImageMagick script and exploit [[CVE-2024-41817]] via shared library injection
4. Use cron job running magick to create setuid binary for root access
## Techniques used
- [[directory-traversal]] — os.path.join behavior with absolute paths to bypass base directory
- [[hash-cracking]] — PBKDF2-HMAC-SHA256 from Gitea database
- [[CVE-2024-41817]] — ImageMagick library search path hijacking via libxcb.so.1
## Tools used
[[nmap]], [[ffuf]], [[feroxbuster]], [[hashcat]], sqlite3
## Services / ports
- [[ssh]] (22) - OpenSSH 8.9p1
- [[http]] (80) - Apache 2.4.52
## Lessons / notes
- os.path.join drops all previous path components if an absolute path is provided
- Gitea stores PBKDF2 hashes with salt that can be formatted for hashcat
- ImageMagick's library search path can be hijacked for privilege escalation
- Setuid binaries can be created and executed for persistent root access
