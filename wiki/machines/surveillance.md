---
type: machine
title: Surveillance
platform: htb
os: linux
difficulty: medium
tags: [linux, web, php, rce, docker, database, ldap]
solved: 2026-07-09
sources: [[htb-surveillance]]
related: []
---
# Surveillance
> Linux box running Craft CMS (CVE-2023-41892) and ZoneMinder surveillance software. Exploit PHP object injection to get webshell, crack password from database backup, access ZoneMinder panel, then exploit ZoneMinder for command injection and use LD_PRELOAD technique or sudo abuse for root.

## Attack path
1. [[php-object-injection]] — Exploit Craft CMS CVE-2023-41892 (arbitrary object instantiation)
2. [[file-upload-via-crash]] — Crash ImageMagick to preserve temporary file upload
3. [[imagemagick-malicious-msl]] — Write PHP webshell using MSL file and ImageMagick
4. [[database-backup-cracking]] — Extract SHA256 hash from Craft CMS backup and crack
5. [[zoneminder-auth]] — Login to ZoneMinder with cracked credentials
6. [[command-injection]] — Exploit ZoneMinder CVE-2023-26035 (snapshot action)
7. [[ld-preload]] — Abuse ZoneMinder LD_PRELOAD option or [[command-injection]] in zmupdate.pl
8. [[suid-abuse]] — Create SetUID bash binary for root access

## Techniques used
- [[php-object-injection]] — Craft CMS vulnerability allowing arbitrary object instantiation before 4.4.15
- [[file-upload-via-crash]] — Crash ImageMagick process to prevent cleanup of temp uploads
- [[imagemagick-malicious-msl]] — Use Magick Scripting Language to write files via ImageMagick
- [[database-backup-cracking]] — Crack SHA256 hash from SQL backup using hashcat
- [[command-injection]] — ZoneMinder snapshot vulnerable to shell command injection
- [[ld-preload]] — ZoneMinder configuration allows arbitrary shared library injection

## Tools used
[[nmap]], [[feroxbuster]], [[curl]], [[wireshark]], [[hashcat]], [[john]], [[chisel]], [[evil-winrm]], [[gcc]]

## Services / ports
[[http]] (80), [[ssh]] (22), tcp/8080 (ZoneMinder)

## Lessons / notes
- Craft CMS CVE-2023-41892 allows arbitrary object instantiation via conditions controller
- ImageMagick crashes prevent PHP cleanup of temporary uploaded files
- MSL (Magick Scripting Language) can write files when invoked via ImageMagick
- ZoneMinder CVE-2023-26035 exploits missing authorization on snapshot action
- LD_PRELOAD in ZoneMinder configuration allows arbitrary code execution as root