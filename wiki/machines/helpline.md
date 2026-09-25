---
type: machine
title: Helpline
platform: htb
os: windows
difficulty: hard
tags: [windows, web, ad]
solved: 2026-07-09
sources: [[htb-helpline]]
related: []
---
# Helpline
> Hard Windows box featuring ManageEngine ServiceDesk Plus with multiple vulnerabilities including XXE, LFI, and SQL injection. Exploit CVE-2017-9362 for file read, CVE-2017-11511 for database backup download, and crack bcrypt hashes to obtain credentials.
## Attack path
1. Access [[http]] (8080) running ManageEngine ServiceDesk Plus 9.3
2. Login with default guest credentials (guest/guest)
3. Find Password Audit.xlsx with hidden sheet containing credentials
4. Exploit CVE-2017-9362 XXE vulnerability to read files from system
5. Exploit CVE-2017-11511 LFI to download PostgreSQL database backup
6. Crack bcrypt hashes from aaapassword.sql and aaalogin.sql using [[hashcat]]
7. (Writeup incomplete - mentions Windows vs Kali paths)
## Techniques used
- [[xxe]] — XML External Entity vulnerability in ManageEngine API for arbitrary file read
- [[lfi]] — Local File Include via download-file endpoint for database backup extraction
- [[password-cracking]] — Cracked bcrypt hashes with hashcat (slow, 40+ days for full rockyou)
- [[web-vuln-scanning]] — Found default guest credentials and hidden Excel sheet
## Tools used
- [[nmap]]
- [[smbmap]]
- python (custom XXE script)
- [[hashcat]]
- Excel (VBA editor)
## Services / ports
- [[http]] (8080) — ManageEngine ServiceDesk Plus 9.3
- [[rpc]] (135) — Windows RPC
- [[smb]] (445) — Microsoft-DS
- [[winrm]] (5985) — WinRM for potential access
## Lessons / notes
- ManageEngine SDP 9.3 has multiple critical vulnerabilities (XXE, LFI, authentication bypass)
- Bcrypt hashes are extremely slow to crack (40+ days for full rockyou)
- Excel files can have hidden sheets accessible via VBA editor (Alt+F11)
- XXE can be used to read files but SMB/HTTP exfiltration may fail with SYSTEM hashes
