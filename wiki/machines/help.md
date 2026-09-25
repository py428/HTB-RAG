---
type: machine
title: Help
platform: htb
os: linux
difficulty: easy
tags: [linux, web, kernel]
solved: 2026-07-09
sources: [[htb-help]]
related: []
---
# Help
> Easy Linux box featuring a GraphQL API enumeration for credentials, HelpDeskZ with SQL injection, and kernel exploitation for privilege escalation. Two initial access paths: SQLi after GraphQL auth or unauthenticated file upload bypass.
## Attack path
1. Enumerate [[http]] (3000) running GraphQL API
2. Query GraphQL schema to extract user credentials (helpme@helpme.com / godhelpmeplz)
3. Access HelpDeskZ on [[http]] (80) with found credentials
4. Exploit authenticated SQL injection in ticket attachment parameter
5. Use [[sqlmap]] to dump staff table and crack admin hash (Welcome1)
6. SSH as help user using cracked password
7. Exploit kernel CVE-2017-16995 or CVE-2017-5899 for root
## Techniques used
- [[graphql-enum]] — Enumerated GraphQL schema to extract username and password hash
- [[sqli]] — Blind SQL injection in HelpDeskZ ticket attachment parameter
- [[password-cracking]] — Cracked SHA256 hash from GraphQL and SHA1 from database
- [[kernel-exploit]] — Exploited dirty cow (CVE-2017-16995) or s-nail privsep (CVE-2017-5899)
- Alternative: [[file-upload]] — Unauthenticated PHP upload bypass via HelpDeskZ
## Tools used
- [[nmap]]
- [[curl]]
- [[gobuster]]
- [[sqlmap]]
- [[john]]
- gcc
## Services / ports
- [[http]] (80) — Apache 2.4.18 with HelpDeskZ 1.0.2
- [[http]] (3000) — Node.js Express with GraphQL API
- [[ssh]] (22) — OpenSSH 7.2p2 Ubuntu
## Lessons / notes
- GraphQL APIs expose schema introspection queries for enumeration
- HelpDeskZ 1.0.2 has unauthenticated file upload (files stay in temp despite rejection)
- Bcrypt hashes are very slow to crack but first few results often quick
- Ubuntu 16.04 (4.4.0-116 kernel) vulnerable to multiple local exploits
- Time skew between target and attacker affects upload filename prediction
