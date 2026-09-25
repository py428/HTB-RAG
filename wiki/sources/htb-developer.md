---
type: source
title: "HTB Developer writeup"
raw: raw/htb-developer.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[developer]]
---
# Source: HTB Developer writeup
> Comprehensive walkthrough of Developer HackTheBox machine covering web exploitation (reverse tabnabbing, Django SSTI/deserialization), database credential extraction, and binary reverse engineering of a Rust authenticator for privilege escalation.

## Key facts extracted
- Reverse tabnabbing vulnerability in writeup submission system allows credential phishing
- Django SECRET_KEY leaked in Sentry debug crash page enables pickle deserialization RCE
- PostgreSQL credentials found in Django settings: ctf_admin/CTFOG2021
- Sentry database contains Django password hashes for karl@developer.htb user
- Custom Rust authenticator binary uses AES-CTR with hardcoded key/IV for password validation
- SSH key injection via authenticator provides root access

## Filed into
[[developer]], [[reverse-tabnabbing]], [[django-deserialization]], [[postgresql]], [[binary-reverse-engineering]], [[aes-encryption]]
