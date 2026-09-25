---
type: machine
title: Jail
platform: htb
os: linux
difficulty: insane
tags: [linux, bof, nfs, vim, crypto, privesc]
solved: 2026-07-09
sources: [[htb-jail]]
related: []
---
# Jail
> Insane difficulty Linux machine featuring a beginner-friendly buffer overflow, NFS share abuse, vim escape, and cryptographic challenges. Long multi-stage path from nobody to root requiring diverse exploitation techniques.

## Attack path
1. [[buffer-overflow]] in custom jail service (TCP 7411) with execstack enabled
2. [[nfs-abuse]] via setuid binary creation to escalate to frank
3. [[rvim-escape]] via Python to escalate to adm
4. RAR archive cracking with Atbash cipher + hashcat rules
5. [[rsa-key-recovery]] via Wiener's attack to get root SSH key

## Techniques used
- [[buffer-overflow]] — 32-bit jail service with execstack, DEBUG mode leaks buffer address at 0xffffd610, 28-byte offset to return address
- [[nfs-abuse]] — Share /var/nfsshare with no_all_squash allows uploading setuid binaries as frank
- [[rvim-escape]] — Restricted vim (rvim) escape via Python: `:py import os; os.execl("/bin/sh", "sh", "-c", "reset; exec sh")`
- atbash-cipher — Decoded hint: "Hahaha! Nobody will guess my new password! Only a few lucky souls have Escaped from Alcatraz alive like I did!!!"
- [[rsa-key-recovery]] — RsaCtfTool recovered private key from public key using Wiener's attack

## Tools used
[[nmap]], gdb, PEDA/pwntools, [[hashcat]], unrar, RsaCtfTool

## Services / ports
[[ssh]] (22), [[http]] (80), [[nfs]] (2049), rpc (111), jail-custom (7411)

## Lessons / notes
- When AS-REP roasting 2600+ users, expect long run times but high success probability
- DEBUG mode in jail service leaks static buffer address - always check for info leaks
- NFS with no_all_squash preserves user permissions across mount for privilege escalation
- Frank Morris escaped Alcatraz in 1962 - password: Morris1962!
- rvim escapes possible via Python/Lua despite shell command restrictions
- RSA keys with small d can be recovered using Wiener's attack
