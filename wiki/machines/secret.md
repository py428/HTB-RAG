---
type: machine
title: Secret
platform: htb
os: linux
difficulty: easy
tags: [web, privesc, linux, jwt, git]
solved: 2026-07-09
sources: [[htb-secret]]
related: []
---
# Secret
> Secret is an easy Linux box featuring a Node.js application with downloadable source code. The attack involves analyzing Git history to find JWT signing secrets, forging admin tokens to exploit command injection, and exploiting a SUID binary with file descriptor abuse to read root files. Two exploitation paths exist for root: using file descriptors from a running SUID process, or crashing the process to extract files from core dumps.

## Attack path
1. [[nmap]] enumeration reveals SSH and HTTP on ports 80 and 3000
2. Download and analyze source code from `/download/files.zip`
3. Analyze Git history with `git show` to find previous JWT secret in commit history
4. Register account on application and obtain initial JWT token
5. Forge admin JWT token using extracted secret and PyJWT library
6. Exploit [[command-injection]] in `/api/logs` endpoint as admin user - inject commands via file parameter
7. Obtain reverse shell as user dasith via command injection
8. Discover SUID binary `/opt/count` that analyzes files and directories
9. Exploit file descriptors - read root files via `/proc/[pid]/fd` while count process has files open
10. Alternative: crash SUID binary to generate core dump and extract files with [[strings]]

## Techniques used
- [[git-history-analysis]] — Extract JWT signing secret from previous Git commits
- [[jwt-forging]] — Create admin JWT tokens using extracted signing secret
- [[command-injection]] — Git log command with unsanitized file parameter allows command injection
- [[suid-file-descriptor-abuse]] — Exploit SUID binary file descriptors to read protected files
- [[core-dump-analysis]] — Crash SUID binary and extract file contents from core dumps

## Tools used
[[nmap]], [[feroxbuster]], [[git]], [[jwt]], [[hashcat]], [[strings]], [[nc]]

## Services / ports
22/tcp — [[ssh]], 80/tcp — HTTP (NGINX), 3000/tcp — HTTP (Node.js/Express)

## Lessons / notes
- Git history often contains sensitive credentials that have been "removed" from current code
- JWT tokens without expiration can be forged indefinitely if signing secret is known
- SUID binaries that open files can be exploited via file descriptors even with setuid drops
- Core dumps from SUID binaries may contain file contents even if normal reading is prevented
- Command injection in git log execution allows for blind command execution with output
