---
type: source
title: "HTB Proper writeup"
raw: raw/htb-proper.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[proper]]
---
# Source: HTB Proper writeup
> In-depth analysis of Proper, a Hard Windows box featuring parameter hashing, ORDER BY SQL injection, SMB-based TOCTOU RFI, arbitrary file write via cleanup service, and multiple SYSTEM escalation paths.

## Key facts extracted
- IIS 10.0 with PHP 7.4.1 on Windows 10/Server 2016/2019
- SECURE_PARAM_SALT: hie0shah6ooNoim leaked from PHP error
- Hash format: MD5(salt + parameter)
- 29 user credentials in database, all crackable with rockyou.txt
- SMB password: charlotte123! for web user
- TOCTOU vulnerability in secure_include function
- Cleanup service (Go binary) cleans files >30 days old in Downloads
- Arbitrary write via base64 filename manipulation in C:\ProgramData\Cleanup
- Multiple SYSTEM privesc paths: WerTrigger, arbitrary read via named pipe, NetworkService impersonation, CVE-2021-1732

## Filed into
[[proper]], [[parameter-hashing]], [[sqli]], [[sqli-with-eval]], [[toctou]], [[smb-authentication]], [[rfi-over-smb]], [[arbitrary-write]], [[wertrigger]]
