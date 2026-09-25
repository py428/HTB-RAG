---
type: machine
title: Backdoor
platform: htb
os: linux
difficulty: easy
tags: [web, linux, wordpress, gdbserver, privesc]
solved: 2026-07-09
sources: [[htb-backdoor]]
related: []
---
# Backdoor is an easy Linux box featuring a WordPress site with a directory traversal vulnerability in the Ebook Download plugin, which allows reading process information to discover gdbserver for initial access, followed by screen session hijacking for root access.

## Attack path
1. [[directory-traversal]] via vulnerable WordPress plugin
2. [[process-enumeration]] through /proc filesystem to find gdbserver
3. [[gdbserver-exploit]] to get reverse shell as user
4. [[screen-session-hijacking]] to access root session

## Techniques used
- [[directory-traversal]] — Ebook Download plugin allows reading arbitrary files via path traversal
- [[process-enumeration]] — Reading /proc/cmdline reveals gdbserver listening on port 1337
- [[gdbserver-exploit]] — Uploading and executing reverse shell payload through gdb debugger
- [[screen-session-hijacking]] — Multiuser screen session allows accessing root's session

## Tools used
[[nmap]], [[curl]], [[wpscan]], [[gdb]], [[msfvenom]], [[metasploit]]

## Services / ports
[[ssh]] (22), [[http]] (80), 1337 (gdbserver)

## Lessons / notes
- WordPress plugins should be checked for directory traversal vulnerabilities
- /proc filesystem can reveal valuable information about running processes
- gdbserver can be exploited for code execution if accessible
- Screen sessions configured for multiuser mode can be hijacked
- Alternative exploitation methods exist (Metasploit) when manual exploitation fails
