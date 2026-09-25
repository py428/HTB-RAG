---
type: machine
title: Bitlab
platform: htb
os: linux
difficulty: medium
tags: [ad, linux, web, privesc, gitlab, javascript, tunneling, reverse-engineering]
solved: 2026-07-09
sources: [[htb-bitlab]]
related: []
---
# Bitlab
> GitLab CI/CD exploitation box featuring automated deployment pipelines. Attack path: obtain credentials via JavaScript deobfuscation in bookmarks, access GitLab instance, deploy webshell via git merge automation, pivot through PostgreSQL containers, and reverse engineer Windows binary to extract Putty credentials for root access.

## Attack path
1. [[javascript-deobfuscation]] — Extract GitLab credentials from malicious bookmark link
2. [[web-shell]] — Deploy via GitLab merge request webhook automation
3. [[tunneling]] — Access PostgreSQL container through chisel reverse tunnel
4. [[database-extraction]] — Extract SSH credentials from PostgreSQL database
5. [[binary-reverse-engineering]] — Reverse engineer RemoteConnection.exe to find Putty credentials
6. [[privilege-escalation]] — SSH as root with extracted credentials

## Techniques used
- [[javascript-deobfuscation]] — Decode GitLab login credentials from obfuscated JavaScript in bookmarks.html
- [[web-shell]] — Inject PHP webshell into GitLab profile pages via malicious merge request
- [[git-webhook-abuse]] — Exploit automated git pull on merge to deploy malicious code
- [[tunneling]] — Use chisel reverse tunnel to access containerized PostgreSQL from host
- [[database-extraction]] — Query PostgreSQL user profiles table for SSH credentials
- [[binary-reverse-engineering]] — Debug PE32 executable with x32dbg to extract Putty command-line arguments
- [[privilege-escalation]] — Reuse cracked Putty password for root SSH access

## Tools used
[[nmap]], exiftool, [[chisel]], psql, gdb, x32dbg

## Services / ports
[[ssh]] (22), [[http]] (80), PostgreSQL (5432)

## Lessons / notes
- GitLab's automated deployment via webhooks can be abused for code execution if merge permissions are obtained
- JavaScript bookmarklets often contain obfuscated credentials that can be deobfuscated for initial access
- Containerized databases may require tunneling to access from external networks
- Windows executentials on Linux systems often contain credentials for further lateral movement
- Debugging with x32dbg can reveal command-line arguments even when the executable crashes on invalid input
