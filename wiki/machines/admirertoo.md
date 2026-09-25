---
type: machine
title: AdmirerToo
platform: htb
os: linux
difficulty: hard
tags: [web, linux, privesc, ssrf, rce, chaining]
solved: 2026-07-09
sources: [[htb-admirertoo]]
related: []
---
# AdmirerToo
> A complex Linux box requiring exploit chaining: SSRF in Adminer to discover OpenTSDB, command injection for initial shell, file write vulnerability combined with Fail2ban RCE for root.

## Attack path
1. [[web-enumeration]] reveals Adminer interface with SSRF vulnerability (CVE-2021-21311)
2. [[ssrf]] in Adminer to discover and exploit OpenTSDB on localhost
3. [[opentsdb-command-injection]] (CVE-2020-35476) for initial shell as opentsdb user
4. [[database-credential-exposure]] from local config files to pivot to jennifer user
5. [[file-write-vulnerability]] in OpenCats (CVE-2021-25294) to write malicious whois.conf
6. [[fail2ban-rce]] (CVE-2021-32749) via whois command injection for root access

## Techniques used
- [[ssrf]] — CVE-2021-21311 in Adminer 4.7.8 using Elasticsearch driver and redirect
- [[opentsdb-command-injection]] — CVE-2020-35476 in yrange parameter with system() execution
- [[database-credential-exposure]] — credentials stored in PHP config files
- [[file-write-vulnerability]] — CVE-2021-25294 PHP object injection in OpenCats using phpggc
- [[fail2ban-rce]] — CVE-2021-32749 whois command injection via mail action payload

## Tools used
[[nmap]] [[feroxbuster]] [[wfuzz]] [[hydra]] phpggc ncat flite

## Services / ports
- [[ssh]] 22 — OpenSSH 7.9p1 Debian 10+deb10u2
- [[http]] 80 — Apache httpd 2.4.38 hosting multiple virtual hosts
- OpenTSDB 4242 — Time series database with command injection vulnerability
- MySQL 3306 — localhost only

## Lessons / notes
- Multi-stage exploit chaining requires careful persistence and privilege escalation planning
- SSRF can be used to enumerate and exploit services bound to localhost
- File write vulnerabilities can be leveraged to configure system-level exploits (whois.conf for fail2ban)
- The fail2ban exploit requires controlling the whois response, achieved by writing custom whois configuration
