---
type: machine
title: Unicode
platform: htb
os: linux
difficulty: medium
tags: [web, jwt, ad, python, privesc]
solved: 2026-07-09
sources: [[htb-unicode]]
related: []
---
# Unicode
> Medium Linux box demonstrating unicode normalization bypass for directory traversal, JWT jku abuse via open redirect, and parameter injection in PyInstaller binaries.

## Attack path
1. [[jwt-abuse]] via jku header using open redirect to serve malicious JWKS
2. [[directory-traversal]] using unicode characters (‥) bypassing filters
3. [[file-read-via-web]] to read source code via /proc filesystem
4. [[credential-extraction]] from db.yaml to get database credentials
5. [[parameter-injection]] in PyInstaller treport binary for root

## Techniques used
- [[jwt-abuse]] — Forged JWT with malicious jku pointing to open redirect
- [[open-redirect]] — /redirect endpoint abused to host malicious JWKS
- [[unicode-normalization]] — U+2025 (‥) character normalizes to "../" bypassing WAF
- [[directory-traversal]] — Read arbitrary files via display endpoint
- [[file-read-via-web]] — Source code read via /proc/self/cwd/app.py and db.yaml
- [[parameter-injection]] — Injected additional curl parameters via brace expansion

## Tools used
- [[nmap]]
- [[feroxbuster]]
- [[ffuf]]
- [[curl]]
- [[openssl]]
- jwt.io
- Python

## Services / ports
- [[ssh]] — TCP 22 (OpenSSH 8.2p1)
- [[http]] — TCP 80 (nginx 1.18.0 Flask application)

## Lessons / notes
- Unicode normalization can bypass string-based filters (‥ → ../)
- JWT jku header must be validated to prevent arbitrary JWKS inclusion
- Open redirects can be chained with JWT validation bypass
- /proc filesystem provides access to process working directory and source code
- PyInstaller binaries can be extracted and decompiled
- Brace expansion {a,b,c} can bypass space restrictions in command injection

## CVEs
- CVE-2023-33733 — ReportLab PDF generation RCE (not used on this box but similar technique)
