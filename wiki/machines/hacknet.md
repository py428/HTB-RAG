---
type: machine
title: HackNet
platform: htb
os: linux
difficulty: medium
tags: [linux, web, ssti, deserialization, privesc]
solved: 2026-07-09
sources: [[htb-hacknet]]
related: []
---
# HackNet
> Django social media site with server-side template injection in username rendering leading to user data disclosure, Python pickle deserialization via world-writable Django cache directory, and GPG-encrypted database backup password cracking for root access.

## Attack path
1. [[ssti]] via username HTML injection in likes page rendering
2. [[python]] script to enumerate Django QuerySet and dump user credentials
3. [[ssh]] access using credentials from leaked email/username pattern
4. [[pickle]] deserialization by poisoning Django FileBasedCache
5. [[gpg]] private key password cracking with [[hashcat]]
6. Database backup decryption revealing shared root password

## Techniques used
- [[ssti]] — Django template injection in username field when rendered in likes page, using `{{ users.values }}` to dump user objects with plaintext passwords
- [[pickle]] — Python pickle deserialization RCE by replacing Django cache files with malicious payload in world-writable `/var/tmp/django_cache`
- [[password-reuse]] — Database credentials reused for user shell access
- [[gpg]] — Cracking GPG private key password protecting encrypted database backups containing password messages

## Tools used
- [[nmap]]
- feroxbuster
- [[curl]]
- [[ffuf]]
- python
- [[openssl]]
- [[gpg2john]]
- [[hashcat]]
- [[netcat]]
- ssh

## Services / ports
- [[ssh]] (22)
- [[http]] (80)

## Lessons / notes
- Django SSTI via `engine.from_string()` with user-controlled input in template construction
- Django FileBasedCache uses pickle serialization — world-writable cache directory enables cache poisoning
- GPG private keys can be cracked with gpg2john + hashcat when protected by weak passwords
- Database backups may contain sensitive password exchanges in user messages
