---
type: source
title: "HTB AdmirerToo writeup"
raw: raw/htb-admirertoo.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[admirertoo]]
---
# Source: HTB AdmirerToo writeup
> Comprehensive guide to exploiting AdmirerToo, a hard Linux HackTheBox machine demonstrating advanced exploit chaining including SSRF, command injection, file write vulnerabilities, and Fail2Ban RCE.

## Key facts extracted
- Adminer 4.7.8 vulnerable to SSRF (CVE-2021-21311) via Elasticsearch driver
- OpenTSDB on port 4242 vulnerable to command injection (CVE-2020-35476) 
- Database credentials for jennifer: bQ3u7^AxzcB7qAsxE3
- OpenCats 0.9.5.2 vulnerable to PHP object injection (CVE-2021-25294)
- Fail2Ban vulnerable to RCE (CVE-2021-32749) via whois command injection
- Final exploit required writing whois.conf to redirect whois queries to attacker-controlled server

## Filed into
[[admirertoo]], [[ssrf]], [[opentsdb-command-injection]], [[file-write-vulnerability]], [[fail2ban-rce]]
