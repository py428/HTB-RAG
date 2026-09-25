---
type: machine
title: Bizness
platform: htb
os: linux
difficulty: easy
tags: [linux, web, privesc, cve, deserialization, database]
solved: 2026-07-09
sources: [[htb-bizness]]
related: []
---
# Bizness
> Apache OFBiz exploitation box featuring pre-auth RCE via XML-RPC deserialization. Attack path: exploit CVE-2023-49070 for initial shell, exfiltrate Derby database to extract admin hash, crack hash for root access via su.

## Attack path
1. [[cve-2023-49070]] — Exploit Apache OFBiz XML-RPC deserialization for pre-auth RCE
2. [[deserialization]] — Use ysoserial to generate malicious Java serialized payload
3. [[database-exfiltration]] — Exfiltrate Apache Derby database files via tar and nc
4. [[hash-cracking]] — Extract and crack admin hash from Derby USER_LOGIN table
5. [[privilege-escalation]] — Use cracked admin password for root via su

## Techniques used
- [[cve-2023-49070]] — Exploit pre-auth RCE in Apache OFBiz XML-RPC endpoint
- [[deserialization]] — Craft ysoserial CommonsBeanutils1 payload for code execution
- [[database-exfiltration]] — Exfiltrate Derby database from containerized environment
- [[hash-cracking]] — Crack OFBiz custom SHA1+salt hash format using hashcat
- [[privilege-escalation]] — Password reuse allows root access via su

## Tools used
[[nmap]], [[feroxbuster]], hashcat, ysoserial, ij, dbeaver

## Services / ports
[[ssh]] (22), [[http]] (80), [[https]] (443)

## Lessons / notes
- Apache OFBiz XML-RPC endpoint vulnerable to pre-auth RCE via deserialization even in latest versions
- OFBiz uses custom SHA1 hash format with salt stored in separate field ($SHA$d$salt$hash)
- Derby database files can be exfiltrated and analyzed offline using ij or DBeaver
- Database contains plaintext passwords in legacy OFBiz installations
- Java 11 may be required for ysoserial payload generation due to module access restrictions
