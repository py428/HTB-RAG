---
type: source
title: "HTB Writer writeup"
raw: raw/htb-writer.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[writer]]
---
# Source: HTB Writer writeup
> Complete walkthrough of Writer HackTheBox machine covering SQL injection exploitation, command injection via image upload, Django password cracking, Postfix mail filter abuse, and apt configuration manipulation.
## Key facts extracted
- CMS Made Simple vulnerable to authentication bypass SQLi
- MySQL database with FILE privileges allowing file read operations
- Image upload via file:// URLs with command injection in filename
- Django web application on localhost:8080 with SQLite database
- PBKDF2_SHA256 password hash for kyle user
- Postfix mail filter script running as john user
- apt configuration directory writable by management group
## Filed into
[[writer]], [[sqli]], [[command-injection]], [[django-cracking]], [[postfix-abuse]], [[apt-config-abuse]], [[linux]], [[web]]
