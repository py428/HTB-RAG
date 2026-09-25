---
type: machine
title: Admirer
platform: htb
os: linux
difficulty: easy
tags: [web, linux, privesc, sudo, python]
solved: 2026-07-09
sources: [[htb-admirer]]
related: []
---
# Admirer
> A Linux box featuring web enumeration leading to FTP credential exposure, database interface manipulation for file access, and Python library hijacking via sudo configuration for privilege escalation.

## Attack path
1. Web enumeration to find [[web-enumeration]] and discover FTP credentials in admin-dir
2. [[ftp-credential-exposure]] to access source code with database credentials  
3. [[adminer-file-read]] vulnerability to read local files and obtain SSH credentials
4. SSH access as waldo using database credentials
5. [[sudo-pythonpath-hijack]] via PYTHONPATH environment variable abuse for root access

## Techniques used
- [[web-enumeration]] — robots.txt disclosure and directory brute forcing
- [[ftp-credential-exposure]] — credentials stored in backup files accessible via FTP
- [[adminer-file-read]] — LOAD DATA LOCAL INFILE for local file read through database interface
- [[sudo-pythonpath-hijack]] — SETENV tag allowing PYTHONPATH manipulation to hijack Python libraries

## Tools used
[[nmap]] [[gobuster]] [[wget]] [[mysql]] ssh

## Services / ports
- [[ftp]] 21 — vsftpd 3.0.3
- [[ssh]] 22 — OpenSSH 7.4p1 Debian 10+deb9u7
- [[http]] 80 — Apache httpd 2.4.25

## Lessons / notes
- The Adminer database interface can be abused for local file access even without database credentials by connecting to a local MySQL server
- When sudo has the SETENV tag, environment variables like PYTHONPATH can be manipulated to hijack library imports
- The debug Flask PIN generation requires multiple system-specific pieces of information including MAC address, machine-id, and cgroup
