---
type: machine
title: Bamboo
platform: htb
os: linux
difficulty: medium
tags: [proxy, cve, binary-hijack, paperless]
solved: 2026-07-09
sources: [[htb-bamboo]]
related: []
---
# Bamboo

> Bamboo features a Squid HTTP proxy providing access to a PaperCut NG instance. I'll scan through the proxy, exploit CVE-2023-27350 authentication bypass, enable print scripting for RCE, then hijack a root-executed binary for privilege escalation.

## Attack path
1. Enumerate [[squid]] proxy and use [[spose]] to scan internal services
2. Discover PaperCut NG on ports 9191/9192/9195 through proxy
3. Exploit [[cve-2023-27350]] authentication bypass via SetupCompleted endpoint
4. Enable print scripting and disable sandbox for [[rce]]
5. Execute commands through PaperCut print script functionality
6. Hijack server-command binary executed by root for privilege escalation

## Techniques used
- [[proxy-enumeration]] — Using spose to scan ports through Squid proxy
- [[cve-2023-27350]] — PaperCut authentication bypass via SetupCompleted class
- [[papercut-rce]] — Abusing print scripting functionality for code execution
- [[binary-hijack]] — Replacing server-command binary executed by root process
- [[setuid-exploitation]] — Creating SetUID binary for persistent root access

## Tools used
[[nmap]], [[spose]], [[proxychains]], [[curl]], [[netcat]], Python/poc-exploit

## Services / ports
[[ssh]] (22), [[squid]] (3128), [[http]] (9191, 9192, 9195)

## Lessons / notes
- Squid proxies require specialized tools like spose for internal port scanning
- PaperCut NG has known authentication bypass vulnerabilities in specific versions
- Print scripting in print management applications can provide code execution
- Process monitoring with pspy reveals privileged binary execution patterns
- Binary hijacking works when user controls directory and binary is executed by root
