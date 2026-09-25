---
type: machine
title: Atom
platform: htb
os: windows
difficulty: medium
tags: [ad, windows, web, privesc]
solved: 2026-07-09
sources: [[htb-atom]]
related: []
---
# Atom

> Medium Windows box centered around an Electron application (Heed) with an insecure update mechanism. The exploit path leverages SMB share access, electron-updater signature bypass, PortableKanban credential extraction, and Redis manipulation to achieve domain compromise.

## Attack path
1. [[nmap]] scan reveals [[smb]], [[http]], [[redis]], and [[winrm]] services
2. Access Software_Updates share via guest session
3. Analyze Heed Electron application for update mechanism
4. Exploit [[electron-update-bypass]] by uploading malicious latest.yml
5. Reverse shell execution as jason user
6. Extract PortableKanban config with Redis credentials
7. Decrypt PortableKanban password to access Redis
8. Extract administrator hash from Redis and crack it
9. Access as administrator via [[evil-winrm]]
10. [[printnightmare]] exploit for SYSTEM (alternate path)

## Techniques used
- [[smb-share]] — Guest access to Software_Updates share
- [[electron-update-bypass]] — Signature bypass in electron-updater via single quote in filename
- [[password-decryption]] — DES decryption of PortableKanban stored passwords
- [[redis-access]] — Direct Redis authentication to extract credentials
- [[printnightmare]] — CVE-2021-34527 exploitation for SYSTEM privilege

## Tools used
- [[nmap]], [[smbmap]], [[smbclient]], [[redis-cli]], [[evil-winrm]], [[msfvenom]]

## Services / ports
- 80/tcp [[http]] — Apache httpd 2.4.46
- 445/tcp [[smb]] — Windows 10 Pro 19042
- 5985/tcp [[winrm]] — Microsoft HTTPAPI 2.0
- 6379/tcp [[redis]] — Redis key-value store
- 7680/tcp — pando-pub

## Lessons / notes
- Electron applications using electron-updater can be exploited via malicious update files
- The CVE-2019-16375 exploit bypasses signature checks by embedding single quotes in filenames
- PortableKanban stores credentials encrypted with DES (key: 7ly6UznJ, IV: XuVUm5fR)
- Redis can be accessed directly once credentials are obtained
- PrintNightmare (CVE-2021-34527) allows privilege escalation from user to SYSTEM
- Electron app.asar files can be extracted and analyzed for update configuration
