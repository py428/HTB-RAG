---
type: machine
title: EarlyAccess
platform: htb
os: linux
difficulty: hard
tags: [linux, web, docker, xss, sqli, plugin-development, capabilities]
solved: 2026-07-09
sources: [[htb-earlyaccess]]
related: []
---
# EarlyAccess
> Game company themed box with multiple websites and Docker containers. Chain: XSS to steal admin cookie, SQL injection to game database, custom key validation algorithm, command injection via hash function debug mode, Docker container breakout, and capabilities abuse for root.

## Attack path
1. [[xss]] — Store XSS in username to steal admin session cookie
2. [[second-order-sqli]] — Inject SQL via username into scoreboard to dump database hashes
3. [[key-validation]] — Reverse engineer game key validation algorithm and brute force magic number
4. [[command-injection]] — Abuse debug parameter to execute system commands via hash function
5. [[docker-container-breakout]] — Crash game server container to execute script from host as root
6. [[capabilities-abuse]] — Use arp binary with all capabilities to read root flag and SSH key

## Techniques used
- [[xss]] — Stored XSS in profile username executed when admin views messages
- [[second-order-sqli]] — Username from main site injected into game site scoreboard SQL queries
- [[key-validation]] — Analyzed Python validation script, generated keys for all 60 possible magic numbers
- [[command-injection]] — PHP allowed calling arbitrary functions as hash functions when debug=1
- [[docker-container-breakout]] — Crashed game server with negative rounds, triggered script execution on restart
- [[capabilities-abuse]] — arp binary had =ep (all capabilities) allowing file read

## Tools used
[[nmap]], [[wfuzz]], [[sqlmap]], python3, [[curl]], nc, docker, getcap

## Services / ports
[[ssh]] (22), [[http]] (80), [[https]] (443), minecraft (25565)

## Lessons / notes
- Forum post hinted at SQL injection in username field for scoreboard crashes
- Game key validation used checksum algorithm and magic number that changed every 30 minutes
- PHP hash_pw function treated string variable name as callable function
- Docker entrypoint.d directory mapped from host, scripts run as root on container start
- Linux capabilities can provide full root access without SUID (arp had =ep)
- MySQL credentials leaked via Docker API check_db endpoint for internal database
