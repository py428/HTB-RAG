---
type: machine
title: Slonik
platform: htb
os: linux
difficulty: medium
tags: [nfs, database, privesc, linux]
solved: 2026-07-09
sources: [[htb-slonik]]
related: []
---
# Slonik
> Medium-difficulty Linux box featuring insecure NFS configuration allowing filesystem escape, SSH UNIX socket port forwarding to access PostgreSQL, command execution via SQL COPY, and setuid binary abuse for privilege escalation.

## Attack path
1. [[nfs-escape]] to read /etc/shadow and find service user hash
2. [[ssh-unix-socket-forward]] to forward PostgreSQL socket from target to local machine
3. [[postgresql-copy-command]] to execute commands and inject SSH public key for postgres user
4. [[setuid-privilege-escalation]] by copying setuid bash into pg_basebackup directory

## Techniques used
- [[nfs-escape]] — Exploited no_subtree_check and root_squash options in /etc/exports to escape shares and read entire filesystem including /etc/shadow
- [[ssh-unix-socket-forward]] — Used SSH -L to forward /var/run/postgresql/.s.PGSQL.5432 UNIX socket to local port for PostgreSQL access
- [[postgresql-copy-command]] — Executed commands via COPY FROM PROGRAM and wrote files via COPY TO PROGRAM in PostgreSQL
- [[setuid-privilege-escalation]] — Copied /bin/bash into /var/lib/postgresql/14/main/, set chmod 6777, executed with -p flag to preserve root privileges
- [[cron-job-abuse]] — Monitored cron execution with pspy, identified pg_basebackup running as root every minute

## Tools used
- [[nmap]] for port and service discovery  
- [[showmount]] for NFS share enumeration
- [[netexec]] with NFS module for advanced NFS enumeration and file operations
- [[john]] for cracking yescrypt hashes from /etc/shadow
- [[psql]] for PostgreSQL interaction
- [[pspy]] for process monitoring and cron job identification

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 8.9p1 Ubuntu 3ubuntu0.13
- 111/tcp — [[rpc]] — rpcbind 2-4
- 2049/tcp — [[nfs]] — NFS_ACL 3

## Lessons / notes
- NFS with no_subtree_check allows clients to escape share boundaries and access entire filesystem
- service account had /bin/false shell preventing SSH login but worked for PostgreSQL authentication
- PostgreSQL COPY FROM PROGRAM allows command execution as database user (postgres)
- pg_basebackup copies database files including setuid binaries when run by cron
- Netexec NFS enumeration revealed root escape capability and automated file listing across shares
- User flag located in non-standard /var/lib/postgresql directory per box creator specification