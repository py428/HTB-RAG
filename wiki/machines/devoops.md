---
type: machine
title: DevOops
platform: htb
os: linux
difficulty: medium
tags: [linux, web, xml, xxe, git, ssh, python]
solved: 2026-07-09
sources: [[htb-devoops]]
related: []
---
# DevOops
> A blog feed application vulnerable to XXE file read, allowing SSH key exfiltration and initial access. Privilege escalation exploits git history to recover a committed root SSH key that was later removed from the repository.

## Attack path
1. [[xxe]] — Upload malicious XML with external entity to read arbitrary files
2. [[ssh]] — Use exfiltrated SSH key to access as roosa user
3. [[git-history]] — Recover root SSH key from accidental commit in git history
4. [[ssh]] — Use recovered root key for direct SSH access

## Techniques used
- [[xxe]] — XML External Injection via blog feed upload endpoint reads arbitrary files from filesystem
- [[ssh]] — Private key authentication provides direct shell access
- [[git-history]] — Checkout previous commit to recover credentials removed in later version
- [[pickle-deserialization]] — Python pickle RCE via /newpost endpoint (alternative path)

## Tools used
[[nmap]], [[gobuster]], [[curl]], [[ssh]], [[git]], [[python]], [[hashcat]]

## Services / ports
- [[ssh]] (22) — OpenSSH 7.2p2 Ubuntu
- [[http]] (5000) — Gunicorn 19.7.1 Flask application

## Lessons / notes
- XXE via file:// protocol allows reading any file accessible by web user
- Git history preserves "deleted" data — credentials must be properly removed with git filter-branch
- Python pickle deserialization with user input provides trivial RCE
- Flask upload endpoints may process XML without proper entity sanitization
- Gunicorn + Flask combination common for Python web applications
