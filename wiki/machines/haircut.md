---
type: machine
title: Haircut
platform: htb
os: linux
difficulty: medium
tags: [linux, web, parameter-injection, suid, privesc]
solved: 2026-07-09
sources: [[htb-haircut]]
related: []
---
# Haircut
> PHP web application invoking curl with user-controlled URL input, vulnerable to parameter injection for webshell upload and SUID screen binary exploitation for privilege escalation.

## Attack path
1. [[parameter-injection]] in curl command via exposed.php URL parameter
2. [[webshell]] upload using curl `-o` option to write PHP shell to uploads directory
3. [[suid]] binary exploitation of screen 4.5.0 via ld.so.preload hijack
4. [[suid]] binary execution for root shell

## Techniques used
- [[parameter-injection]] — Injecting curl options like `-o` into URL parameter to write malicious files to server filesystem
- [[webshell]] — PHP webshell execution through uploaded .aspx file in accessible uploads directory
- [[suid]] — Exploiting SUID screen binary with log file creation to write malicious library path to `/etc/ld.so.preload`
- [[pickle]] — Screen exploit uses compiled shared library with `__attribute__ ((__constructor__))` to execute before main

## Tools used
- [[nmap]]
- gobuster
- [[curl]]
- nc
- gcc
- [[netcat]]

## Services / ports
- [[ssh]] (22)
- [[http]] (80)

## Lessons / notes
- Character filtering may block direct command injection but allow parameter injection
- SUID screen binary can write to arbitrary files via `-L` (log) option, including `/etc/ld.so.preload`
- The `ld.so.preload` file forces library preloading for all executables, enabling code execution as root
- PHP filter blocks many common webshell extensions but allows.txt upload with copy/rename to.php
