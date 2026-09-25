---
type: source
title: "HTB Slonik writeup"
raw: raw/htb-slonik.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[slonik]]
---
# Source: HTB Slonik writeup
> Medium Linux box exploitation guide covering NFS filesystem escape techniques, SSH UNIX socket forwarding for PostgreSQL access, SQL command execution, setuid binary abuse via cron jobs, and Netexec NFS tool bug discovery and fix.

## Key facts extracted
- Two NFS shares exported: /home and /var/backups with no_subtree_check allowing filesystem escape
- service user (UID 1337) with /bin/false shell and password matching MD5 hash in .psql_history
- PostgreSQL listening on UNIX socket at /var/run/postgresql/.s.PGSQL.5432
- Cron job runs /usr/bin/backup script executing pg_basebackup every minute as root
- User flag location /var/lib/postgresql/user.txt (non-standard per creator notes)

## Filed into
[[slonik]], [[nfs-escape]], [[ssh-unix-socket-forward]], [[postgresql-copy-command]], [[setuid-privilege-escalation]]