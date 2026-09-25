---
type: machine
title: Hawk
platform: htb
os: linux
difficulty: medium
tags: [linux, web, drupal, database, password-reuse]
solved: 2026-07-09
sources: [[htb-hawk]]
related: []
---
# Hawk
> Drupal 7 CMS with encrypted FTP file containing credentials, PHP execution via PHP filter module, H2 database abuse for file read and RCE, and password reuse for privilege escalation.

## Attack path
1. [[openssl]] brute force on encrypted FTP file for Drupal admin credentials
2. [[drupal]] PHP filter module enabling PHP execution in content
3. [[password-reuse]] from Drupal database config for daniel user SSH access
4. [[h2-database]] backup function for arbitrary file read as root
5. [[h2-database]] alias creation for command execution as root

## Techniques used
- [[openssl]] — Brute-forcing AES-256-CBC encrypted file with password dictionary
- [[drupal]] — PHP filter module allows embedding PHP code in content for RCE
- [[password-reuse]] — Drupal database credentials reused for system user access
- [[h2-database]] — Backup tool creates zip of .db files, following symlinks for file read
- [[h2-database]] — SQL alias creation for OS command execution via Java Runtime.exec()

## Tools used
- [[nmap]]
- [[ftp]]
- [[openssl]]
- bash scripts
- [[hydra]]
- droopscan
- [[python]]
- [[impacket]]
- [[dbeaver]]

## Services / ports
- [[ftp]] (21)
- [[ssh]] (22)
- [[http]] (80)
- TCP 5435 — H2 PostgreSQL server
- TCP 8082 — H2 database console
- TCP 9092 — H2 TCP server

## Lessons / notes
- AES-256-CBC encrypted files can be brute-forced with openssl and password dictionaries
- Drupal PHP filter module provides easy RCE when enabled
- Database configuration files often contain credentials reused elsewhere
- H2 database tools run as database user (often root) and can read files via backup functionality
- H2 database allows creating SQL aliases for arbitrary Java code execution
- H2 listens on multiple ports for different protocols (PG, TCP, HTTP)
- SSH tunneling needed to access local-only H2 console remotely
