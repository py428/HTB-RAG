---
type: source
title: "HTB Moderators writeup"
raw: raw/htb-moderators.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[moderators]]
---
# Source: HTB Moderators writeup

> Complete exploitation walkthrough for Moderators, a Hard-level Linux box demonstrating multi-stage web exploitation including IDOR vulnerabilities, file upload bypasses, WordPress plugin vulnerabilities, and VirtualBox/LUKS encryption cracking.

## Key facts extracted
- IDOR vulnerability in /report endpoint allowing enumeration of MD5-hashed report IDs
- File upload accepts .php.pdf extension with magic bytes bypass
- WordPress instance running on localhost:8000 with Brandfolder plugin LFI vulnerability
- WordPress database credentials: wpuser:q!L@us6ru96^!e%h (from wp-config.php)
- VirtualBox VDI encryption using AES-256-XTS with 100000 PBKDF2 iterations
- LUKS passphrase reused between VirtualBox disk and sudo access
- Beyond root: local file inclusion to RCE via expect wrapper

## Filed into
[[moderators]], [[idor]], [[file-upload-bypass]], [[disable-functions-bypass]], [[wordpress-lfi]], [[encryption-decryption]], [[virtualbox-encryption-cracking]], [[luks-cracking]], [[password-reuse]]
