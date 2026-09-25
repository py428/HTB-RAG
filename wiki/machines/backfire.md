---
type: machine
title: Backfire
platform: htb
os: linux
difficulty: medium
tags: [c2, ssrf, command-injection, websocket, jwt, sudo]
solved: 2026-07-09
sources: [[htb-backfire]]
related: []
---
# Backfire

> Backfire focuses on exploiting red team infrastructure - Havoc C2 and HardHatC2. I'll chain SSRF to authentication bypass, exploit authenticated RCE via websocket, forge HardHatC2 JWT tokens with default secret, and abuse sudo iptables rules for root.

## Attack path
1. Enumerate [[http]] services and discover Havoc C2 infrastructure
2. Exploit [[ssrf]] vulnerability (CVE-2024-41570) in Havoc demon callback
3. Chain SSRF with authenticated [[command-injection]] (CVE-2024-41571) via websocket
4. Access HardHatC2 panel using default JWT secret from GitHub
5. Obtain shell through HardHatC2 terminal functionality
6. Exploit sudo iptables-save for [[arbitrary-write]] to gain root access

## Techniques used
- [[ssrf]] — Abusing COMMAND_SOCKET and COMMAND_PIVOT in Havoc demon for internal port scanning
- [[websocket-exploitation]] — Manually constructing websocket frames for authenticated RCE
- [[jwt-forgery]] — Using default HardHatC2 secret from GitHub to forge admin tokens
- [[c2-exploitation]] — Leveraging HardHatC2 terminal feature for command execution
- [[iptables-arbitrary-write]] — Abusing iptables comment injection to write arbitrary files as root

## Tools used
[[nmap]], [[feroxbuster]], Python/pycryptodome, [[wscat]], [[proxychains]]

## Services / ports
[[ssh]] (22), [[http]] (443, 8000), filtered (5000, 7096)

## Lessons / notes
- C2 frameworks often have vulnerabilities in their agent callback handlers
- Websocket exploitation requires understanding frame structure and masking
- Default JWT secrets in open-source C2 frameworks are a common misconfiguration
- iptables-save -f can write arbitrary files when combined with comment injection
- C2 infrastructure can be exploited both externally and internally
