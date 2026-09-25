---
type: machine
title: Developer
platform: htb
os: linux
difficulty: hard
tags: [linux, web, privesc, python, django, postgresql, reverse-tabnabbing, ssti]
solved: 2026-07-09
sources: [[htb-developer]]
related: []
---
# Developer
> A CTF-style platform with eight challenges and writeup submission functionality. The box combines reverse tabnabbing to harvest admin credentials, Django deserialization for initial foothold, PostgreSQL database access for user escalation, and binary reverse engineering for root access via a custom authenticator binary.

## Attack path
1. [[reverse-tabnabbing]] — Exploit writeup link vulnerability to capture Django admin credentials
2. [[django-deserialization]] — Use leaked secret from Sentry debug page to craft pickle RCE payload
3. [[postgresql]] — Extract Django hashes from Sentry database and crack to get user password
4. [[binary-reverse-engineering]] — Reverse custom Rust authenticator binary to extract hardcoded password
5. [[ssh-key]] — Add SSH key via authenticator for root access

## Techniques used
- [[reverse-tabnabbing]] — Admin clicks malicious writeup link, JavaScript redirects parent window to fake login page capturing credentials
- [[django-deserialization]] — Craft malicious pickle payload using Django SECRET_KEY from debug crash page
- [[postgresql]] — Query Sentry database to extract user password hashes
- [[hash-cracking]] — Crack Django PBKDF2-SHA256 hashes using hashcat
- [[binary-reverse-engineering]] — Extract AES key and IV from Rust binary to decrypt hardcoded password

## Tools used
[[nmap]], [[feroxbuster]], [[curl]], [[hashcat]], [[psql]], [[gdb]], [[ghidra]], [[dnspy]], [[ssh]], [[netcat]], [[python]], [[cyberchef]], [[john]]

## Services / ports
- [[ssh]] (22) — OpenSSH 8.2p1 Ubuntu
- [[http]] (80) — Apache 2.4.41
- PostgreSQL — localhost only
- Sentry — developer-sentry.developer.htb

## Lessons / notes
- Reverse tabnabbing exploits missing `rel="noopener nofollow"` attributes on target="_blank" links
- Django debug pages can leak critical secrets like SECRET_KEY in crash dumps
- Django pickle deserialization with known SECRET_KEY provides reliable RCE
- Rust binaries add extensive safety checks that complicate reverse engineering
- AES-CTR mode with static key/IV allows decryption of hardcoded secrets
- Git history may contain committed credentials that were later removed
