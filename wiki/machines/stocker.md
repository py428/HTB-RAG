---
type: machine
title: Stocker
platform: htb
os: linux
difficulty: easy
tags: [nosql, xss, pdf, sudo, easy, linux, web, privesc]
solved: 2026-07-09
sources: [[htb-stocker]]
related: []
---
# Stocker
> Easy Linux box featuring NoSQL injection and server-side XSS. Initial foothold through NoSQL authentication bypass on dev site, then exploiting server-side XSS in PDF generation for file read. Privilege escalation via sudo rule allowing arbitrary Node.js script execution.
## Attack path
1. [[nosql-injection]] — bypass login using MongoDB NoSQL injection
2. [[server-side-xss]] — exploit PDF generation with XSS payloads
3. [[file-read-xss]] — read files via server-side XSS in PDF
4. [[sudo-misconfiguration]] — execute arbitrary JavaScript via sudo

## Techniques used
- [[nosql-injection]] — MongoDB operator injection for auth bypass
- [[server-side-xss]] — XSS in PDF generation via Chromium
- [[file-read-xss]] — server-side file reading via XMLHttpRequest
- [[sudo-misconfiguration]] — wildcard in sudo rule for script execution

## Tools used
- [[nmap]] — port scanning
- ffuf — subdomain fuzzing
- feroxbuster — directory brute force
- [[curl]] — HTTP requests and file transfer
- [[nc]] — reverse shell listener

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 8.2p1 Ubuntu
- 80/tcp — [[http]] — nginx 1.18.0

## Lessons / notes
- NoSQL injection uses MongoDB operators like `$ne` for authentication bypass
- Server-side XSS in PDF generation can read local files
- Chromium PDF generation interprets HTML/JS in input
- Sudo rules with wildcards can be abused for arbitrary execution
- Express applications often use NoSQL databases like MongoDB
- Subdomain enumeration reveals additional attack surfaces
