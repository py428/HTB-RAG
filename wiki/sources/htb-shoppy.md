---
type: source
title: "HTB Shoppy writeup"
raw: raw/htb-shoppy.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[shoppy]]
---
# Source: HTB Shoppy writeup
> Detailed walkthrough of exploiting NoSQL injection in a NodeJS-based e-commerce site, accessing Mattermost for credentials, and pivoting through Docker privileges.
## Key facts extracted
- NoSQL injection payload: `admin' || 'a'=='a` bypasses authentication
- MD5 hash cracking via crackstation reveals josh password
- Mattermost contains SSH credentials for jaeger user
- Static password "Sample" hardcoded in password-manager binary
- Deploy user has docker group privileges for container escape
## Filed into
[[shoppy]], [[nosql-injection]], [[hash-cracking]], [[docker-privilege-escalation]], [[reverse-engineering]]
