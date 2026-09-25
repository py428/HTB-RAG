---
type: machine
title: Chemistry
platform: htb
os: linux
difficulty: easy
tags: [linux, web, deserialization, linux-privesc]
solved: 2026-07-09
sources: [[htb-chemistry]]
related: []
---
# Chemistry
> Easy Linux box with Flask CIF processing website vulnerable to pymatgen deserialization (CVE-2024-23346) and AIOHTTP directory traversal (CVE-2024-23334), requiring hash cracking and SSH tunneling for internal site access.

## Attack path
1. [[deserialization]] in pymatgen CIF parser via eval injection (CVE-2024-23346)
2. Crack rosa's MD5 hash from SQLite database with [[hashcat]]
3. SSH as rosa, find internal AIOHTTP site on TCP 8080
4. [[ssh-tunnel]] to access internal monitoring site
5. [[directory-traversal]] in AIOHTTP static assets (CVE-2024-23334) to read root SSH key

## Techniques used
- [[deserialization]] — pymatgen CIF parser eval injection for RCE
- [[hash-cracking]] — MD5 hash from database leaked via CrackStation
- [[ssh-tunnel]] -L flag to access localhost-restricted internal service
- [[directory-traversal]] — AIOHTTP CVE-2024-23334 via follow_symlinks=True

## Tools used
[[nmap]], [[feroxbuster]], [[curl]], tcpdump, [[netcat]], [[ssh]], [[hashcat]]

## Services / ports
- TCP 22 — SSH
- TCP 5000 — Flask CIF analyzer
- TCP 8080 — Internal AIOHTTP monitoring (localhost only)

## Lessons / notes
- Python eval with user input leads to RCE, even with comments about safety
- MD5 hashes still crackable for weak passwords
- Internal services require SSH tunneling when blocked by iptables
- AIOHTTP follow_symlinks=True enables directory traversal

## CVEs
- CVE-2024-23346 — Pymatgen arbitrary code execution via insecure deserialization
- CVE-2024-23334 — AIOHTTP directory traversal via static routes
