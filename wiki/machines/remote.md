---
type: machine
title: Remote
platform: htb
os: windows
difficulty: easy
tags: [windows, web, privesc, nfs, registry]
solved: 2026-07-09
sources: [[htb-remote]]
related: []
---
# Remote
> A Windows machine with NFS share暴露 and TeamViewer installation. The attack involves finding credentials in exposed configuration files, cracking hashes, exploiting a Umbraco CMS vulnerability, and extracting TeamViewer passwords from the Windows registry.

## Attack path
1. [[nmap]] scan reveals [[nfs]] share and [[http]] with Umbraco CMS
2. [[nfs-enumeration]] via showmount to find mountable shares
3. Mount [[nfs]] share to access web backup files
4. Extract Umbraco admin hash from database file
5. [[hash-cracking]] with [[hashcat]] to obtain password
6. Umbraco CMS exploit for authenticated RCE
7. [[registry-password-extraction]] from TeamViewer registry keys
8. [[winrm]] access as administrator for SYSTEM shell

## Techniques used
- [[nfs-enumeration]] — Enumerate and mount NFS shares to access backup files
- [[hash-cracking]] — Crack SHA1 hash from Umbraco database using rockyou.txt
- [[cms-exploit]] — Umbraco authenticated XSLT code execution vulnerability
- [[registry-password-extraction]] — Decrypt TeamViewer passwords stored in registry

## Tools used
[[nmap]] | [[showmount]] | [[hashcat]] | [[evil-winrm]] | [[impacket]]

## Services / ports
[[nfs]] (2049) | [[http]] (80) | [[smb]] (445) | [[winrm]] (5985)

## Lessons / notes
- NFS shares on Windows can contain sensitive backup data
- Umbraco CMS files use XML format that can be parsed with strings
- TeamViewer stores encrypted passwords in registry under specific keys
- Static AES key/IV used for TeamViewer password encryption
- WinRM provides convenient shell access as administrator
- Evil-WinRM, psexec.py, and wmiexec.py all work for Windows shell access
