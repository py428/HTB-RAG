---
type: source
title: "HTB Interpreter writeup"
raw: raw/htb-interpreter.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[interpreter]]
---
# Source: HTB Interpreter writeup
> Comprehensive writeup for HTB Interpreter covering Mirth Connect deserialization exploitation and Flask template injection for privilege escalation.

## Key facts extracted
- Mirth Connect 4.4.0 vulnerable to CVE-2023-43208 (incomplete CVE-2023-37679 patch)
- API runs on Jersey with XStream XML deserialization before auth check
- Database credentials: mirthdb/MirthPass123! for mc_bdd_prod database
- PBKDF2-HMAC-SHA256 with 600,000 iterations and 8-byte salt
- Flask notification server on localhost:54321 with eval() vulnerability

## Filed into
[[interpreter]], [[xstream-deserialization]], [[python-template-injection]]