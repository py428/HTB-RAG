---
type: source
title: "HTB NodeBlog writeup"
raw: raw/htb-nodeblog.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[nodeblog]]
---

# Source: HTB NodeBlog writeup
> Comprehensive writeup covering NodeJS NoSQL injection, XXE file reading, insecure deserialization with node-serialize, and password reuse for privilege escalation.

## Key facts extracted
- NodeBlog runs on NodeJS Express with MongoDB backend
- Login vulnerable to NoSQL injection using `$ne` operator in JSON
- File upload accepts XML and processes it with XXE vulnerability
- Session cookies use node-serialize library with unsafe deserialization
- MongoDB runs without authentication exposing user credentials
- Admin password reused between MongoDB and Linux system
- Source code location disclosed via error stack trace

## Filed into
[[nodeblog]], [[nosql-injection]], [[xxe]], [[deserialization]], [[password-reuse]]
