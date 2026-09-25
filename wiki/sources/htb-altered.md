---
type: source
title: "HTB Altered writeup"
raw: raw/htb-altered.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[altered]]
---
# Source: HTB Altered writeup
> Detailed exploitation of Laravel application including rate limit bypass for brute force, type juggling to bypass integrity checks, SQL injection for file read/write, and Dirty Pipe kernel exploit for privilege escalation.

## Key facts extracted
- Password reset PIN brute force protected by rate limiting vulnerable to X-Forwarded-For bypass
- Secret validation uses weak comparison allowing type juggling bypass
- SQL injection in profile endpoint allows file operations
- Dirty Pipe exploit used to overwrite SUID binary (pkexec) with shellcode
- Custom PAM-Wordle module adds authentication challenge to su

## Filed into
[[altered]], [[rate-limit-bypass]], [[type-juggling-bypass]], [[sqli]], [[file-write-sqli]], [[dirty-pipe]], [[pam-wordle]]
