---
type: source
title: "HTB Smasher writeup"
raw: raw/htb-smasher.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[smasher]]
---
# Source: HTB Smasher writeup
> Comprehensive writeup for Smasher, an Insane-difficulty HTB machine requiring advanced exploitation techniques including path traversal, buffer overflow with ROP chains, padding oracle cryptography attacks, and race condition exploitation. Focuses on shenfeng tiny-web-server exploitation and AES padding oracle vulnerability.

## Key facts extracted
- **Initial foothold**: Path traversal in shenfeng tiny-web-server (GitHub issue #2) provides access to source code and binary outside webroot
- **Buffer overflow**: 568-byte offset in tiny web server exploited using ROP chain with pop rdi; ret (0x4011dd) and pop rsi; pop r15; ret (0x4011db) gadgets
- **Padding oracle**: PKCS7 padding oracle in crackme.py (AES-CBC with hardcoded key "Th1sCh4llang31SInsane!!!") decrypts password "PaddingOracleMaster123"
- **Race condition**: TOCTOU vulnerability in /usr/bin/checker (setuid root) with 1-second sleep between access() and read() allows symlink swap attack
- **Cryptography**: AES-256-CBC encryption with IV reuse; padding oracle decrypts without knowing key
- **Privilege escalation**: Additional buffer overflow (552 bytes) in checker binary for full root shell (not completed)

## Filed into
[[smasher]], [[path-traversal]], [[buffer-overflow]], [[padding-oracle]], [[race-condition]], [[timing-attack]], [[http]]