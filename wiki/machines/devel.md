---
type: machine
title: Devel
platform: htb
os: windows
difficulty: easy
tags: [windows, ftp, iis, webshell, kernel-exploit, privesc]
solved: 2026-07-09
sources: [[htb-devel]]
related: []
---

# Devel

> Beginner Windows box with anonymous FTP access to web root enabling webshell upload, followed by multiple kernel exploitation paths for system privilege escalation.

## Attack path

1. Access anonymous [[ftp]] server which shares web root directory
2. Upload ASPX webshell to gain RCE via IIS
3. Use webshell for initial enumeration and privilege escalation
4. Expit Windows kernel vulnerability (MS11-046) for SYSTEM shell
5. Alternative: Use Metasploit for kernel exploitation (MS10-015)

## Techniques used

- [[anonymous-ftp]] — FTP anonymous login with web root access
- [[webshell]] — Upload ASPX webshell for remote code execution
- [[kernel-exploit]] — MS11-046 AFD.sys local privilege escalation
- [[alternative-exploitation]] — Multiple kernel exploits available (MS10-015, MS10-073, MS10-092, MS11-046, MS12-042, MS13-005)

## Tools used

- [[nmap]] — Port scanning and service enumeration
- [[ftp]] — Webshell upload to web directory
- [[netcat]] — Reverse shell catch listener
- smbserver.py (Impacket) — File sharing for exploit binary transfer
- [[hashcat]] — Not needed (alternate exploit path)
- Watson — Local privilege escalation enumeration
- Metasploit — Kernel exploit automation

## Services / ports

- [[ftp]] (21) — Anonymous access with web root write permissions
- [[http]] (80) — IIS 7.5 web server

## Lessons / notes

- Anonymous FTP with web root access is an immediate win - upload webshell directly
- ASPX webshells work well against IIS servers
- Windows 7 without patches is vulnerable to many kernel exploits
- Watson tool identifies missing patches and suggests exploits
- MS11-046 AFD.sys exploit reliable for Windows 7 SP1 x86
- Multiple exploitation paths available (webshell → netcat → privilege escalation)
- Good box for practicing Windows enumeration and kernel exploitation
- Always check FTP anonymous access for web root sharing