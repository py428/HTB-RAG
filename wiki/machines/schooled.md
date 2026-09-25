---
type: machine
title: Schooled
platform: htb
os: freebsd
difficulty: medium
tags: [web, privesc, freebsd, moodle]
solved: 2026-07-09
sources: [[htb-schooled]]
related: []
---
# Schooled
> Schooled is a medium FreeBSD box featuring a Moodle learning management system. The attack path involves chained Moodle exploits (stored XSS, privilege escalation CVE-2021-14321, plugin upload RCE), database credential harvesting, and abuse of the FreeBSD package manager for privilege escalation.

## Attack path
1. Register student account on moodle.schooled.htb
2. [[stored-xss]] in MoodleNet profile to steal manager cookie (CVE-2020-25627)
3. Auth as Manuel Phillips, exploit privilege escalation (CVE-2021-14321) to manager role
4. Use "Log in as" feature to impersonate Lianne Carter (manager)
5. Modify manager role permissions to enable plugin installation
6. Upload malicious Moodle plugin for [[webshell]]
7. Extract database credentials, crack admin hash (!QAZ2wsx)
8. SSH as jamie, abuse sudo rights on pkg command
9. Create malicious FreeBSD package that adds sudoers entry
10. Host malicious package, modify /etc/hosts to point to attacker
11. Install malicious package for root access

## Techniques used
- [[stored-xss]] — MoodleNet profile XSS (CVE-2020-25627) for cookie theft
- [[moodle-privilege-escalation]] — Course enrollment privilege escalation (CVE-2021-14321)
- [[plugin-upload]] — Moodle plugin installation for RCE
- [[hash-cracking]] — Bcrypt hash cracking with hashcat
- [[package-manager-abuse]] — FreeBSD pkg command abuse for privilege escalation
- [[hosts-file-modification]] — Edit /etc/hosts to redirect package updates

## Tools used
[[nmap]], [[feroxbuster]], [[wfuzz]], [[hashcat]], [[mysql]], [[pkg]], fpm

## Services / ports
- [[ssh]] (22) — OpenSSH 7.9 (FreeBSD)
- [[http]] (80) — Apache 2.4.46 with PHP 7.4.15, Moodle instance
- mysqlx (33060) — MySQL X Protocol

## Lessons / notes
- Moodle version 3.9 with multiple XSS vulnerabilities
- CVE-2021-14321 allows privilege escalation from teacher to manager
- Manager role can enable plugin installation through permissions modification
- FreeBSD uses different web root: /usr/local/www/apache24/data
- pkg manager commands can be abused with custom repositories
- /etc/hosts writable by wheel group for DNS redirection
- +POST_INSTALL script in package executes during installation
