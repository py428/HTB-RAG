---
type: source
title: "HTB Overflow writeup"
raw: raw/htb-overflow.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[overflow]]
---

# Source: HTB Overflow writeup
> Detailed writeup for HackTheBox Overflow machine covering padding oracle attack on encrypted cookies, SQL injection exploitation, Exiftool CVE-2021-22204 exploitation for initial shell access, and buffer overflow with TOCTOU vulnerability for root privilege escalation.

## Key facts extracted
- Linux web application server (Ubuntu 18.04) running Apache with PHP applications
- Padding oracle vulnerability in auth cookie implementation allowing decryption and forgery
- SQL injection in logs.php parameter enabling database credential extraction
- CVE-2021-22204 in Exiftool 11.92 exploited via malicious DjVu file in uploaded image
- Buffer overflow in setuid file_encrypt binary with TOCTOU race condition for arbitrary file read
- Time-of-check/time-of-use vulnerability allows bypassing root file ownership checks
- Multiple services including SSH, HTTP, and SMTP with various exploitation opportunities
- Complex attack chain requiring web exploitation, database access, and binary exploitation

## Filed into
[[overflow]], [[padding-oracle]], [[sqli]], [[cve-2021-22204]], [[buffer-overflow]], [[toctou]]
