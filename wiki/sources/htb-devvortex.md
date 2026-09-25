---
type: source
title: "HTB DevVortex writeup"
raw: raw/htb-devvortex.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[devvortex]]
---
# Source: HTB DevVortex writeup
> Exploitation of Joomla CVE-2023-23752 for information disclosure leading to admin access, followed by webshell deployment, database hash cracking, and apport-cli privilege escalation.

## Key facts extracted
- Joomla 4.2.6 vulnerable to CVE-2023-23752 information disclosure
- API endpoints /api/index.php/v1/users and /api/index.php/v1/config/application accessible without auth
- MySQL credentials: lewis/P4ntherg0t1n5r3c0n## for joomla database
- Two users: lewis (admin) and logan paul with bcrypt password hashes
- logan password cracks to "tequieromucho" using hashcat mode 3200
- apport-cli 2.20.11 vulnerable to CVE-2023-1326 pager escape

## Filed into
[[devvortex]], [[cve-2023-23752]], [[joomla-rce]], [[webshell]], [[sql]], [[hash-cracking]], [[cve-2023-1326]]
