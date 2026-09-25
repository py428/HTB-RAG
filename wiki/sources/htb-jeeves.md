---
type: source
title: "HTB Jeeves writeup"
raw: raw/htb-jeeves.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[jeeves]]
---
# Source: HTB Jeeves writeup
> Medium Windows machine with unauthenticated Jenkins, KeePass database cracking, pass-the-hash, and NTFS alternate data streams.

## Key facts extracted
- Jenkins on port 50000 at /askjeeves, no authentication required
- kohsuke user has CEH.kdbx KeePass database in Documents
- Master password: moonshine1 (cracked with keepass2john + hashcat)
- "Backup stuff" entry contains Administrator NT hash: e0fb1fb85756c24235ff238cbe81fe00
- LM hash aad3b435b51404eeaad3b435b51404ee (empty password indicator)
- Pass-the-hash successful with psexec.py for SYSTEM access
- root.txt hidden in alternate data stream: hm.txt:root.txt
- Jetty 9.4.z-SNAPSHOT running Jenkins

## Filed into
[[jeeves]], [[jenkins-rce]], [[keepass-cracking]], [[pass-the-hash]], [[alternate-data-stream]]
