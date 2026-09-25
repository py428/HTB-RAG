---
type: source
title: "HTB Surveillance writeup"
raw: raw/htb-surveillance.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[surveillance]]
---
# Source: HTB Surveillance writeup
> Linux server running Craft CMS and ZoneMinder surveillance software. Exploits chain: Craft CMS PHP object injection (CVE-2023-41892) for initial shell, database password extraction for user access, ZoneMinder authentication via reused credentials, then ZoneMinder command injection (CVE-2023-26035) or LD_PRELOAD abuse for privilege escalation.

## Key facts extracted
- Craft CMS version 4.4.14 vulnerable to CVE-2023-41892 (arbitrary object instantiation)
- ImageMagick crash trick preserves temporary file uploads for MSL exploitation
- Database backup contains SHA256 hash: 39ed84b22ddc63ab3725a1820aaa7f73a8f3f10d0848123562c9f35c675770ec
- Cracked password: starcraft122490 (works for both matthew and admin users)
- ZoneMinder version 1.36.32 vulnerable to CVE-2023-26035 (unauthenticated RCE via snapshot)
- zoneminder user can run zm*.pl scripts as any user via sudo
- LD_PRELOAD option in ZoneMinder allows privilege escalation

## Filed into
[[surveillance]], [[php-object-injection]], [[file-upload-via-crash]], [[imagemagick-malicious-msl]], [[database-backup-cracking]], [[command-injection]], [[ld-preload]], [[suid-abuse]]