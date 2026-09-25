---
type: machine
title: MonitorsThree
platform: htb
os: linux
difficulty: medium
tags: [cacti, sqli, web, docker, privesc, backup]
solved: 2026-07-09
sources: [[htb-monitorsthree]]
related: []
---
# MonitorsThree

> Linux host with Cacti and Duplicati backup solution, exploited via SQLi in password reset, file upload vulnerability, and backup tool abuse for root access.

## Attack path

1. [[subdomain-enumeration]] — find `cacti.monitorsthree.htb` virtual host
2. [[sqli-blind]] — exploit boolean-based blind SQL injection in password reset form
3. [[hash-cracking]] — dump and crack admin password hash from database
4. [[file-upload]] — exploit CVE-2024-25642 (Cacti package import) for PHP code upload
5. [[credential-cracking]] — extract marcus password from Cacti database
6. [[backup-tool-abuse]] — abuse Duplicati backup tool to backup `/root` and restore flag to accessible location

## Techniques used

- [[sqli-blind]] — Boolean-based blind SQL injection in forgot password form with `OR NOT` payload
- [[hash-cracking]] — CrackStation for MD5 hashes, hashcat for bcrypt hashes
- [[file-upload]] — CVE-2024-25642: Authenticated arbitrary file write via package import feature
- [[backup-tool-abuse]] — Duplicati backup/restore functionality to read host filesystem

## Tools used

- [[nmap]], [[ffuf]], [[sqlmap]], [[hashcat]], [[ssh]], [[sqlite3]]

## Services / ports

- 22/tcp — [[ssh]] — OpenSSH 8.9
- 80/tcp — [[http]] — nginx 1.18.0
- 8084/tcp — filtered (Duplicati web interface, localhost only)
- 8200/tcp — [[http]] — Duplicati web interface (localhost only)

## Lessons / notes

- Boolean-based blind SQLi much faster than time-based for this injection point
- CVE-2024-25642 requires XML package with signed payload using RSA key pair
- Duplicati runs in Docker container with host filesystem mounted at `/source`
- Backup tool can be used to read any host file by creating backup of target directory
