---
type: source
title: "HTB Luanne writeup"
raw: raw/htb-luanne.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[luanne]]
---

# Source: HTB Luanne writeup
> First NetBSD box writeup covering Supervisord enumeration, Lua command injection analysis, SSH key recovery from public_html, and doas abuse with PGP-decrypted backup.

## Key facts extracted
- Supervisord on TCP 9001 with default user/123 credentials
- Process list reveals httpd running weather.lua on localhost:3000
- Weather API vulnerable to Lua injection via city parameter using os.execute()
- SSH key in r.michaels/public_html accessible with webapi_user/iamthebest
- Encrypted backup devel_backup-2020-09-16.tar.gz.enc decrypts with netpgp
- Backup contains .htpasswd with littlebear password for doas as root
- Lua vulnerability in string.format + load() equivalent to eval() injection

## Filed into
[[luanne]], [[default-credentials]], [[supervisord]], [[lua-injection]], [[command-injection]], [[ssh-key-reuse]], [[http-auth]], [[doas-abuse]], [[backup-decryption]], [[password-reuse]]
