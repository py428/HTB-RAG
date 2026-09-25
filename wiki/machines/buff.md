---
type: machine
title: Buff
platform: htb
os: windows
difficulty: easy
tags: [windows, web, buffer-overflow, privesc, cloudme]
solved: 2026-07-09
sources: [[htb-buff]]
related: []
---
# Buff
> Easy Windows box running Gym Management System with unauthenticated RCE vulnerability and CloudMe file sync service with buffer overflow. Initial access through webshell upload exploiting Gym Management System, followed by privilege escalation via CloudMe buffer overflow with custom shellcode through port forwarding.

## Attack path
1. [[file-upload]] — Exploit Gym Management System unauthenticated file upload RCE
2. [[webshell-upload]] — Deploy PHP webshell to get initial shell as shaun
3. [[port-forwarding]] — Set up Chisel tunnel to access CloudMe on localhost:8888
4. [[buffer-overflow]] — Exploit CloudMe 1.11.2 buffer overflow with custom reverse shell shellcode
5. [[shellcode-custom]] — Generate custom shellcode for reverse shell as administrator

## Techniques used
- [[file-upload]] — Unauthenticated file upload in Gym Management System with extension bypass
- [[webshell-upload]] — PHP webshell uploaded with PNG magic bytes to bypass filters
- [[port-forwarding]] — Chisel tunneling to reach localhost-only CloudMe service
- [[buffer-overflow]] — SEH-based buffer overflow in CloudMe 1.11.2 with POP/POP/RET chain
- [[shellcode-custom]] — Custom msfvenom shellcode for reverse TCP shell

## Tools used
[[nmap]], [[gobuster]], Python (exploit), [[smbclient]], [[impacket]], [[chisel]], msfvenom, [[netcat]]

## Services / ports
[[http]] (8080 - XAMPP), [[smb]] (445), CloudMe (8888 - localhost only)

## Lessons / notes
- Gym Management System had unauthenticated file upload vulnerable to RCE
- Upload bypass required PNG magic bytes and .php.png double extension
- Windows Defender blocked uploads with "system" keyword but could be bypassed with HTML
- CloudMe 1.11.2 on localhost:8888 vulnerable to buffer overflow
- SEH exploitation with PUSH ESP; RET gadget to redirect execution to shellcode
- Chisel port forwarding required to reach localhost-only CloudMe service
- Custom msfvenom shellcode used for stageless reverse TCP shell
