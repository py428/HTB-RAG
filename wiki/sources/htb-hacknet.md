---
type: source
title: "HTB HackNet writeup"
raw: raw/htb-hacknet.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[hacknet]]
---
# Source: HTB HackNet writeup
> Django social media application exploitation through server-side template injection in username rendering, Python pickle deserialization via cache poisoning, and GPG backup decryption for privilege escalation.

## Key facts extracted
- Django SSTI in likes page rendering when username contains template syntax
- Django QuerySet accessible via `{{ users.values }}` to dump user objects with plaintext passwords
- World-writable Django cache directory `/var/tmp/django_cache` allows pickle cache poisoning
- GPG-encrypted database backups contain password exchange messages
- GPG private key password crackable via gpg2john + hashcat

## Filed into
[[hacknet]], [[ssti]], [[pickle]], [[gpg]], [[password-reuse]]
