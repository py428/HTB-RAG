---
type: machine
title: Caption
platform: htb
os: linux
difficulty: hard
tags: [http, ssh, web, proxy, cache-poisoning, xss, smuggling, rce, privesc, ad, docker, command-injection]
solved: 2026-07-09
sources: [[htb-caption]]
related: []
---
# Caption
> Caption is a hard Linux box featuring a complex multi-step attack through a caching server architecture. Exploitation involves HTTP/2 cleartext smuggling to bypass HAProxy restrictions, cache poisoning with XSS to steal admin credentials, CVE-2023-37474 for file access, and command injection in a log service for privilege escalation.

## Attack path
1. [[subdomain-enumeration]] → [[gitbucket]] access with default creds
2. [[parameter-tampering]] → Admin access via login_type modification  
3. [[cache-poisoning]] with XSS → Admin cookie theft
4. [[http-request-smuggling]] (h2c) → Bypass HAProxy to /logs and /download
5. [[cve-2023-37474]] (directory traversal) → SSH key from copyparty
6. [[ssh-access]] as margo
7. [[command-injection]] in log service → [[privilege-escalation]]

## Techniques used
- [[http-request-smuggling]] — HTTP/2 cleartext (h2c) smuggling to bypass HAProxy ACLs
- [[cache-poisoning]] — Poison Varnish cache with XSS payload via X-Forwarded-Host header
- [[xss]] — Steal admin session cookie via cache poisoning
- [[parameter-tampering]] — Modify login_type parameter to gain admin access
- [[cve-2023-37474]] — Directory traversal in copyparty (%2F encoding)
- [[command-injection]] — Inject commands via user-agent field in log processing

## Tools used
- [[nmap]] — Port scanning and service identification
- [[feroxbuster]] — Directory brute force
- wfuzz — Subdomain fuzzing
- h2csmuggler — HTTP/2 smuggling exploitation
- [[python]] — Scripting and payload execution
- [[curl]] — HTTP requests and cache poisoning
- thrift — Log service communication
- [[chisel]] — SOCKS proxy for tunneling
- [[ssh]] — Remote access with private key
- nc — Reverse shell connections

## Services / ports
- 22/tcp — [[ssh]] (OpenSSH 8.9p1)
- 80/tcp — [[http]] (HAProxy → Varnish → Flask)
- 8080/tcp — [[http]] (GitBucket)
- 9090/tcp — Thrift log service
- 3923/tcp — copyparty file server

## Lessons / notes
- Caching servers introduce complex attack surfaces for poisoning and smuggling
- HTTP/2 cleartext smuggling can bypass WAF/proxy restrictions
- X-Forwarded-Host header reflection enables cache poisoning
- Default GitBucket credentials (root:root) are a common misconfiguration
- Non-HttpOnly session cookies vulnerable to XSS theft
- Directory traversal via URL encoding (%2F) bypasses path restrictions
- Command injection in log processing services is a common vulnerability pattern
