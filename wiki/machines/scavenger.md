---
type: machine
title: Scavenger
platform: htb
os: linux
difficulty: hard
tags: [web, privesc, kernel, ad]
solved: 2026-07-09
sources: [[htb-scavenger]]
related: []
---
# Scavenger
> Scavenger is a hard Linux box featuring extensive web enumeration, SQL injection in a whois server, DNS zone transfers, and a webshell leading to user access. The root path involves reverse engineering a modified rootkit kernel module or exploiting CVE-2019-10149 in the Exim mail server.

## Attack path
1. [[sqli]] in whois service to enumerate domains
2. [[dns-zone-transfer]] to discover subdomains
3. Find webshell on hacked site (sec03.rentahacker.htb)
4. Enumerate via webshell, find FTP credentials in email
5. Access FTP as ib01c01, get user.txt and rootkit kernel module
6. [[kernel-module-abuse]]: Reverse engineer root.ko to find trigger password "g3tPr1v"
7. Write "g3tPr1v" to /dev/ttyR0 for root access (or [[cve-2019-10149]] via Exim)

## Techniques used
- [[sqli]] — SQL injection in whois server to dump domain list
- [[dns-zone-transfer]] — AXFR to enumerate subdomains across domains
- [[webshell]] — Abandoned webshell on defaced WordPress site
- [[kernel-module-abuse]] — Reverse engineer rootkit to find root trigger password
- [[cve-2019-10149]] — Exim RCE for alternative root path

## Tools used
[[nmap]], [[whois]], [[dig]], [[wfuzz]], [[hydra]], [[netcat]], [[curl]], [[openssl]], [[john]], [[hashcat]], [[wireshark]], python3

## Services / ports
- [[ftp]] (21) — vsftpd 3.0.3, requires credentials
- [[ssh]] (22) — OpenSSH 7.4p1, authentication requires valid credentials
- [[smtp]] (25) — Exim 4.89, vulnerable to CVE-2019-10149
- [[whois]] (43) — Custom whois server with MariaDB backend, SQL injection
- [[dns]] (53) — BIND 9.10.3, zone transfer enabled
- [[http]] (80) — Apache 2.4.25, multiple virtual hosts

## Lessons / notes
- Firewall rules (iptables) prevent reverse shells but allow established connections
- The whois SQL injection uses MariaDB syntax with `like` and `limit 1`
- DNS zone transfers reveal the full domain structure efficiently
- The webshell parameter fuzzing with wfuzz finds the `hidden` parameter
- Stateful shell using mkfifo technique for better interaction
- Kernel module rootkit analysis with IDA Pro reveals modified magic string
- Exim exploit requires special syntax with ${run{...}} for command execution
