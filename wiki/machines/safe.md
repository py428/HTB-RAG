---
type: machine
title: Safe
platform: htb
os: linux
difficulty: easy
tags: [linux, buffer-overflow, rop, ret2libc, web, privesc]
solved: 2026-07-09
sources: [[htb-safe]]
related: []
---
# Safe

> Linux box featuring a buffer overflow in a custom echo service on port 1337, exploited via ROP to get a user shell, then a KeePass database with a cracked password for root access.

## Attack path

1. [[buffer-overflow]] — Exploit `gets()` vulnerability in custom service on TCP 1337
2. [[rop]] — Use Return Oriented Programming with `system()` and `/bin/sh` to get shell
3. [[keepass-cracking]] — Crack KeePass database with john using images as keyfiles
4. [[password-reuse]] — Use cracked root password to `su` to root

## Techniques used

- [[buffer-overflow]] — 120-byte offset in `gets()` call in custom echo service
- [[rop]] — Three methods: ret2libc with leaked puts address, write `/bin/sh` to .data, abuse `test()` function
- [[keepass-cracking]] — john with keepass2john using images as potential keyfiles

## Tools used

- [[nmap]] — Port scanning
- gobuster — Directory brute force
- [[gdb]] — Debugging and exploit development with PEDA
- ropper — ROP gadget finder
- pwntools — Python exploit framework
- [[john]] — Password cracking for KeePass database
- kpcli — KeePass database interaction
- [[curl]] — Web interaction

## Services / ports

- [[ssh]] — 22/tcp
- [[http]] — 80/tcp — Apache with default page and `/myapp` ELF download
- Custom echo service — 1337/tcp — Vulnerable buffer overflow service

## Lessons / notes

- Three different ROP strategies demonstrated: two-stage with address leak, writing `/bin/sh` to .data section, and abusing unused `test()` function
- Offset found at 120 bytes using pattern_create and pattern_offset in gdb
- NX enabled but no PIE, ASLR assumed present
- KeePass database cracked with john using rockyou wordlist, IMG_0547.JPG as keyfile
- No standard reverse shell tools available, used SSH key upload for stable shell
