---
type: machine
title: Ransom
platform: htb
os: linux
difficulty: medium
tags: [web, linux, php, laravel, crypto]
solved: 2026-07-09
sources: [[htb-ransom]]
related: []
---
# Ransom
> Laravel-based file transfer service exploiting type juggling vulnerability for authentication bypass, known plaintext attack on ZipCrypto encrypted archives, and hardcoded credential discovery for privilege escalation.

## Attack path
1. Exploit [[type-juggling]] vulnerability in Laravel login by sending boolean true instead of string password
2. Access protected file download area and retrieve encrypted ZipCrypto archive with SSH keys
3. Perform known plaintext attack using bkcrack with standard .bash_logout file to decrypt archive
4. SSH authentication using extracted private key as htb user
5. Discover hardcoded password in Laravel application source code
6. Use same credentials for root access via su

## Techniques used
- [[type-juggling]] — PHP loose comparison vulnerability using boolean true to bypass string comparison
- [[zip-crypto-known-plaintext]] — Decrypt ZipCrypto archive using known plaintext attack with bkcrack
- [[hardcoded-credentials]] — Extract password from Laravel AuthController source code

## Tools used
- [[nmap]] — Port scanning identifying Apache and OpenSSH services
- [[feroxbuster]] — Web directory enumeration
- [[bkcrack]] — ZipCrypto known plaintext attack tool
- [[john]] — Password hash cracking (attempted)
- [[ssh]] — Remote access using extracted private keys

## Services / ports
- SSH (22) — OpenSSH 8.2p1 Ubuntu
- HTTP (80) — Apache 2.4.41 with Laravel application

## Lessons / notes
- PHP type juggling allows boolean true to match any string in loose comparison (==)
- ZipCrypto encryption vulnerable to known plaintext attack using 12+ bytes of known file content
- Laravel framework stores configuration in composer.json and routes/api.php files
- Standard Ubuntu files like .bash_logout serve as effective known plaintext for zip attacks
- Laravel artisan command-line interface provides route listing and application debugging capabilities