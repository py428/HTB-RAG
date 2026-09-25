---
type: machine
title: Aragog
platform: htb
os: linux
difficulty: medium
tags: [linux, web, xxe, wordpress, ssh]
solved: 2026-07-09
sources: [[htb-aragog]]
related: []
---
# Aragog
> Medium Linux box featuring XXE (XML External Entity) vulnerability exploitation for initial access, followed by WordPress modification to capture credentials for privilege escalation.

## Attack path
1. Anonymous [[ftp]] access to discover XML file structure
2. Directory enumeration reveals hosts.php endpoint
3. [[xxe]] vulnerability in XML processing to read arbitrary files
4. Extract SSH private key via XXE for user access
5. Modify WordPress login script to capture administrative credentials
6. Use captured credentials for root access

## Techniques used
- [[xxe]] — Injecting malicious DTD to read files via XML external entity processing
- [[ssh-key-reuse]] — Using private key extracted from filesystem for authentication
- [[web-shell-upload]] — Modifying PHP script to capture submitted credentials

## Tools used
- [[nmap]], [[ftp]], [[smbclient]], [[gobuster]], [[curl]], [[ssh]], [[hashcat]]

## Services / ports
- [[ftp]] (21), [[ssh]] (22), [[http]] (80)

## Lessons / notes
- XXE can be exploited even when XML input is processed and returned to user
- WordPress wp-login.php modification allows credential capture without database access
- Scheduled tasks (restore.sh) can reveal credential usage patterns
- pspy useful for monitoring processes without root access
- SSH keys in .ssh directory readable via XXE even when not web-accessible
