---
type: source
title: "HTB Sightless writeup"
raw: raw/htb-sightless.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[sightless]]
---
# Source: HTB Sightless writeup
> Walkthrough of SQLPad SSTI exploitation, container escape via hash cracking, and Froxlor XSS for privilege escalation.
## Key facts extracted
- SQLPad running version vulnerable to CVE-2022-0944 (SSTI in connection test)
- Container has michael user with cracked password: insaneclownposse
- Froxlor vulnerable to CVE-2024-34070 (stored XSS in login logs)
- Keepass database on FTP contains root SSH private key
- Froxlor admin panel on localhost:8080
## Filed into
[[sightless]], [[ssti]], [[hash-cracking]], [[xss]], [[ftp-access]]
