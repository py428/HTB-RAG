---
type: machine
title: Visual
platform: htb
os: windows
difficulty: medium
tags: [windows, web, privesc, ad, build-process-rce, webshell, privilege-recovery, potato]
solved: 2026-07-09
sources: [[htb-visual]]
related: []
---
# Visual
> Visual is a Windows box centered around abusing a Visual Studio build service. The website accepts Git repo URLs and compiles Visual Studio projects, which I exploit by hosting a malicious project with a pre-build action that executes a PowerShell reverse shell. From the webshell, I escalate to SYSTEM using FullPower to recover SeImpersonate privileges, then GodPotato for the final privilege escalation.

## Attack path
1. Enumerate HTTP service and identify Visual Studio build functionality via [[file-enumeration]]
2. Host malicious [[build-process-rce]] project with pre-build PowerShell command using [[docker]] and [[gitea]]
3. Submit project URL to get reverse shell as enox user
4. Deploy [[webshell]] to XAMPP web root for persistent access
5. Use [[privilege-recovery]] (FullPowers) to restore SeImpersonate privilege
6. Exploit SeImpersonate with [[potato]] (GodPotato) to get SYSTEM shell

## Techniques used
- [[build-process-rce]] — Abusing Visual Studio pre-build events to execute arbitrary PowerShell commands
- [[webshell]] — Writing PHP webshell to XAMPP htdocs directory for persistent access
- [[privilege-recovery]] — Using FullPowers to restore SeImpersonate privilege stripped from Local Service
- [[potato]] — GodPotato exploitation using SeImpersonate to gain SYSTEM privileges

## Tools used
- [[nmap]] — Port scanning and service enumeration
- [[feroxbuster]] — Directory brute force on web server
- docker — Running Gitea instance for Git hosting
- gitea — Git server for hosting malicious Visual Studio project
- dotnet — Building .NET 6.0 projects on Linux
- [[netcat]] — Reverse shell listener
- powershell — Command execution and reverse shells
- FullPowers — Privilege recovery tool
- GodPotato — Potato exploit for SYSTEM access

## Services / ports
- 80/tcp — [[http]] (Apache httpd 2.4.56 with PHP 8.1.17, XAMPP)

## Lessons / notes
- Build process exploitation: Pre-build events in .csproj files execute arbitrary commands during compilation
- XAMPP default configuration exposes web root at C:\xampp\htdocs for writable webshell deployment
- Local Service runs with reduced privileges; FullPowers can recover SeImpersonate via scheduled task trick
- GodPotato is the current go-to exploitation for SeImpersonate → SYSTEM on modern Windows
- Git URLs work for project submission; hosting a Git server locally enables malicious project delivery
