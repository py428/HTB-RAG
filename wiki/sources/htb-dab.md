---
type: source
title: "HTB Dab writeup"
raw: raw/htb-dab.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[dab]]
---
# Source: HTB Dab writeup

> Comprehensive walkthrough of Dab, a hard-difficulty HTB box featuring web applications with memcached integration, demonstrating credential brute-forcing, cache enumeration, and library hijacking for privilege escalation via ldconfig abuse.

## Key facts extracted

- Two web applications on ports 80 and 8080 sharing memcached backend
- Admin login on port 80 populates memcached with user credentials
- Port 8080 provides TCP proxy access to memcached with password authentication
- SUID binary `myexec` requires password and loads `libseclogin.so` library
- SUID `ldconfig` binary can modify library search paths

## Filed into

[[dab]], [[memcached-enumeration]], [[library-hijacking]], [[ldconfig-abuse]], [[brute-force]], [[steganography]]