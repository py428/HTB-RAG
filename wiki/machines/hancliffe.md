---
type: machine
title: Hancliffe
platform: htb
os: windows
difficulty: hard
tags: [windows, web, ssti, tunneling, firefox-credentials, buffer-overflow]
solved: 2026-07-09
sources: [[htb-hancliffe]]
related: []
---
# Hancliffe
> Java-based Nuxeo CMS behind nginx with URI normalization bypass for SSTI RCE, Unified Remote exploitation for user escalation, Firefox credential extraction, and custom buffer overflow with socket reuse for privilege escalation.

## Attack path
1. [[uri-normalization]] bypass to access internal Nuxeo application
2. [[ssti]] in Nuxeo login.jsp for RCE as svc_account
3. [[unified-remote]] RCE via protocol abuse for shell as clara
4. [[firefox-credentials]] extraction using [[firepwd]] for development user
5. [[buffer-overflow]] in custom MyFirstApp.exe with [[socket-reuse]] for administrator shell

## Techniques used
- [[uri-normalization]] — NGINX passes `/maintenance/..;/` to backend Java which treats `;` as path separator, bypassing access controls to reach internal Nuxeo
- [[ssti]] — Java template injection in Nuxeo login.jsp with `${"".getClass().forName("java.lang.Runtime").getMethod("getRuntime", null).invoke(null, null).exec(...)}` for RCE
- [[unified-remote]] — Binary protocol exploitation to send keystrokes and download/execute payload via certutil
- [[firefox-credentials]] — Extracting saved passwords from Firefox profile using key4.db and logins.json with master key derivation
- [[buffer-overflow]] — Custom Windows application with strcpy overflow in _SaveCreds, exploited via socket reuse to receive full shellcode
- [[socket-reuse]] — Recovering socket descriptor from stack and calling recv to stage larger shellcode when buffer space is limited

## Tools used
- [[nmap]]
- [[feroxbuster]]
- [[chisel]]
- [[msfvenom]]
- [[firepwd]]
- pwntools
- x32dbg
- metasm

## Services / ports
- [[http]] (80) — nginx front-end
- [[http]] (8000) — H@$hPa$$ password manager
- TCP 9999 — MyFirstApp.exe custom application

## Lessons / notes
- URI normalization differences between web servers can lead to access control bypasses
- Java SSTI payloads differ from Python/Jinja2 — require accessing Runtime class explicitly
- Unified Remote protocol allows sending keystrokes to execute arbitrary commands
- Firefox stores credentials encrypted with PBKDF2 in key4.db, requiring master password or tooling
- Windows buffer overflows with limited buffer space can use socket reuse to stage shellcode
- Socket reuse preserves existing connection while receiving additional shellcode over same channel
