---
type: source
title: "HTB Node writeup"
raw: raw/htb-node.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[node]]
---

# Source: HTB Node writeup
> Detailed guide covering API information disclosure, hash cracking, MongoDB command injection via task scheduler, and return-to-libc buffer overflow exploitation with ASLR brute forcing.

## Key facts extracted
- `/api/users/` endpoint exposes password hashes for all users including admin
- MongoDB connection string in app.py contains credentials
- Task scheduler executes commands from MongoDB tasks collection every 30 seconds
- SUID backup binary vulnerable to buffer overflow at 512-byte offset
- Binary lacks canaries and PIE but has NX enabled
- ASLR enabled but limited to 9-bit randomization on 32-bit
- Backup binary creates zip archives with system() calls
- Multiple unintended root methods including path wildcards and environment variables

## Filed into
[[node]], [[information-disclosure]], [[hash-cracking]], [[zip-cracking]], [[command-injection]], [[buffer-overflow]], [[return-to-libc]], [[aslr-brute-force]]
