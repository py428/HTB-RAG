---
type: source
title: "HTB DevOops writeup"
raw: raw/htb-devoops.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[devoops]]
---
# Source: HTB DevOops writeup
> Detailed exploitation of XXE vulnerability in blog feed application to leak SSH keys, followed by git history analysis to recover committed root credentials.

## Key facts extracted
- Blog feed upload endpoint accepts XML without proper entity sanitization
- File read XXE via <!ENTITY bar SYSTEM "file:///path"> extracts arbitrary files
- User roosa has SSH key at /home/roosa/.ssh/id_rsa readable via XXE
- Git repository at /home/roosa/work/blogfeed/.git contains commit history
- Commit "reverted accidental commit with proper key" removed root SSH key from resources/integration/authcredentials.key
- Checkout previous commit (d387abf) recovers root private key

## Filed into
[[devoops]], [[xxe]], [[ssh]], [[git-history]], [[pickle-deserialization]]
