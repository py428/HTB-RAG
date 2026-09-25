---
type: machine
title: FriendZone
platform: htb
os: linux
difficulty: easy
tags: [linux, web, lfi, smb, dns, cronjob, privesc]
solved: 2026-07-09
sources: [[htb-friendzone]]
related: []
---
# FriendZone
> FriendZone is an easy Linux box involving DNS zone enumeration, SMB credential discovery, LFI exploitation for initial access, and Python library hijacking for privilege escalation via a writable os.py module.

## Attack path
1. [[dns-zone-transfer]] to discover subdomains
2. [[smb-enum]] to find admin credentials
3. [[lfi]] in dashboard.php with SMB upload to get webshell
4. Database credentials lead to friend user access
5. Writable [[python-library-hijack]] in /usr/lib/python2.7/os.py
6. Inject reverse shell into os.py for root access via cron

## Techniques used
- [[dns-zone-transfer]] — AXFR query to discover subdomains
- [[smb-enum]] — Enumerating SMB shares and finding credentials
- [[lfi]] — Local file inclusion with PHP filters
- [[webshell-upload]] — Uploading PHP webshell via SMB
- [[python-library-hijack]] — Hijacking Python os.py module for privilege escalation
- [[cronjob-abuse]] — Exploiting root cron job running hijacked Python script

## Tools used
[[nmap]], [[smbmap]], [[smbclient]], [[gobuster]], [[dig]], [[curl]], [[ffuf]], python, [[nc]]

## Services / ports
- 21/tcp — [[ftp]]
- 22/tcp — [[ssh]]
- 53/tcp — [[dns]]
- 80/tcp — [[http]]
- 139/tcp — [[smb]]
- 443/tcp — [[https]]
- 445/tcp — [[smb]]

## Lessons / notes
- DNS zone transfer revealed multiple subdomains and attack surface
- SMB shares contained useful credentials and were writable for webshell upload
- LFI with php://filter allowed reading PHP source code
- Python module hijacking is a powerful privesc technique when modules are writable
- The cron job ran /opt/server_admin/reporter.py every 2 minutes as root
