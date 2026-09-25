---
type: machine
title: Arctic
platform: htb
os: windows
difficulty: easy
tags: [windows, web, coldfusion, kernel-exploit]
solved: 2026-07-09
sources: [[htb-arctic]]
related: []
---
# Arctic
> Easy Windows box featuring ColdFusion 8 with multiple initial access vectors including unauthenticated file upload and password hash leak, leading to kernel exploitation for privilege escalation.

## Attack path
1. [[coldfusion]] discovery on TCP 8500 with directory listing
2. Password hash leak via directory traversal vulnerability
3. Either: Crack password or use HMAC bypass to login as admin
4. File upload via FCKeditor or scheduled tasks to get JSP shell
5. [[kernel-exploit]] MS10-059 for SYSTEM privilege escalation

## Techniques used
- [[directory-traversal]] — Null byte injection to read password.properties file
- [[coldfusion]] — FCKeditor file upload bypass with JSP payload disguised as TXT
- [[kernel-exploit]] — MS10-059 chimichurri exploit for Windows 2008 R2

## Tools used
- [[nmap]], [[curl]], [[msfvenom]], [[searchsploit]], [[smbserver.py]], [[hashcat]]

## Services / ports
- [[http]] (8500 ColdFusion), [[rpc]] (135, 49154)

## Lessons / notes
- ColdFusion 8 has multiple unauthenticated RCE vulnerabilities
- HMAC-SHA1 hash reuse allows login without password cracking
- FCKeditor upload bypasses extensions filtering with content-type header
- Windows 2008 R2 without hotfixes vulnerable to multiple kernel exploits
- MS10-059 provides reverse shell as SYSTEM without interactive access
- Scheduled tasks can be used for file upload in ColdFusion admin panel
