---
type: machine
title: "HTB Rabbit"
platform: htb
os: windows
difficulty: insane
tags: [windows, ad, exchange, php, mysql, privesc]
solved: 2026-07-09
sources: [[htb-rabbit]]
related: []
---

# HTB Rabbit

> Rabbit was all about enumeration and rabbit holes. I'll work to quickly eliminate vectors and try to focus in on ones that seem promising. I'll find an instance of Complain Management System, and exploit multiple SQL injections to get a dump of hashes and usernames. I'll use them to log into an Outlook Web Access portal, and use that access to send phishing documents with macros to get a shell. From there, I'll find one of the webservers running as SYSTEM and write a webshell to get a shell.

## Attack path

1. [[sqli]] in Complain Management System to dump user hashes
2. [[hash-cracking]] MySQL hashes to obtain user passwords
3. [[phishing]] via Exchange OWA with macro-enabled documents
4. [[macro]] execution in OpenOffice for initial shell access
5. [[file-upload]] via WAMP server writeable directory for SYSTEM shell
6. [[constrained-language-mode]] bypass via PowerShell v2

## Techniques used

- [[sqli]] — Exploiting UNION and boolean-based blind SQL injection in Complain Management System
- [[hash-cracking]] — Cracking MySQL MD5 hashes with sqlmap and crackstation
- [[phishing]] — Sending malicious OpenOffice documents via Exchange OWA email
- [[macro]] — Creating auto-executing macros in OpenOffice documents for reverse shells
- [[scheduled-task]] — Analyzing Windows scheduled tasks for automation and privilege escalation
- [[file-upload]] — Writing PHP webshell to WAMP directory with user write permissions
- [[constrained-language-mode]] — Bypassing PowerShell CLM using PowerShell v2
- [[file-permission-abuse]] — Exploiting weak permissions on C:\wamp64\www directory

## Tools used

- [[nmap]], [[feroxbuster]], [[sqlmap]], [[libreoffice]], [[netcat]], [[powershell]]

## Services / ports

- [[http]] (80/443) — IIS 7.5 with OWA and Apache 2.4.27 with various applications
- [[smtp]] (25/587) — Microsoft Exchange SMTP
- [[mysql]] (3306) — MySQL 5.7.19 database backend
- [[ldap]] (389/636/3268/3269) — Active Directory LDAP services
- [[kerberos]] (88) — Windows Kerberos
- [[winrm]] (5985) — Windows Remote Management

## Lessons / notes

- Automated email processing systems can be exploited for macro-based initial access
- Exchange OWA provides reliable email delivery for internal phishing campaigns
- Multiple SQL injection vulnerabilities in legacy applications provide different exploitation paths
- PowerShell constrained language mode can be bypassed using older PowerShell versions
- WAMP server installations often have overly permissive directory permissions
- Windows scheduled tasks provide insight into automated security processes
- OpenOffice macro execution is less likely to be blocked than Office macros
- File race conditions can be exploited for privilege escalation in multi-user environments

## CVEs / exploits

- Complain Management System multiple SQL injection vulnerabilities
- PowerShell constrained language mode bypass via v2
