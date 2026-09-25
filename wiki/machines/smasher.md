---
type: machine
title: Smasher
platform: htb
os: linux
difficulty: insane
tags: [linux, web, buffer-overflow, crypto, race-condition, privesc]
solved: 2026-07-09
sources: [[htb-smasher]]
related: []
---
# Smasher
> Insane-difficulty Linux box testing advanced exploitation skills including path traversal, buffer overflow, cryptography, and race conditions. Starting with shenfeng tiny-web-server on TCP 1111, chain through a buffer overflow for initial shell, padding oracle attack to decrypt AES-encrypted password, and exploit a race condition in a setuid binary to read root.txt.

## Attack path
1. [[path-traversal]] in tiny-web-server to leak source code and binary
2. [[buffer-overflow]] ROP chain in tiny web server to get shell as www
3. [[padding-oracle]] attack on AES-encrypted challenge to decrypt smasher's password
4. [[race-condition]] / [[timing-attack]] in setuid checker binary to read root.txt (potential root shell via additional buffer overflow)

## Techniques used
- [[path-traversal]] — shenfeng tiny-web-server vulnerability allows reading files outside webroot via `../../../../../` paths
- [[buffer-overflow]] — Exploit 568-byte overflow in tiny web server using ROP chain (pop rdi; ret, pop rsi; pop r15; ret) to execute shellcode
- [[padding-oracle]] — PKCS7 padding oracle vulnerability in AES-encrypted crackme.py challenge allows plaintext decryption without key
- [[race-condition]] — 1-second sleep between access() check and file read in checker binary enables symlink swap attack
- [[timing-attack]] — TOCTOU race in setuid binary allows reading files as root by swapping authorized file with target during sleep window

## Tools used
[[nmap]], [[curl]], gobuster, nc, [[python]], pwntools, paddingoracle (python-paddingoracle), openssl, [[gdb]], objdump, hexcurse, [[ssh]], ltrace, file, strings, xxd

## Services / ports
- [[ssh]] TCP 22 — OpenSSH 7.2p2 Ubuntu 4ubuntu2.4
- [[http]] TCP 1111 — shenfeng tiny-web-server with path traversal vulnerability

## Lessons / notes
- Buffer overflow chain: BSS address + read PLT + socket descriptor 4 + dup2 shellcode for reverse shell
- Padding oracle: Different error messages ("Invalid Padding!" vs "Generic error, ignore me!") indicate oracle exists
- Race condition: Script removes/recreates file, runs checker in background, swaps to symlink during 1-second sleep
- IPv6 not initially visible in nmap scan, required alternative enumeration methods (SNMP, ARP cache, neighbor discovery)
- ASLR disabled on binary level (no PIE, NX disabled), but host-level ASLR enabled for most exploitation
- No-canary binary exploitation with 362-byte offset to EIP control
- SUID checker binary vulnerable to additional buffer overflow (552 bytes) for full root shell (not completed in writeup)