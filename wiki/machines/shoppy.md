---
type: machine
title: Shoppy
platform: htb
os: linux
difficulty: easy
tags: [linux, web, nosql, docker, privesc]
solved: 2026-07-09
sources: [[htb-shoppy]]
related: []
---
# Shoppy
> E-commerce website running a NodeJS backend vulnerable to NoSQL injection, leading to admin access and a Mattermost server with credentials. Final pivot through Docker group privileges.
## Attack path
1. [[nosql-injection]] on admin login page (`admin' || 'a'=='a`) → Admin dashboard access
2. [[nosql-injection]] on user search (`admin' || 'a'=='a`) → Dump all user hashes including josh
3. [[hash-cracking]] with crackstation → josh password → Mattermost login
4. [[password-reuse]] → Find jaeger SSH creds in Mattermost "Deploy Machine" channel → SSH as jaeger
5. [[reverse-engineering]] password-manager binary (strings/ghidra) → Static password "Sample" → su deploy
6. [[docker-privilege-escalation]] → Mount host root filesystem in container → root flag
## Techniques used
- [[nosql-injection]] — Bypass login and extract user data via MongoDB-style injection in NodeJS application
- [[hash-cracking]] — MD5 hash of josh user cracked via online rainbow tables
- [[docker-privilege-escalation]] — Deploy user in docker group mounts host / as /mnt in container for full filesystem access
## Tools used
[[nmap]], [[feroxbuster]], [[wfuzz]], hashcat/crackstation, [[ssh]], [[docker]]
## Services / ports
- [[http]] (80) - nginx/1.23.1, redirects to shoppy.htb
- [[http]] (9093) - Prometheus metrics (copycat)
- [[ssh]] (22) - OpenSSH 8.4
## Lessons / notes
- NoSQL injection in NodeJS often uses syntax like `admin' || 'a'=='a` to bypass authentication
- Always check for subdomains when main domain shows limited functionality (mattermost.shoppy.htb)
- Docker group membership is equivalent to root access - can mount host filesystem in container
- Silver tickets with forged group memberships can enable OPENROWSET BULK operations in MSSQL
- Reverse engineering basics (strings, Ghidra) often faster than full binary analysis for simple C++ programs
