---
type: machine
title: Armageddon
platform: htb
os: linux
difficulty: easy
tags: [ad, linux, web, privesc]
solved: 2026-07-09
sources: [[htb-armageddon]]
related: []
---
# Armageddon

> Easy Linux box featuring a Drupal 7.56 installation vulnerable to Drupalgeddon2, allowing initial webshell access. The attack path progresses through database credential extraction, hash cracking, and password reuse to gain user access, then abuses snap package installation permissions for privilege escalation to root.

## Attack path
1. [[nmap]] scan reveals Drupal 7.56 on [[http]] (port 80)
2. Exploit [[drupalgeddon2]] for RCE and upload webshell
3. Extract database credentials from Drupal config
4. Dump user table, crack [[hashcat|hash]] to get password
5. Reuse password for [[ssh]] access as brucetherealadmin
6. Abuse sudo permissions to install malicious snap package for root

## Techniques used
- [[drupalgeddon2]] — Drupal 7.x RCE via SQL injection in user password reset form
- [[hash-cracking]] — Drupal hash extraction and cracking with hashcat mode 7900
- [[password-reuse]] — Database password reused for SSH access
- [[snap-package-abuse]] — Craft malicious snap package with install hook for root

## Tools used
- [[nmap]], [[curl]], [[hashcat]], [[docker]] (for snap building), [[snapcraft]]

## Services / ports
- 22/tcp [[ssh]] — OpenSSH 7.4
- 80/tcp [[http]] — Apache httpd 2.4.6 with Drupal 7.56

## Lessons / notes
- Drupalgeddon2 exploits CVE-2018-7600 in Drupal 7.x
- Drupal 7 hashes use specific format recognizable by hashcat mode 7900
- Snap packages can execute arbitrary scripts during installation via hooks
- Malicious snap packages require `--dangerous` and `--devmode` flags when unsigned
- Targeting snap install hooks allows writing SSH keys or creating users with elevated privileges
