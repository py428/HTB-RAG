---
type: source
title: "HTB Intense writeup"
raw: raw/htb-intense.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[intense]]
---
# Source: HTB Intense writeup
> Detailed exploitation guide covering SQLite SQL injection, hash extension attacks, SNMP command execution, and multi-stage binary exploitation with canary leaks and ROP chains.

## Key facts extracted
- SQLite database uses SHA256 hashes with custom cookie signing
- SNMP community string "SuP3RPrivCom90" provides read/write access
- Custom note_server binary has buffer overflow and information leak vulnerabilities
- Binary has full RELRO, canary, NX, and PIE protections enabled

## Filed into
[[intense]], [[sqlite-sqli]], [[hash-extension]], [[directory-traversal]], [[snmp-arbitrary-command]], [[canary-leak]], [[rop-chain]]
