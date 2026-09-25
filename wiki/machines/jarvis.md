---
type: machine
title: Jarvis
platform: htb
os: linux
difficulty: medium
tags: [linux, web, sqli, python, privesc]
solved: 2026-07-09
sources: [[htb-jarvis]]
related: []
---
# Jarvis
> Medium difficulty Linux machine featuring SQL injection behind a WAF, PHPMyAdmin LFI to RCE, Python script command injection, and systemctl abuse for privilege escalation.

## Attack path
1. [[sqli]] with WAF bypass on room.php cod parameter
2. Extract DBadmin credentials from MySQL user table
3. [[phpmyadmin-lfi]] (CVE-2018-12613) for webshell
4. [[command-injection]] in simpler.py ping function via `$()` syntax
5. [[systemctl-abuse]] to create malicious service for root

## Techniques used
- [[sqli]] — UNION injection with 7 columns, IronWAF 2.0.3 bypassed with low-level/risk sqlmap options
- [[waf-bypass]] — IronWAF bans IPs for 90 seconds after 5+ suspicious requests to room.php?cod
- [[phpmyadmin-lfi]] — CVE-2018-12613: `%3f` bypasses security check but not include, leading to session file LFI
- [[command-injection]] — Python script blocks `& ; - \` || |` but misses `$()` for command substitution
- [[systemctl-abuse]] — SUID systemctl for pepper user can link and start malicious .service files

## Tools used
[[nmap]], gobuster, [[sqlmap]], [[curl]], [[nc]]

## Services / ports
[[ssh]] (22), [[http]] (80/64999)

## Lessons / notes
- IronWAF creates iptables rule redirecting port 80 to 64999 for banned IPs (90-second ban)
- PHPMyAdmin 4.8.0 vulnerable to LFI via inconsistent `%3f` handling
- Command injection blacklist incomplete without `$()` - always test all bash substitution syntaxes
- systemctl SUID binary allows creating/linking arbitrary .service files
- Clean script runs via cron every 15 minutes to clear Apache access logs
- Python WAF script parses Apache logs in real-time to detect SQLi patterns
