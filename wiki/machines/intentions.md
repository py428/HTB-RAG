---
type: machine
title: Intentions
platform: htb
os: linux
difficulty: hard
tags: [web, sqli, php, imagemagick, git, privesc]
solved: 2026-07-09
sources: [[htb-intentions]]
related: []
---
# Intentions
> Intentions is a Linux hard box featuring second-order SQL injection, client-side password hashing, ImageMagick arbitrary object instantiation for webshell upload, Git credential harvesting, and creative file reading via a copyright scanning tool.

## Attack path
1. Identify [[second-order-sqli]] in gallery feed via user profile genres
2. Use UNION-based injection to leak admin credentials from database
3. Find v2 API endpoint that hashes passwords client-side instead of server-side
4. Authenticate as admin using bcrypt hash directly instead of password
5. Exploit ImageMagick arbitrary object instantiation via MSL payload to write webshell
6. Find hardcoded credentials in Git history for user pivot
7. Abuse DMCA scanner binary with CAP_DAC_READ_SEARCH capability to read root SSH key

## Techniques used
- [[second-order-sqli]] — SQL injection stored in profile, executed on feed view
- [[client-side-hashing]] — V2 API uses client-side bcrypt hashing
- [[imagemagick-arbitrary-object]] — MSL payload exploitation for file write
- [[git-credential-harvesting]] — Hardcoded credentials in Git commit history
- [[capability-abuse]] — CAP_DAC_READ_SEARCH allows reading any file
- [[hash-brute-force]] — MD5 brute-force for byte-by-byte file reading

## Tools used
- [[nmap]], [[feroxbuster]], [[sqlmap]], [[python]], [[imagemagick]], [[git]], [[hashcat]]

## Services / ports
- 22/tcp — [[ssh]]
- 80/tcp — [[http]] (nginx/Laravel PHP)

## Lessons / notes
- Second-order SQL injection requires separate testing of storage and retrieval
- Laravel applications may have renamed session cookies matching app name
- ImageMagick MSL payloads allow arbitrary file writes via vid: scheme
- Git history often contains credentials that should have been removed
- Linux capabilities can provide file read access equivalent to root
- Hash brute-forcing allows reading files byte-by-byte when partial hash comparison is available
