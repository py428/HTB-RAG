---
type: machine
title: SolarLab
platform: htb
os: windows
difficulty: medium
tags: [windows, web, sqli, cve, ad, privesc]
solved: 2026-07-09
sources: [[htb-solarlab]]
related: []
---
# SolarLab
> Medium Windows box featuring SMB enumeration with password spreadsheet, ReportLab PDF generation with CVE-2023-33733 for RCE, and OpenFire with CVE-2023-32315 for admin creation and plugin RCE.

## Attack path
1. Enumerate [[smb]] share with guest access to find password spreadsheet
2. Password spray to find valid ReportHub credentials (blakeb)
3. Exploit [[cve-2023-33733]] in ReportLab PDF generation for RCE
4. Two paths to openfire user: database creds or CVE-2023-32315 exploit
5. Decrypt OpenFire administrator password from embedded database
6. Use [[psexec]] with admin creds for system shell

## Techniques used
- [[password-spray]] — Username enumeration and password spraying from spreadsheet
- [[cve-2023-33733]] — ReportLab PDF library RCE via color attribute
- [[cve-2023-32315]] — OpenFire path traversal for admin creation
- [[openfire-plugin-rce]] — Malicious JAR plugin upload for code execution
- [[runascs]] — Credential-based command execution as another user

## Tools used
- [[nmap]]
- [[feroxbuster]]
- [[netexec]]
- [[smbclient]]
- [[ffuf]]
- [[chisel]]
- [[runascs]]
- psexec.py

## Services / ports
- [[smb]] (445) — Guest access to Documents share
- [[http]] (80, 6791) — nginx with ReportHub application
- [[rpc]] (135)

## Lessons / notes
- SMB guest access can provide valuable password spreadsheets
- Error message enumeration helps identify valid usernames
- ReportLab CVE-2023-33733 allows RCE via malformed color attributes
- Payload length limits can be bypassed by targeting different fields
- OpenFire embedded database contains encrypted credentials
- Unicode path traversal (%u002e%u002e/) bypasses filters in OpenFire
- OpenFire plugins are JAR files that can execute arbitrary code
