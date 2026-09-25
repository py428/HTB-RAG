---
type: machine
title: Proper
platform: htb
os: windows
difficulty: hard
tags: [web, sqli, php, rfi, windows-privesc, arbitrary-write]
solved: 2026-07-09
sources: [[htb-proper]]
related: []
---
# Proper
> Windows IIS/PHP server with hashed URL parameters requiring salt leak, SQL injection in ORDER BY clause, time-of-check-time-of-use SMB file include vulnerability, and arbitrary file write via cleanup service for SYSTEM.

## Attack path
1. Enumerate [[http]] (80) with [[nmap]] and gobuster
2. Leak SECURE_PARAM_SALT from PHP error message
3. Calculate MD5 hashes for URL parameters
4. Perform [[sqli]] in ORDER BY clause with sqlmap --eval
5. Crack database hashes for login credentials
6. Exploit TOCTOU in [[rfi]] over SMB for shell
7. Abuse cleanup service for [[arbitrary-write]] as SYSTEM
8. Use WerTrigger to get SYSTEM shell

## Techniques used
- [[parameter-hashing]] — MD5 hash with salt required for URL parameters
- [[sqli]] — Boolean-based blind injection in ORDER BY clause
- [[sqli-with-eval]] — Used sqlmap --eval to calculate hashes dynamically
- [[toctou]] — Race condition between file_get_contents and include
- [[smb-authentication]] — Cracked Net-NTLMv2 hash for SMB connection
- [[rfi-over-smb]] — Remote file include via SMB with authentication
- [[arbitrary-write]] — Manipulated cleanup service file restoration paths
- [[wertrigger]] — Windows Error Reporting DLL hijacking for SYSTEM

## Tools used
- [[nmap]]
- gobuster
- Burp Suite
- sqlmap
- [[hashcat]]
- smbserver.py (impacket)
- inotify-tools
- [[netcat]]
- WinPEAS
- Ghidra/IDA/x64dbg

## Services / ports
- [[http]] (80) — Microsoft IIS 10.0 with PHP 7.4.1

## Lessons / notes
- PHP error messages can leak sensitive configuration data like salts
- ORDER BY clause SQLi is limited but exploitable with CASE statements
- sqlmap --eval parameter useful for dynamic parameter calculation
- MD5crypt hashes are fast to crack with common passwords
- SMB remote file include possible when allow_url_include disabled
- TOCTOU vulnerabilities possible when files are read multiple times
- Windows cleanup service running as SYSTEM can be abused for arbitrary write
- Named pipe communication allows custom clients for service interaction
- WerTrigger technique uses Windows Error Reporting for DLL loading
- Multiple paths to SYSTEM: arbitrary read via named pipe, NetworkService token impersonation, CVE-2021-1732
