---
type: machine
title: SolidState
platform: htb
os: linux
difficulty: medium
tags: [linux, email, rbash, privesc]
solved: 2026-07-09
sources: [[htb-solidstate]]
related: []
---
# SolidState
> Medium Linux box featuring James mail server with default admin credentials, directory traversal to write bash completion scripts for initial shell, restricted shell escape, and cron job hijacking for root.

## Attack path
1. Access James admin interface with default root/root credentials
2. Enumerate users and reset passwords to access email via POP3
3. Find SSH credentials in email for mindy user with [[rbash-escape]]
4. Exploit [[james-directory-traversal]] to write bash completion script
5. Trigger on SSH login for reverse shell, escaping [[rbash-escape]]
6. Find writable Python script in cron and hijack for root shell

## Techniques used
- [[james-directory-traversal]] — Path traversal in username creation for arbitrary file write
- [[rbash-escape]] — SSH -t bash and bash completion script execution
- [[cronjob-hijack]] — Modify world-writable Python script executed by cron

## Tools used
- [[nmap]]
- gobuster
- [[nc]]
- telnet
- [[sshpass]]
- pspy

## Services / ports
- [[ssh]] (22) — OpenSSH 7.4
- [[smtp]] (25) — James SMTP 2.3.2
- [[http]] (80) — Apache 2.4.25
- [[pop3]] (110) — James POP3 2.3.2
- nntp (119) — James NNTP
- james-admin (4555) — James Remote Admin 2.3.2

## Lessons / notes
- James mail server has default root/root credentials
- Directory traversal in username creation allows writing to arbitrary paths
- Bash completion scripts in /etc/bash_completion.d execute on user login
- rbash can be escaped with SSH -t bash flag
- World-writable scripts in cron are privilege escalation vectors
- James stores emails in filesystem with predictable paths
