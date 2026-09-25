---
type: source
title: "HTB Safe writeup"
raw: raw/htb-safe.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[safe]]
---
# Source: HTB Safe writeup

> Detailed writeup covering buffer overflow exploitation with multiple ROP strategies and KeePass password database cracking for privilege escalation.

## Key facts extracted

- Custom echo service on TCP 1337 with `gets()` buffer overflow vulnerability
- 120-byte offset to return address, no PIE but NX enabled
- Three ROP methods demonstrated: libc leak with ret2libc, write `/bin/sh` to .data, and abuse `test()` function
- KeePass database cracked with john using rockyou, IMG_0547.JPG as keyfile
- Root password: `u3v2249dl9ptv465cogl3cnpo3fyhk`

## Filed into

[[safe]], [[buffer-overflow]], [[rop]], [[keepass-cracking]], [[password-reuse]]
