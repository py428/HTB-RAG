---
type: machine
title: Appsanity
platform: htb
os: windows
difficulty: hard
tags: [windows, iis, jwt, ssrf, file-upload, reverse-engineering, dll, hard]
solved: 2026-07-09
sources: [[htb-appsanity]]
related: []
---
# Appsanity

> Appsanity consists of two ASP.NET applications sharing JWT secrets, requiring hidden field manipulation, SSRF exploitation, file upload bypass, DLL hijacking, and binary reverse engineering for administrator access.

## Attack path

1. [[hidden-input-manipulation]] — Modify Acctype parameter to escalate to doctor role
2. [[jwt-token-reuse]] — Reuse JWT cookie between applications with shared secret
3. [[ssrf]] — Server-side request forgery to discover internal port 8080
4. [[file-upload-bypass]] — Upload ASPX webshell disguised as PDF with magic bytes
5. [[dll-hijacking]] — Exploit writable Libraries directory for DLL side-loading

## Techniques used

- [[hidden-input-manipulation]] — Manipulating hidden form fields for role escalation
- [[jwt-token-reuse]] — Cookie replay between applications with shared JWT secrets
- [[ssrf]] — Internal port scanning and file access via prescription link feature
- [[file-upload-bypass]] — PDF magic bytes preservation for webshell upload
- [[registry-enumeration]] — Extracting encryption keys from Windows Registry
- [[password-reuse]] — Using recovered encryption key for WinRM authentication
- [[dll-hijacking]] — Writable Libraries directory for DLL side-loading attack
- [[binary-reverse-engineering]] — Ghidra/x64dbg analysis of C++ binary
- [[chisel-tunnel]] — Port forwarding for internal service access

## Tools used

- [[nmap]] — TCP port scanning and service identification
- [[ffuf]] — Subdomain and port fuzzing via SSRF
- [[feroxbuster]] — Web directory brute forcing
- [[netcat]] — Reverse shell connections and service interaction
- netexec (formerly CrackMapExec) — WinRM password spraying
- [[evil-winrm]] — WinRM shell access
- [[impacket]] — SMB server for file exfiltration
- DotPeek — .NET binary decompilation
- Ghidra — C++ binary reverse engineering
- x64dbg — Dynamic binary analysis and debugging
- Process Monitor — Process and file system monitoring
- msfvenom — Malicious DLL generation

## Services / ports

- 80/tcp — http — Microsoft IIS 10.0 redirecting to https://meddigi.htb
- 443/tcp — https — Microsoft IIS 10.0 with TLS certificate
- 5985/tcp — wsman — WinRM for remote management
- 8080/tcp — http — Internal ExaminationPanel management interface
- 100/tcp — unknown — ReportManagement custom service

## Lessons / notes

- Hidden form fields often contain critical access control parameters
- Applications sharing JWT secrets allow cookie replay between sites
- SSRF can be used for internal network reconnaissance when direct access blocked
- File upload filters can be bypassed by preserving magic bytes while modifying content
- .NET binaries often contain hardcoded credentials in decompiled code
- Windows Registry frequently stores application encryption keys
- Writable directories in Program Files can indicate DLL hijacking opportunities
- Custom TCP ports may indicate custom services worth investigating
- Binary reverse engineering essential for understanding proprietary services
- Process monitoring helps identify file system interactions andDLL loading behavior

## CVEs

- No specific CVEs exploited — relies on application misconfigurations and custom vulnerabilities
