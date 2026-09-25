---
type: machine
title: Alert
platform: htb
os: linux
difficulty: easy
tags: [web, xss, file-read, ldap]
solved: 2026-07-09
sources: [[htb-alert]]
related: []
---
# Alert
> Web application box featuring blind XSS in markdown viewer, directory traversal to read Apache config, and cronjob hijacking via writable PHP import.

## Attack path
1. [[xss-blind]] in markdown upload → Phish admin with malicious link
2. Use XSS to read internal pages via [[directory-traversal]] → Apache config
3. Read .htpasswd file → Crack hash with [[hashcat]]
4. Use cracked credentials for SSH access → User shell
5. Find writable PHP import in monitoring script → [[cronjob-hijack]] → Root shell

## Techniques used
- [[xss-blind]] — HTML/script injection in uploaded markdown files, triggered by admin viewing
- [[directory-traversal]] — File read vulnerability in messages.php using "../" sequences
- [[htpasswd-crack]] — Apache .htpasswd file contains crackable MD5 hashes
- [[cronjob-hijack]] — Writable PHP configuration file included in cronned PHP script

## Tools used
- [[nmap]], ffuf, [[feroxbuster]], [[hashcat]], [[ssh]], [[netcat]]

## Services / ports
- [[ssh]] (22), [[http]] (80)

## Lessons / notes
- Blind XSS can be used to read internal pages and exfiltrate data via fetch()
- Directory traversal often works on file read endpoints even when include fails
- Apache .htpasswd files can be cracked with hashcat using mode 1600
- Cron jobs running PHP scripts may include writable configuration files
- Group permissions on files are as important as user permissions
- SSH tunnels can expose locally running services for remote access
