---
type: machine
title: Book
platform: htb
os: linux
difficulty: medium
tags: [web, sqli, xss, pdf, linux, privesc]
solved: 2026-07-09
sources: [[htb-book]]
related: []
---
# Book
> Library web application vulnerable to SQL truncation for admin access, XSS in PDF generation for file read, and logrotate race condition for root access via symlink attack.

## Attack path
1. Exploit [[sql-truncation]] on registration to overwrite admin@book.htb password
2. Login as admin, identify XSS in PDF export functionality
3. Use [[xss-file-read]] with XMLHttpRequest to exfil /etc/passwd and other files
4. Extract SSH private key from /home/reader/.ssh/id_rsa via PDF XSS
5. SSH as reader, identify logrotate cron running every 5 seconds
6. Exploit [[logrotten]] race condition to create symlink to /etc/bash_completion.d
7. Write reverse shell to bash_completion.d, get root when cron runs

## Techniques used
- [[sql-truncation]] — Bypass unique email constraint by appending spaces to exceed field length
- [[xss-file-read]] — Inject JavaScript in PDF title to read local files via XMLHttpRequest
- [[logrotten]] — Race condition in logrotate allows symlink creation for file write

## Tools used
- [[nmap]], [[gobuster]], [[ssh]], [[nc]], [[gcc]]

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 7.6p1 Ubuntu
- 80/tcp — [[http]] — Apache (library web application)

## Lessons / notes
- SQL truncation occurs when input exceeds field length and trailing whitespace is stripped
- PDF generation with XSS allows server-side file reads since rendering happens server-side
- logrotate race: between mv access.log access.log.1 and touch access.log, replace with symlink
- /etc/bash_completion.d scripts execute for any user starting bash session
- Database cleanup scripts ran every 2 minutes to remove extra admin accounts
