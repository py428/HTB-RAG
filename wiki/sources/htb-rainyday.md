---
type: source
title: "HTB RainyDay writeup"
raw: raw/htb-rainyday.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[rainyday]]
---
# Source: HTB RainyDay writeup
> Advanced multi-stage exploitation guide covering IDOR vulnerability for hash leakage, Docker container breakout via process inspection, Python sandbox escape using use-after-free vulnerability, and cryptographic secret recovery through Unicode truncation technique.

## Key facts extracted
- Flask API vulnerable to IDOR via decimal suffix (user/1.0 vs user/1) to leak bcrypt hashes
- Background container processes run as UID 1000 regardless of session user, enabling jailbreak via /proc inspection
- Python memoryview use-after-free vulnerability allows bypassing import restrictions in safe_python
- bcrypt 72-byte limit can be exploited using Unicode multi-byte characters for secret recovery
- Dev subdomain (dev.rainycloud.htb) only accessible from internal networks via proxy
- Regex-based healthcheck API can be exploited for arbitrary file reads using custom patterns

## Filed into
[[rainyday]], [[idor]], [[container-breakout]], [[python-exec-bypass]], [[unicode-truncation]], [[file-read]], [[docker]], [[python]], [[flask]]