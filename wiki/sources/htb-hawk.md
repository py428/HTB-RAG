---
type: source
title: "HTB Hawk writeup"
raw: raw/htb-hawk.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[hawk]]
---
# Source: HTB Hawk writeup
> Drupal exploitation through encrypted FTP credential discovery, PHP filter RCE, H2 database abuse for file reads and command execution.

## Key facts extracted
- Anonymous FTP access to `.drupal.txt.enc` file encrypted with AES-256-CBC
- Password "friends" decrypts file revealing Drupal admin credentials
- Drupal 7.58 with PHP filter module enabled for content execution
- Database credentials `drupal4hawk` work for daniel system user
- H2 database runs as root with backup tool allowing arbitrary file read via symlinks
- H2 SQL alias creation enables Java Runtime.exec() for OS command execution
- H2 console on port 8082 only accessible from localhost without tunnel

## Filed into
[[hawk]], [[openssl]], [[drupal]], [[password-reuse]], [[h2-database]]
