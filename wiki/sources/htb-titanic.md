---
type: source
title: "HTB Titanic writeup"
raw: raw/htb-titanic.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[titanic]]
---
# Source: HTB Titanic writeup
> Detailed walkthrough for HackTheBox Titanic machine covering directory traversal exploitation, Gitea database analysis, hash cracking, and ImageMagick library hijacking for privilege escalation.
## Key facts extracted
- Flask application with directory traversal via os.path.join absolute path behavior
- Gitea database accessible via file read with PBKDF2 password hashes
- ImageMagick 7.1.1-35 vulnerable to CVE-2024-41817 library hijacking
- Cron job running magick identify on images in writable directory
- Ubuntu 22.04 with Apache 2.4.52 and Python 3.10
## Filed into
[[titanic]], [[directory-traversal]], [[hash-cracking]], [[CVE-2024-41817]]
