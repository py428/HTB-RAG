---
type: machine
title: Noter
platform: htb
os: linux
difficulty: medium
tags: [web, linux, flask, ftp, command-injection, mysql, privesc, udf, cve]
solved: 2026-07-09
sources: [[htb-noter]]
related: []
---

# Noter
> Noter is a Flask note-taking application with crackable session cookies, FTP access using default password pattern, and RCE via CVE-2021-23639 in md-to-pdf library, with MySQL UDF exploitation for root.

## Attack path
1. [[flask-cookie-cracking]] — Brute force Flask secret with flask-unsign
2. [[username-enumeration]] — Use login oracle or forge cookies to find valid users
3. [[flask-session-forgery]] — Craft cookie for blue user with cracked secret
4. [[password-policy-abuse]] — FTP admin uses `username@site_name!` pattern
5. Download site source from FTP
6. [[cve-exploitation]] — CVE-2021-23639 in md-to-pdf for RCE
7. [[mysql-udf-exploitation]] — Deploy Raptor UDF for root shell

## Techniques used
- [[flask-cookie-cracking]] — Brute force Flask session secret with rockyou.txt
- [[username-enumeration]] — Different error messages for valid vs invalid users
- [[flask-session-forgery]] — Forge cookies with TimestampSigner and TaggedJSONSerializer
- [[password-policy-abuse]] — Default passwords follow `username@site_name!` pattern
- [[cve-exploitation]] — md-to-pdf 4.1.0 vulnerable to JavaScript injection
- [[command-injection]] — Alternative shell escape in subprocess call
- [[mysql-udf-exploitation]] — Load malicious library via INTO DUMPFILE for sys_exec

## Tools used
- [[nmap]]
- [[ftp]]
- flask-unsign
- wfuzz
- feroxbuster
- md-to-pdf
- mysql
- gcc
- raptor_udf2.c

## Services / ports
- FTP (21) — vsftpd 3.0.3
- SSH (22) — OpenSSH 8.2
- HTTP (5000) — Werkzeug/Flask
- MySQL (3306) — localhost only

## Lessons / notes
- Flask cookies use HMAC signing with secret key
- flask-unsign can decode, crack, and sign Flask cookies
- Login error messages often reveal valid usernames
- Password patterns can be guessed from policy documentation
- md-to-pdf processes markdown with embedded JavaScript
- Subprocess calls with shell=True can be exploited with quotes
- MySQL running as root allows UDF privilege escalation
- Raptor UDF creates do_system() function for command execution
