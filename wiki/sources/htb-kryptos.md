---
type: source
title: "HTB Kryptos writeup"
raw: raw/htb-kryptos.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[kryptos]]
---
# Source: HTB Kryptos writeup
> Detailed walkthrough of exploiting Kryptos, an insane-difficulty HTB box with heavy emphasis on cryptography. The writeup covers MySQL DSN injection for auth bypass, RC4 known plaintext attacks, SQLite webshell injection, VimCrypt cracking, and ECDSA weak RNG exploitation for privilege escalation.

## Key facts extracted
- **Auth bypass**: MySQL PDO DSN injection allows specifying database host and port in login form
- **RC4 encryption**: Static RC4 keystream enables decryption of any page using known plaintext
- **SQLite injection**: ATTACH DATABASE with stacked queries writes PHP webshell to world-writable directory
- **VimCrypt backup**: Weak IV reuse allows cracking with partial known plaintext
- **ECDSA RNG**: Custom secure_rng() function only produces 209 unique outputs from 128-bit seed
- **Root shell**: Recover ECDSA signing key, sign malicious expression, bypass Python restrictions

## Filed into
[[kryptos]], [[mysql-dsn-injection]], [[rc4-known-plaintext]], [[sqlite-attack]], [[vim-crypt-cracking]], [[weak-rng-ecdsa]], [[python-eval-bypass]]