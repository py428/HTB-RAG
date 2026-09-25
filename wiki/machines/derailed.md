---
type: machine
title: Derailed
platform: htb
os: linux
difficulty: insane
tags: [linux, web, xss, file-upload, ruby, openmediavault, privesc]
solved: 2026-07-09
sources: [[htb-derailed]]
related: []
---

# Derailed

> Insane-difficulty Ruby on Rails application with WebAssembly buffer overflow enabling blind XSS, leading to file read vulnerability, command injection, and OpenMediaVault RPC abuse for root access.

## Attack path

1. Exploit buffer overflow in WebAssembly username field to bypass XSS filter via date overwrite
2. Use blind XSS against admin browser to enumerate `/administration` page
3. Leak CSRF token and exploit file read vulnerability in report log parameter
4. Read Ruby source code to identify command injection in `open()` function
5. Inject commands via pipe character in report parameter to get shell as rails user
6. Crack database hashes to get OpenMediaVault credentials
7. Abuse OpenMediaVault RPC to add SSH key for root or create cron job
8. Access root shell and retrieve flags

## Techniques used

- [[buffer-overflow]] — WebAssembly username overflow overwrites date string to bypass XSS filters
- [[xss-blind]] — Exploit blind XSS through admin report review system
- [[file-read]] — Abuse insecure `open()` function in Ruby to read arbitrary files
- [[command-injection]] — Pipe character injection in Ruby `open()` for RCE
- [[rpc-abuse]] — Exploit OpenMediaVault RPC for privilege escalation
- [[password-cracking]] — Crack bcrypt hashes from Rails database

## Tools used

- [[ffuf]] — Note enumeration and IDOR brute forcing
- [[feroxbuster]] — Directory brute forcing
- [[hashcat]] — Password cracking with bcrypt ($2a$) hashes
- [[chisel]] — Port forwarding to access localhost services
- [[netcat]] — Reverse shell catch listener
- targetedKerberoast.py — Kerberoasting automation (if needed)
- [[nmap]] — Port scanning and service enumeration

## Services / ports

- [[ssh]] (22) — Secure shell access
- [[http]] (3000) — Ruby on Rails application
- [[http]] (80) — OpenMediaVault web interface (localhost only)

## Lessons / notes

- WebAssembly buffer overflows can enable XSS bypasses through adjacent memory overwriting
- Blind XSS requires reliable callback mechanisms - use custom Python server with CORS headers
- Ruby's `open()` function with pipe prefix enables command injection: `open("|command")`
- File read vulnerabilities via `open()` can leak source code and credentials
- OpenMediaVault RPC allows privilege escalation through SSH key addition or cron creation
- Database credential leaks are common in web application configurations
- Password cracking with hashcat rules effective against password variants mentioned in chat
- Tunneling required when SSH port forwarding disabled - use chisel for localhost access
- Complex multi-stage exploitation requiring understanding of web applications, XSS, and system administration