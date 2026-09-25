---
type: machine
title: "HTB Beep"
platform: htb
os: linux
difficulty: easy
tags: [linux, web, lfi, webmin, multiple-privesc, elastix]
solved: 2026-07-09
sources: [[htb-beep]]
related: []
---
# HTB Beep
> Beep was an easy Linux box running Elastix PBX software with multiple attack paths. LFI in vtigercrm leads to password disclosure, and numerous privilege escalation vectors including sudo nmap, chmod, webmin credentials, shellshock, and SMTP webshell upload.
## Attack path
1. Enumerate services to find Elastix on [[https]] (443) and webmin on TCP 10000  
2. Discover [[lfi]] in /vtigercrm/graph.php with null byte injection
3. Read Elastix configuration files to obtain database credentials
4. Multiple paths to root: [[sudo-abuse]] with nmap/chmod, [[webmin]] access, [[shellshock]], or webshell via SMTP
## Techniques used
- [[lfi-with-null-byte]] — Local file inclusion in vtigercrm graph.php using %00 truncation on old PHP versions
- [[sudo-abuse]] — Privilege escalation via sudo nmap interactive mode or sudo chmod for SUID binary creation  
- [[webmin]] — Remote administration interface with default credential reuse
- [[shellshock]] — CGI bash vulnerability exploitation via User-Agent header injection
- [[webshell-upload-smtp]] — Upload PHP webshell via email to asterisk user and execute via LFI
## Tools used
[[nmap]], [[dirsearch]], [[john]], [[svwar]], [[chisel]], [[netcat]], [[curl]], [[telnet]]
## Services / ports
- [[http]] (80) - Apache 2.2.3 redirecting to HTTPS
- [[https]] (443) - Elastix web interface
- [[smtp]] (25) - Postfix for email operations
- [[imap]] (143, 993) - Cyrus IMAP server
- [[pop3]] (110, 995) - Cyrus POP3 server
- [[ssh]] (22) - OpenSSH 4.3
- webmin (10000) - Webmin administration interface
## Lessons / notes
- Multiple valid exploitation paths demonstrate importance of comprehensive enumeration
- Legacy PHP versions allow null byte truncation for LFI exploitation  
- sudo permissions can be abused for privesc via various techniques
- SMTP can be leveraged for file upload when other methods are blocked
