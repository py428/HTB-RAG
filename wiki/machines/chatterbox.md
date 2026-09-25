---
type: machine
title: Chatterbox
platform: htb
os: windows
difficulty: medium
tags: [windows, web, buffer-overflow, seh, privesc]
solved: 2026-07-09
sources: [[htb-chatterbox]]
related: []
---
# Chatterbox
> Windows box running AChat application on TCP 9255/9256 with SEH-based stack buffer overflow vulnerability, exploited via Python script using msfvenom payloads and AutoRunScript migration for stable shell.

## Attack path
1. [[nmap]] port scan finds non-standard ports 9255 and 9256
2. Exploit [[buffer-overflow]] in AChat via Python script with msfvenom shellcode
3. Use [[meterpreter]] AutoRunScript migration to maintain stable shell
4. Abuse [[acl-genericwrite]] on root.txt with icacls grant permissions

## Techniques used
- [[buffer-overflow]] — SEH-based stack overflow in AChat beta v0.150 application
- [[seh-based-exploit]] — Structured Exception Handler exploitation with Unicode-mixed encoding
- [[meterpreter-migration]] — AutoRunScript to migrate from crashing AChat process

## Tools used
[[nmap]], [[netcat]], msfvenom, python, icacls

## Services / ports
- TCP 9255 — AChat monitoring service
- TCP 9256 — AChat vulnerable UDP/TCP service

## Lessons / notes
- Non-standard ports require full port range scanning
- Unicode-mixed encoding avoids bad characters in buffer overflow exploits
- Process migration essential when exploiting unstable applications
- icacls can grant file permissions even without full read access
