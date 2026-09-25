---
type: machine
title: Awkward
platform: htb
os: linux
difficulty: medium
tags: [ad, web, linux, privesc]
solved: 2026-07-09
sources: [[htb-awkward]]
related: []
---
# Awkward
> Awkward is a Linux box featuring a Node.js HR application with multiple vulnerabilities leading to initial access via password recovery from a backup file, then privilege escalation through email-based command injection using symlinked files.

## Attack path
1. [[cookie-bypass]] to access dashboard without authentication
2. [[api-bypass]] to enumerate users and dump password hashes
3. [[hash-cracking]] to recover credentials for christopher.jones
4. [[ssrf]] via store status API to enumerate internal services
5. [[awk-injection]] to read arbitrary files on the filesystem
6. [[backup-analysis]] to extract SSH credentials from xpad notes
7. [[symlink-abuse]] to write arbitrary content to leave requests
8. [[command-injection]] via mail command to get root shell

## Techniques used
- [[cookie-bypass]] — Authentication check only verifies cookie is "guest", allowing bypass to dashboard
- [[api-bypass]] — Staff details API returns without authentication, leaking password hashes
- [[ssrf]] — Store status API accepts URL parameter to fetch internal resources
- [[awk-injection]] — Awk command injection in all-leave API using filename manipulation to read arbitrary files
- [[hash-cracking]] — SHA-256 hashes cracked with hashcat and rockyou.txt
- [[backup-analysis]] — Backup archive extracted and xpad notes file contains SSH password
- [[symlink-abuse]] — Cart files symlinked to leave_requests.csv to inject content
- [[command-injection]] — Mail command injection using --exec parameter to execute arbitrary commands

## Tools used
[[nmap]], [[wfuzz]], [[curl]], [[hashcat]], [[ssh]], [[netcat]]

## Services / ports
[[http]] (80), [[ssh]] (22)

## Lessons / notes
- Weak authentication checks can often be bypassed by manipulating client-side values
- Awk injection techniques allow reading arbitrary files when certain characters are blocked
- Backup archives may contain sensitive credentials in unexpected places
- Symlink attacks can bypass file write restrictions
- Email processing pipelines are often vulnerable to command injection
