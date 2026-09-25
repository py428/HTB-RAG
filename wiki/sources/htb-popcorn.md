---
type: source
title: "HTB Popcorn writeup"
raw: raw/htb-popcorn.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[popcorn]]
---
# Source: HTB Popcorn writeup
> Medium HackTheBox Linux box featuring torrent upload webshell exploitation and PAM MOTD / DirtyCow privilege escalation on Ubuntu 9.10.
## Key facts extracted
- Torrent Hoster application on /torrent allows image upload for torrent thumbnails
- Upload checks Content-Type header but not file extension or magic bytes
- Uploaded files accessible via `/torrent/upload/<hash>.php` for direct execution
- CVE-2010-0832: PAM MOTD vulnerability allows any user to own arbitrary files via ~/.cache symlink
- Matt user denied SSH login but password reuses between SSH key and system
- Ubuntu 9.10 Karmic runs kernel 2.6.31, vulnerable to DirtyCow exploit
## Filed into
[[popcorn]], [[file-upload-bypass]], [[cve-2010-0832]], [[dirty-cow]], [[password-cracking]]
