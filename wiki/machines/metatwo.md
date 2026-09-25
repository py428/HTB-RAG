---
type: machine
title: MetaTwo
platform: htb
os: linux
difficulty: easy
tags: [linux, web, wordpress, database, privesc]
solved: 2026-07-09
sources: [[htb-metatwo]]
related: []
---
# MetaTwo
> Linux easy box starting with WordPress BookingPress SQL injection, XXE for file reading, SMTP credentials from FTP, and Passpie password manager for root.

## Attack path
1. Exploit [[sqli]] in BookingPress plugin for WordPress admin access
2. Use [[xxe]] via WordPress media manager to read wp-config.php
3. FTP credentials from WordPress config for [[ftp-access]]
4. SMTP credentials from FTP scripts for SSH access as jnelson
5. Crack Passpie [[pgp-key]] for root password

## Techniques used
- [[sqli]] — Unauthenticated SQL injection in BookingPress plugin
- [[wordpress-exploitation]] — WordPress authentication and media upload
- [[xxe]] — XML external entity injection via WordPress media upload (CVE-2021-29447)
- [[ftp-access]] — FTP access using credentials from wp-config.php
- [[smtp-credentials]] — SMTP credentials enumeration for SSH access
- [[password-cracking]] — PGP key cracking with John the Ripper
- [[password-manager]] — Passpie password manager exploitation

## Tools used
- [[nmap]]
- [[wfuzz]]
- sqlmap
- [[hashcat]]
- [[curl]]
- [[ftp]]
- sshpass
- [[john]]

## Services / ports
- [[ssh]] (22)
- [[http]] (80)
- [[ftp]] (21)

## Lessons / notes
- BookingPress < 1.0.11 vulnerable to unauthenticated SQL injection
- WordPress 5.6.2 media manager vulnerable to XXE (CVE-2021-29447)
- wp-config.php often contains FTP credentials for file operations
- SMTP credentials can be reused for SSH access
- Passpie uses PGP encryption that can be cracked with John
