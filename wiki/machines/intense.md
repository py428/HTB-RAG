---
type: machine
title: Intense
platform: htb
os: linux
difficulty: hard
tags: [web, sqli, crypto, snmp, binary-exploitation, privesc]
solved: 2026-07-09
sources: [[htb-intense]]
related: []
---
# Intense
> Intense is a Linux hard box featuring SQLite SQL injection, hash length extension attacks, SNMP exploitation, and complex binary exploitation with canary leaks and ROP chains.

## Attack path
1. Identify [[sqlite-sqli]] via error messages on feedback submission
2. Develop boolean and time-based blind injection techniques
3. Brute-force usernames and password hashes from SQLite database
4. Perform [[hash-extension]] attack to forge admin cookies
5. Access admin panel with [[directory-traversal]] in log viewing
6. Find SNMP read/write community string in configuration files
7. Use [[snmp-arbitrary-command]] to gain shell as Debian-snmp user
8. Exploit buffer overflow in custom note_server binary with canary leak
9. Build ROP chain to bypass ASLR and get root shell

## Techniques used
- [[sqlite-sqli]] — Boolean and time-based blind SQL injection
- [[hash-extension]] — Length extension attack on SHA256-signed cookies
- [[directory-traversal]] — Path traversal in admin log viewing
- [[snmp-arbitrary-command]] — Command execution via NET-SNMP-EXTEND-MIB
- [[canary-leak]] — Stack canary leak via buffer overflow information disclosure
- [[rop-chain]] — Return-oriented programming with libc calls
- [[stack-pivoting]] — Information leak and ROP chain development

## Tools used
- [[nmap]], [[snmpwalk]], [[hash_extender]], [[python]], [[snmp-shell]], [[pwntools]], [[gdb]], [[readelf]], [[checksec]]

## Services / ports
- 22/tcp — [[ssh]]
- 80/tcp — [[http]] (nginx/Python Flask)
- 161/udp — [[snmp]]

## Lessons / notes
- SQLite injection requires different techniques than MySQL (no SLEEP, use zeroblob)
- Hash length extension attacks work against SHA256 when data is known
- SNMP read/write community strings allow arbitrary command execution
- Binary exploitation requires multiple stages: leak canary, leak libc, build ROP
- Stack alignment (16-byte) is required for system() calls in 64-bit
- PIE bypass requires leaking main binary address via return address
