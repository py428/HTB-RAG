---
type: machine
title: Undetected
platform: htb
os: linux
difficulty: medium
tags: [web, php, reverse-engineering, privesc, ad]
solved: 2026-07-09
sources: [[htb-undetected]]
related: []
---
# Undetected
> Medium Linux box tracing a previous attacker's path through CVE-2017-9841 RCE, analysis of backdoored binaries, persistence mechanisms, and malicious Apache modules.

## Attack path
1. [[cve-2017-9841]] RCE via phpunit eval-stdin.php to get www-data shell
2. [[binary-reverse-engineering]] of kernel exploit backdoor to find backdoored users
3. [[hash-cracking]] steven1 hash from /etc/shadow backdoor
4. [[binary-reverse-engineering]] of malicious mod_reader Apache module
5. [[binary-reverse-engineering]] of backdoored sshd to extract hardcoded password

## Techniques used
- [[cve-2017-9841]] — Remote code execution in PHPUnit via eval-stdin.php endpoint
- [[directory-traversal]] — Feroxbuster finds /vendor directory with composer packages
- [[binary-reverse-engineering]] — Analysis of kernel exploit binary showing backdoor persistence mechanisms
- [[hash-cracking]] — SHA512 hash from backdoored /etc/shadow entry cracked to "ihatehackers"
- [[binary-reverse-engineering]] — Ghidra analysis of malicious Apache module and SSH binary
- [[backdoor-password]] — Hardcoded password extracted from backdoored sshd binary

## Tools used
- [[nmap]]
- [[feroxbuster]]
- [[wfuzz]]
- [[curl]]
- hashcat
- Ghidra
- Python

## Services / ports
- [[ssh]] — TCP 22 (OpenSSH 8.2, with backdoored sshd)
- [[http]] — TCP 80 (Apache 2.4.41 with malicious mod_reader.so)

## Lessons / notes
- CVE-2017-9841 affects PHPUnit < 5.6.5 when debug/eval-stdin.php is exposed
- The box simulates investigating a previous attacker's persistence mechanisms
- Kernel exploit backdoor showed how attackers modify /etc/passwd and /etc/shadow
- Apache modules can be backdoored to execute arbitrary commands on startup
- SSH binaries can be modified to include hardcoded backdoor passwords
- Multiple persistence mechanisms: SSH keys, cron jobs, backdoored users, replaced binaries
