---
type: machine
title: Rainbow
platform: htb
os: windows
difficulty: medium
tags: [windows, web, exploit, buffer-overflow, uac]
solved: 2026-07-09
sources: [[htb-rainbow]]
related: []
---
# Rainbow
> Windows-based custom webserver exploit involving buffer overflow vulnerability analysis and weaponization with x32dbg, followed by UAC bypass using fodhelper technique to achieve elevated privileges.

## Attack path
1. Anonymous FTP access provides rainbow.exe binary and dev.txt documentation
2. Manual fuzzing of TCP 8080 custom webserver identifies crash vulnerability
3. Use x32dbg to analyze crash and develop buffer overflow exploit with bad character filtering
4. Weaponize exploit to gain reverse shell as low-integrity user
5. Exploit UAC vulnerability using [[fodhelper]] technique to bypass Windows Defender and elevate privileges

## Techniques used
- [[buffer-overflow]] — Custom webserver crash analysis and exploit development with x32dbg
- [[fodhelper]] — UAC bypass using Windows Registry manipulation of fodhelper.exe
- [[uac-bypass]] — Bypass User Account Control to gain high-integrity shell

## Tools used
- [[nmap]] — Comprehensive port scanning identifying 8 open ports including custom webserver
- [[feroxbuster]] — Web directory enumeration
- [[x32dbg]] — Debugger for exploit development and crash analysis
- [[curl]] — Web fuzzing and vulnerability confirmation
- [[netcat]] — Reverse shell handler

## Services / ports
- FTP (21) — Anonymous FTP with rainbow.exe and dev.txt
- HTTP (80) — IIS 10.0 default page
- HTTP (8080) — Custom Rainbow webserver (vulnerable to buffer overflow)
- SMB (445) — Windows file sharing
- RDP (3389) — Remote Desktop Protocol
- RPC (135, 49668) — Windows RPC services
- NetBios (139) — Windows NetBIOS

## Lessons / notes
- Custom Windows binaries require manual fuzzing and debugging rather than automated scanners
- x32dbg essential for Windows exploit development and bad character identification
- fodhelper UAC bypass works even when user is in Administrator group but UAC blocks access
- Anonymous FTP can provide development files and binaries for vulnerability analysis