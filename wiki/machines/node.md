---
type: machine
title: Node
platform: htb
os: linux
difficulty: medium
tags: [web, linux, nodejs, information-disclosure, hash-cracking, command-injection, buffer-overflow, privesc, return-to-libc]
solved: 2026-07-09
sources: [[htb-node]]
related: []
---

# Node
> Node is a NodeJS application with an API endpoint exposing password hashes, a backup binary with buffer overflow vulnerability requiring return-to-libc exploitation, and MongoDB task scheduler for command execution.

## Attack path
1. [[information-disclosure]] — `/api/users/` endpoint exposes password hashes
2. [[hash-cracking]] — CrackStation to recover admin password
3. Download backup zip and crack with [[zip-cracking]]
4. Get MongoDB credentials from source for SSH as mark
5. [[command-injection]] — Insert tasks into MongoDB for execution as tom
6. [[buffer-overflow]] — Exploit SUID backup binary with [[return-to-libc]] and [[aslr-brute-force]]

## Techniques used
- [[information-disclosure]] — API endpoint leaks user password hashes
- [[hash-cracking]] — Online cracking with CrackStation
- [[zip-cracking]] — John with zip2john for protected archive
- [[command-injection]] — MongoDB task scheduler executes commands as tom
- [[buffer-overflow]] — 512-byte offset to overwrite EIP in backup binary
- [[return-to-libc]] — Call system('/bin/sh') via libc addresses
- [[aslr-brute-force]] — Brute force limited 9-bit ASLR randomization

## Tools used
- [[nmap]]
- feroxbuster
- curl
- [[jq]]
- CrackStation
- [[john]]
- zip2john
- unzip
- python
- gdb
- msf-pattern_create
- msf-pattern_offset
- ltrace

## Services / ports
- SSH (22) — OpenSSH 7.2
- HTTP (3000) — NodeJS Express
- MongoDB (27017) — localhost only

## Lessons / notes
- NodeJS applications often expose API endpoints with sensitive data
- Express responses can leak database connection strings
- MongoDB without authentication allows task insertion for RCE
- 32-bit binaries require return-to-libc on NX-enabled systems
- ASLR on 32-bit can have limited randomness (9 bits here)
- Buffer overflow offsets found with pattern_create/pattern_offset
- Return-to-libc requires libc base address, system/exit offsets, and /bin/sh string
- Return-to-libc stack layout: system_addr, exit_addr, bin/sh_addr
