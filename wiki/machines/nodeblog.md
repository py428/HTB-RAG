---
type: machine
title: NodeBlog
platform: htb
os: linux
difficulty: easy
tags: [web, linux, nosql, xxe, deserialization, privesc, password-reuse]
solved: 2026-07-09
sources: [[htb-nodeblog]]
related: []
---

# NodeBlog
> NodeBlog is a NodeJS blog application with NoSQL authentication, XXE file upload vulnerability, and insecure deserialization leading to RCE, with password reuse for root.

## Attack path
1. [[nosql-injection]] to bypass authentication on login form
2. [[xxe]] in file upload to leak server source code
3. [[deserialization]] via node-serialize cookie to get RCE
4. [[password-reuse]] — admin password from MongoDB works for sudo

## Techniques used
- [[nosql-injection]] — Authentication bypass using `$ne` operator in JSON login
- [[xxe]] — File read via XML external entity in post upload
- [[deserialization]] — RCE via node-serialize cookie with `_$$ND_FUNC$$_` payload
- [[password-reuse]] — MongoDB credentials reused for Linux privilege escalation

## Tools used
- [[nmap]]
- feroxbuster
- Burp Suite
- mongo
- bsondump
- [[netcat]]
- python

## Services / ports
- SSH (22)
- HTTP (5000) — NodeJS Express
- MongoDB (27017) — localhost only

## Lessons / notes
- NoSQL injection requires JSON content-type instead of form data
- XXE payloads need to match the expected XML structure
- Deserialization payloads need URL encoding to avoid breaking HTTP
- node-serialize uses `_$$ND_FUNC$$_function(){...}()` syntax for RCE
- MongoDB without authentication exposes plaintext passwords
- Directory permission issues (644 instead of 755) can prevent access to home directories
