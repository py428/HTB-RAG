---
type: source
title: "HTB Frolic writeup"
raw: raw/htb-frolic.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[frolic]]
---
# Source: HTB Frolic writeup
> Complete writeup for Frolic HTB machine covering web puzzles, PlaySMS exploitation, and ret2libc buffer overflow for privilege escalation.

## Key facts extracted
- Ubuntu system with Samba, Node-RED, and nginx
- Multi-stage puzzle: admin login → Ook! → brainfuck → zip → PlaySMS password
- PlaySMS credentials: admin:idkwhatispass
- CSV upload vulnerability in PlaySMS for RCE
- SUID binary: /home/ayush/.binary/rop (7480 bytes)
- ASLR disabled, NX enabled, PIE disabled, RELRO partial
- libc base: 0xb7e19000

## Filed into
[[frolic]], [[brainfuck-decoding]], [[zip-password-cracking]], [[playsms-exploit]], [[buffer-overflow]], [[ret2libc]]
