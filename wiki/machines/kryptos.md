---
type: machine
title: Kryptos
platform: htb
os: linux
difficulty: insane
tags: [web, crypto, mysql, sqlite, php, ssh, privesc]
solved: 2026-07-09
sources: [[htb-kryptos]]
related: []
---
# Kryptos
> Kryptos is an insane-difficulty Linux box focusing on cryptography and exploitation. The attack path involves bypassing authentication via MySQL DSN injection, breaking RC4 encryption through known plaintext attacks, exploiting SQLite to write a webshell, cracking VimCrypt backups, and finally exploiting weak ECDSA RNG to achieve code execution as root.

## Attack path
1. [[mysql-dsn-injection]] — Bypass login by injecting MySQL host parameter
2. [[rc4-known-plaintext]] — Decrypt encrypted pages using keystream recovery
3. [[sqlite-attack]] — Write webshell via ATTACH DATABASE injection
4. [[vim-crypt-cracking]] — Crack VimCrypt backup file for SSH credentials
5. [[weak-rng-ecdsa]] — Exploit weak random number generator to sign arbitrary expressions
6. [[python-eval-bypass]] — Bypass restricted Python eval to get root shell

## Techniques used
- [[mysql-dsn-injection]] — Inject MySQL DSN host parameter to authenticate to controlled database
- [[rc4-known-plaintext]] — Recover RC4 keystream by XORing known plaintext with ciphertext
- [[sqlite-attack]] — Abuse SQLite ATTACH DATABASE and stacked queries to write PHP webshell
- [[vim-crypt-cracking]] — Exploit weak IV reuse in VimCrypt to decrypt password backup
- [[weak-rng-ecdsa]] — Brute-force limited ECDSA seed space to recover signing key
- [[python-eval-bypass]] — Bypass disabled builtins in eval using subclass attribute access

## Tools used
- [[nmap]]
- [[gobuster]]
- [[burp]]
- [[mysql]]
- [[hashcat]]
- netcat
- [[curl]]
- python3
- [[sshtunnel]]
- ecdsa

## Services / ports
- [[ssh]] (22)
- [[http]] (80)

## Lessons / notes
- MySQL PDO DSN injection allows redirecting authentication to attacker-controlled database
- RC4 with static key is vulnerable to known plaintext attacks—XOR known plaintext with ciphertext to recover keystream
- VimCrypt uses same IV for first 8 blocks, enabling partial decryption with known plaintext
- Custom PRNG with only 209 possible outputs makes ECDSA key recovery feasible
- Python eval restrictions can be bypassed by accessing builtins through object subclasses