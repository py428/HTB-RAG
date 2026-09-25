---
type: source
title: "HTB Zetta writeup"
raw: raw/htb-zetta.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[zetta]]
---
# Source: HTB Zetta writeup
> Complete writeup covering Zetta file sharing service exploitation including FTP bounce attacks for IPv6 discovery, RSync enumeration and brute forcing, Syslog SQL injection for PostgreSQL access, and password reuse for root escalation.

## Key facts extracted
- IPv6-only RSync service accessible after FTP bounce attack
- 13-byte rsyncd.secrets file indicates 8-character password
- Syslog configuration vulnerable to SQL injection via logger
- PostgreSQL COPY FROM PROGRAM allows command execution
- Git history shows config changes but hides current password
- Password reuse pattern between postgres and root accounts

## Filed into
[[zetta]], [[ftp-bounce]], [[rsync-enumeration]], [[password-brute-force]], [[sql-injection]], [[postgresql-copy-from-program]], [[postgresql-privilege-escalation]]