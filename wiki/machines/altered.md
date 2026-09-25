---
type: machine
title: Altered
platform: htb
os: linux
difficulty: hard
tags: [web, laravel, type-juggling, sqli, kernel-exploit]
solved: 2026-07-09
sources: [[htb-altered]]
related: []
---
# Altered
> Laravel application with password reset functionality vulnerable to rate limit bypass, type juggling for secret validation bypass, SQL injection for file read/write, and Dirty Pipe kernel exploit for privilege escalation.

## Attack path
1. [[rate-limit-bypass]] using X-Forwarded-For header → [[pin-brute-force]]
2. Use type juggling to bypass secret check → [[type-juggling-bypass]]
3. [[sqli]] in profile endpoint → [[file-write-sqli]] for webshell
4. [[dirty-pipe]] exploit to overwrite SUID binary → Root shell

## Techniques used
- [[rate-limit-bypass]] — X-Forwarded-For header bypasses IP-based rate limiting
- [[type-juggling-bypass]] — Send "true" as secret value to bypass weak comparison
- [[sqli]] — SQL injection in profile API after secret bypass
- [[file-write-sqli]] — Use UNION SELECT with INTO OUTFILE to write PHP files
- [[dirty-pipe]] — CVE-2022-0847 kernel vulnerability to overwrite SUID binary
- [[pam-wordle]] — Custom PAM module requiring Wordle game for authentication

## Tools used
- [[nmap]], wfuzz, [[feroxbuster]], [[curl]], [[gcc]], msfvenom

## Services / ports
- [[ssh]] (22), [[http]] (80)

## Lessons / notes
- Rate limiting based on X-Forwarded-For can be bypassed with different IPs
- Laravel applications using weak comparisons (== vs ===) vulnerable to type juggling
- SQL injection can be used for both file read (load_file) and write (into outfile)
- Dirty Pipe exploit allows overwriting files without write permissions
- Kernel exploits require proper version matching and may have unique mitigations
