---
type: source
title: "HTB Postman writeup"
raw: raw/htb-postman.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[postman]]
---
# Source: HTB Postman writeup
> Easy HackTheBox Linux box featuring Redis abuse for initial access, SSH key cracking for user pivot, and Webmin command injection for root.
## Key facts extracted
- Redis unauthenticated on 6379, allows writing to filesystem via CONFIG dbfilename and SAVE
- Matt user has encrypted SSH key backup at /opt/id_rsa.bak
- Webmin on TCP 10000 uses system authentication (Matt works)
- CVE-2019-12840: Webmin package-updates/update.cgi vulnerable to command injection via pipe
- Redis config has `rename-command MODULE ""` blocking module-based exploits
## Filed into
[[postman]], [[redis-write-ssh]], [[ssh-key-cracking]], [[password-reuse]], [[webmin-command-injection]]
