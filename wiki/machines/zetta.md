---
type: machine
title: Zetta
platform: htb
os: linux
difficulty: hard
tags: [network, linux, privesc, ftp]
solved: 2026-07-09
sources: [[htb-zetta]]
related: []
---
# Zetta
> Zetta is a file sharing service running on IPv6-only accessible RSync. The attack path involves FTP bounce attacks to discover the IPv6 address, RSync enumeration and password brute-forcing, SQL injection via Syslog for PostgreSQL access, and password reuse for root escalation.

## Attack path
1. [[ftp-bounce]] to discover IPv6 address via EPRT command
2. [[rsync-enumeration]] via IPv6 to find accessible modules
3. [[password-brute-force]] 8-character rsync password for roy user
4. [[sql-injection]] via Syslog to PostgreSQL for [[postgresql-copy-from-program]]
5. [[postgresql-privilege-escalation]] via password reuse pattern (postgres@postgres → root@root)

## Techniques used
- [[ftp-bounce]] — EPRT command with IPv6 address reveals server's IPv6 address
- [[rsync-enumeration]] — RSync access to /etc module reveals configuration and password length
- [[password-brute-force]] — Brute forcing 8-character password derived from rsyncd.secrets file size
- [[sql-injection]] — Stacked queries in Syslog INSERT template for PostgreSQL
- [[postgresql-copy-from-program]] — COPY FROM PROGRAM for command execution as postgres
- [[postgresql-privilege-escalation]] — Password pattern reuse between postgres and root users

## Tools used
[[nmap]], [[ftp]], [[rsync]], [[ssh]], [[logger]], [[psql]], [[nc]], python, grep

## Services / ports
[[ssh]] (22), [[http]] (80), [[ftp]] (21), [[rsync]] (8730)

## Lessons / notes
- FTP FXP/EPRT allows bouncing connections to reveal IPv6 address
- RSync hosts allow/deny rules can permit IPv6 when IPv4 is blocked
- Syslog SQL template vulnerable to injection via logger command
- PostgreSQL COPY FROM PROGRAM executes commands as postgres user
- Password pattern reuse (@service → @root) common in admin configurations