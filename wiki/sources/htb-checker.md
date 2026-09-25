---
type: source
title: "HTB Checker writeup"
raw: raw/htb-checker.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[checker]]
---
# Source: HTB Checker writeup
> Complex multi-vector exploitation involving Teampass SQL injection, BookStack SSRF with PHP filter chains, Google Authenticator 2FA bypass, and shared memory race condition for privilege escalation.

## Key facts extracted
- Teampass CVE-2023-1545 leaks bcrypt hashes via /authorize SQL injection
- BookStack CVE-2023-6199 allows SSRF via html parameter in save-draft
- PHP filter chains enable blind file reads through error oracle
- SSH 2FA bypass by reading .google_authenticator seed from backup
- check_leak binary uses writable shared memory (0o1666) for hash checking
- Three privilege escalation paths via PERL5OPT, http_proxy, LD_PRELOAD

## Filed into
[[checker]], [[sqli]], [[php-filter-chains]], [[2fa-bypass]], [[shared-memory-race]], [[ld-preload]]
