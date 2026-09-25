---
type: machine
title: Overgraph
platform: htb
os: linux
difficulty: hard
tags: [linux, web, xss, csrf, ssti, ffmpeg, rce, privesc, pwn]
solved: 2026-07-09
sources: [[htb-overgraph]]
related: []

# Overgraph
> Complex multi-step exploitation involving reflective XSS, client-side template injection (CSTI), cross-site request forgery (CSRF), FFmpeg arbitrary file read, and binary exploitation for initial access and privilege escalation.

## Attack path
1. [[xss]] on graph.htb main page via JavaScript URL protocol in redirect parameter
2. [[csrf]] to update Larry's profile with [[csti]] payload using stolen session
3. [[ssti]] in Angular template to exfiltrate adminToken from localStorage
4. [[ffmpeg-arbitrary-file-read]] via uploaded video to read SSH private key from database server
5. [[binary-exploitation]] of nreport service using heap manipulation and arbitrary file write

## Techniques used
- [[xss]] — Reflective XSS using JavaScript URL protocol (javascript:) in redirect parameter
- [[csrf]] — Cross-site request forgery to update user profile with malicious payload
- [[csti]] — Client-side template injection in Angular framework using {{constructor.constructor()}} syntax
- [[ssti]] — Server-side template injection in Jinja2 template engine for code execution
- [[token-exfiltration]] — Steal adminToken from localStorage using CSTI payload
- [[ffmpeg-arbitrary-file-read]] — Exploit FFmpeg's concat and subfile protocols to read arbitrary files one line at a time
- [[binary-exploitation]] — Heap manipulation and arbitrary file write in nreport binary to gain root access
- [[docker-abuse]] — Container breakout via Portainer web interface for privilege escalation

## Tools used
- [[nmap]] — Port scanning and service enumeration
- [[wfuzz]] — Web directory and subdomain fuzzing
- [[burp]] — HTTP request interception and modification
- [[python]] — Exploit script development and automation
- [[curl]] — HTTP client for testing and exploitation
- [[ffmpeg]] — Video processing tool (exploited for arbitrary file read)
- [[ffmeg-hls-ssrf]] — Custom server for FFmpeg exploitation
- [[pwntools]] — Python exploitation framework for binary attacks
- [[ssh]] — Shell access using stolen private key
- [[nc]] — Netcat for reverse shell handling

## Services / ports
- [[ssh]] (22) — Secure shell access
- [[http]] (80) — nginx reverse proxy to multiple web applications

## Lessons / notes
- Multi-step exploitation chains require patience and careful enumeration of each step
- Client-side template injection in JavaScript frameworks can be as dangerous as server-side SSTI
- FFmpeg's support for multiple protocols and file formats makes it a potential attack vector
- Binary exploitation often requires understanding heap layout and memory corruption techniques
- Docker management interfaces like Portainer can provide container breakout opportunities
- Token-based authentication systems often have weaknesses in how tokens are stored and validated
- Graph databases and GraphQL APIs require different enumeration approaches than traditional REST APIs
