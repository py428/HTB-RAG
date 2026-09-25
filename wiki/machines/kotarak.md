---
type: machine
title: Kotarak
platform: htb
os: linux
difficulty: hard
tags: [linux, web, ad, privesc, container]
solved: 2026-07-09
sources: [[htb-kotarak]]
related: []
---
# Kotarak
> Complex Ubuntu 16.04 box involving SSRF to enumerate localhost services, Tomcat WAR deployment, NTDS hash cracking, and a wget vulnerability for container root access.

## Attack path
1. [[ssrf]] via web browser service → discover Tomcat backup on localhost
2. [[tomcat-war-upload]] with leaked credentials → shell as tomcat
3. [[dcsync]] from exfiltrated ntds.dit → crack atanas password
4. [[wget-cve-2016-4971]] with FTP redirect to write cron job → root in container
5. Alternative: [[disk-group-abuse]] to exfiltrate entire filesystem

## Techniques used
- [[ssrf]] — Web browser service to enumerate localhost ports and access internal services
- [[tomcat-war-upload]] — WAR file deployment via Tomcat manager with leaked credentials
- [[dcsync]] — NTDS.dit extraction and password dumping using secretsdump from exfiltrated pentest files
- [[wget-cve-2016-4971]] — Wget <1.18 arbitrary file write via HTTP to FTP redirect
- [[disk-group-abuse]] — LVM disk device reading via disk group membership

## Tools used
[[nmap]], [[feroxbuster]], [[curl]], msfvenom, [[secretsdump]], [[hashcat]], [[pspy]], pyftpdlib, dd, gzip

## Services / ports
- 22/tcp — [[ssh]] (OpenSSH 7.2)
- 8009/tcp — Tomcat AJP
- 8080/tcp — [[http]] (Apache Tomcat 8.5.5)
- 60000/tcp — [[http]] (Apache 2.4.18)

## Lessons / notes
- SSRF through web browser service can enumerate localhost ports effectively
- Old pentest data (ntds.dit + SYSTEM hive) can be gold mines for password cracking
- CVE-2016-4971 exploits wget's handling of redirects to FTP servers for arbitrary file writes
- LXC containers keep filesystems in /var/lib/lxc/<container>/rootfs/
- Disk group access allows reading raw block devices for filesystem exfiltration
- Authbind allows non-root users to bind to low-numbered ports
