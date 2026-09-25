---
type: machine
title: Love
platform: htb
os: windows
difficulty: easy
tags: [windows, web, privesc, file-upload]
solved: 2026-07-09
sources: [[htb-love]]
related: []
---

# Love
> Windows box with SSRF on staging subdomain to access localhost-only pages, credential leak for voting system, file upload RCE, and AlwaysInstallElevated MSI abuse for SYSTEM.

## Attack path
1. [[ssrf]] — staging.love.htb beta.php makes requests to internal URLs
2. [[credential-leak]] — SSRF reveals voting system credentials from localhost:5000
3. [[file-upload-rce]] — authenticated image upload bypass to upload PHP webshell
4. [[alwaysinstallelevated]] — MSI abuse with msfvenom payload for SYSTEM shell

## Techniques used
- [[ssrf]] — staging subdomain URL parameter makes requests to localhost services
- [[subdomain-enumeration]] — TLS certificate reveals staging.love.htb
- [[credential-leak]] — SSRF to localhost:5000 returns admin/@LoveIsInTheAir!!!!
- [[file-upload-rce]] — profile picture upload allows PHP webshell
- [[searchsploit]] — Voting System 1.0 File Upload RCE (authenticated)
- [[alwaysinstallelevated]] — Windows MSI installation as any user runs as SYSTEM
- [[msi-abuse]] — msfvenom-generated MSI executes reverse shell as SYSTEM
- [[password-reuse]] — same credentials work for admin login on both ports

## Tools used
[[nmap]], feroxbuster, smbclient, smbmap, [[mysql]], searchsploit, python2, msfvenom, msiexec, winpeas, nc

## Services / ports
- [[http]] (80, 443, 5000) — Apache with PHP
- [[smb]] (445)
- [[mysql]] (3306) — MariaDB, host-restricted
- [[winrm]] (5985, 5986)

## Lessons / notes
- SSRF can expose localhost-only services and credentials
- TLS certificates often reveal internal subdomains (staging.love.htb)
- File upload vulnerabilities often exist even when extensions seem limited
- searchsploit can quickly identify known vulnerabilities in web applications
- AlwaysInstallElevated Windows policy allows any user to install MSI as SYSTEM
- WinPEAS excellent for Windows privilege enumeration, highlighting AlwaysInstallElevated
- Voting System 1.0 has known authenticated RCE via image upload
