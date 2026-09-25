---
type: machine
title: Yummy
platform: htb
os: linux
difficulty: hard
tags: [web, linux, privesc, ad]
solved: 2026-07-09
sources: [[htb-yummy]]
related: []
---
# Yummy
> Yummy is a restaurant reservation system with a Flask backend. The attack path involves directory traversal to read files, weak RSA factorization to forge JWT tokens for admin access, SQL injection to write webshells, cron job abuse for initial shell, Mercurial repository enumeration for credentials, hook abuse for horizontal privsec, and rsync SetUID binary abuse for root.

## Attack path
1. [[directory-traversal]] in calendar invite file creation to read source code and crontab
2. [[rsa-weak-factorization]] of JWT signing key to forge [[jwt-forgery]] admin tokens
3. [[sqli]] in admin dashboard order parameter with [[mysql-file-write]]
4. [[cronjob-abuse]] via mysql user executing scripts from writable directory
5. [[mercurial-credentials]] in repo history for [[mercurial-hook-abuse]] horizontal privesc
6. [[rsync-privesc]] with SetUID bash copy for root

## Techniques used
- [[directory-traversal]] — Path traversal in export file creation allows reading arbitrary files from the host
- [[rsa-weak-factorization]] — Weak RSA prime (2^19-2^20 range) allows factoring JWT signing key
- [[jwt-forgery]] — Forged JWT with administrator role using recovered private key
- [[sqli]] — Blind SQL injection with stacked queries in ORDER BY clause
- [[mysql-file-write]] — SELECT INTO OUTFILE with FILE privilege and secure_file_priv=""
- [[cronjob-abuse]] — Writing to /data/scripts/fixer-v* executed by mysql cron user
- [[mercurial-credentials]] — Database credentials found in hg diff of committed config changes
- [[mercurial-hook-abuse]] — Malicious pre-pull hook executed as dev user via sudo hg pull
- [[rsync-privesc]] — SetUID bash copy via rsync --chown保留 to root

## Tools used
[[nmap]], [[feroxbuster]], [[curl]], [[exiftool]], [[ffuf]], python, sagemath, [[jwt_tool]], [[sqlmap]], [[netcat]], [[ssh]], hg, [[rsync]]

## Services / ports
[[ssh]] (22), [[http]] (80), [[mysql]] (3306)

## Lessons / notes
- Weak RSA key generation with small q (2^19-2^20) made JWT signing recoverable
- MySQL CLIENT.MULTI_STATEMENTS flag enabled stacked queries
- AppArmor disabled allowed MySQL file writes outside /var/lib/mysql
- Mercurial hooks execute as the user running the pull operation
- rsync --chown preserves SetUID bits unlike chown command