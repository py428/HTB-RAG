---
type: machine
title: Frolic
platform: htb
os: linux
difficulty: easy
tags: [linux, web, playsms, buffer-overflow, ret2libc, privesc]
solved: 2026-07-09
sources: [[htb-frolic]]
related: []
---
# Frolic
> Frolic is an easy Linux box involving a series of puzzles to obtain PlaySMS credentials, exploiting the application for RCE, and then performing a ret2libc buffer overflow attack on a SUID binary to gain root access.

## Attack path
1. Solve admin login JavaScript to get password
2. Decode Ook! brainfuck code to get password  
3. Decode base64 and extract zip file
4. [[zip-password-cracking]] with fcrackzip
5. Decode brainfuck in PHP to get PlaySMS password
6. [[playsms-exploit]] for RCE as www-data
7. Find SUID binary in /home/ayush/.binary/rop
8. [[buffer-overflow]] with [[ret2libc]] to get root shell

## Techniques used
- [[javascript-analysis]] — Extracting password from client-side JavaScript
- [[brainfuck-decoding]] — Decoding Ook! and brainfuck esoteric languages
- [[zip-password-cracking]] — Brute forcing zip password with fcrackzip
- [[playsms-exploit]] — CSV upload vulnerability for code execution
- [[buffer-overflow]] — Overflowing buffer to control EIP
- [[ret2libc]] — Return to libc attack with system() and /bin/sh

## Tools used
[[nmap]], [[smbmap]], [[gobuster]], python, [[openssl]], [[nc]], fcrackzip, [[gdb]], PEDA

## Services / ports
- 22/tcp — [[ssh]]
- 139/tcp — [[smb]]
- 445/tcp — [[smb]]
- 1880/tcp — [[http]] (Node-RED)
- 9999/tcp — [[http]] (nginx)

## Lessons / notes
- Multi-stage puzzle chain to obtain PlaySMS credentials
- PlaySMS CSV upload vulnerability allows PHP code execution
- No ASLR and disabled security controls made exploitation straightforward
- ret2libc requires finding system(), exit(), and "/bin/sh" addresses in libc
- ASLR was disabled: echo 0 > /proc/sys/kernel/randomize_va_space

## Exploitation details
- Buffer offset: 52 bytes to EIP
- system() address: 0xb7e53da0
- exit() address: 0xb7e479d0  
- "/bin/sh" address: 0xb7f74a0b
- Payload: 52*A + system() + exit() + "/bin/sh"
