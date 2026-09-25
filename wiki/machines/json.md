---
type: machine
title: Json
platform: htb
os: windows
difficulty: medium
tags: [windows, web, deserialization, privesc]
solved: 2026-07-09
sources: [[htb-json]]
related: []
---
# Json
> Windows Server 2012 R2 box with a .NET deserialization vulnerability in a JSON API endpoint, offering three distinct privilege escalation paths to root.

## Attack path
1. [[deserialization]] via .NET JSON API to get initial shell as userpool
2. Privilege escalation via one of three paths:
   - [[port-forwarding]] to FileZilla admin interface → full FTP access
   - Reverse custom .NET binary to decrypt FTP credentials
   - [[juicypotato]] abuse of SeImpersonatePrivilege

## Techniques used
- [[deserialization]] — .NET JSON deserialization using ysoserial.net with WindowsIdentity gadget and Json.Net formatter
- [[port-forwarding]] — Chisel tunnel to access localhost FileZilla admin interface on TCP 14147
- [[juicypotato]] — Token impersonation abuse on Windows Server 2012 R2

## Tools used
[[nmap]], [[gobuster]], [[chisel]], ysoserial.net, netcat, FileZilla Server, dnSpy, JuicyPotato

## Services / ports
- 21/tcp — [[ftp]] (FileZilla)
- 80/tcp — [[http]] (IIS 8.5)
- 135/tcp, 139/tcp, 445/tcp — [[smb]]/RPC
- 5985/tcp, 47001/tcp — [[winrm]]

## Lessons / notes
- Default admin/admin worked for login
- FileZilla admin port on localhost (14147) was accessible only after port forwarding
- Three different priv esc paths made this box educational for Windows privilege escalation techniques
- SeImpersonatePrivilege is a strong signal for JuicyPotato on pre-2019 Windows versions
