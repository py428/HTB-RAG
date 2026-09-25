---
type: machine
title: Writeup
platform: htb
os: linux
difficulty: easy
tags: [linux, web, privesc]
solved: 2026-07-09
sources: [[htb-writeup]]
related: []
---
# Writeup
> Linux box running CMS Made Simple with blind SQL injection vulnerability for credential extraction. Initial shell via SSH with cracked credentials, then privilege escalation through PATH manipulation in staff group and Perl module hijacking.
## Attack path
1. Exploit blind [[sqli]] in CMS Made Simple to extract and crack user credentials
2. SSH with cracked credentials to gain shell as jkr user
3. Abuse staff group membership to hijack run-parts command in SSH login process
4. Alternative privesc via Perl module manipulation in /usr/local/lib
## Techniques used
- [[blind-sqli]] — Time-based SQL injection with sleep() for credential extraction
- [[staff-group-abuse]] — PATH hijacking via /usr/local/bin writable by staff group
- [[perl-module-hijacking]] — Inserting malicious code in Perl modules loaded by cleanup.pl
- [[password-cracking]] — MD5 hash cracking using rockyou.txt wordlist
## Tools used
- [[nmap]], CMS Made Simple exploit script, [[ssh]], [[netcat]], pspy
## Services / ports
- [[ssh]] (22), [[http]] (80)
## Lessons / notes
- CMS Made Simple versions prior to 2.2.10 vulnerable to unauthenticated blind SQLi
- staff group in Debian can write to /usr/local/bin and /usr/local/sbin
- SSH login executes run-parts with /usr/local/bin and /usr/local/sbin in PATH
- Perl modules in @INC path can be modified to inject malicious code
- cleanup.pl cron job runs Perl scripts that load modified modules
