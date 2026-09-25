---
type: source
title: "HTB Sunday writeup"
raw: raw/htb-sunday.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[sunday]]
---
# Source: HTB Sunday writeup
> Easy Solaris box featuring finger service for user enumeration, password cracking for user escalation, and multiple wget privilege escalation techniques for root access.
## Key facts extracted
- Solaris 11 (SunOS 5.11) with finger service on port 79
- Backup shadow file world-readable in /backup directory
- Multiple wget privilege escalation techniques available
- Overwrite script resets troll binary every 5 seconds
- finger protocol can be used for file transfer
## Filed into
[[sunday]], [[finger-enum]], [[password-cracking]], [[sudo-abuse]], [[wget]], [[solaris]]
