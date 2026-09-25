---
type: machine
title: LinkVortex
platform: htb
os: linux
difficulty: easy
tags: [linux, web, privesc, git, ghost, cve]
solved: 2026-07-09
sources: [[htb-linkvortex]]
related: []
---

# LinkVortex
> Linux box running Ghost CMS with exposed Git repository on dev subdomain leading to credential leak, then CVE-2023-40028 arbitrary file read via symlink upload, and sudo symlink cleanup script abuse.

## Attack path
1. [[subdomain-enumeration]] — discover dev.linkvortex.htb
2. [[git-exposure]] — dump exposed Git repo from dev site
3. [[credential-leak]] — find password in modified test file
4. [[cve-2023-40028]] — exploit Ghost arbitrary file read via symlink upload to read SSH config
5. [[sudo-abuse]] — abuse symlink cleanup script with three methods (double symlinks, TOCTOU, command injection)

## Techniques used
- [[subdomain-enumeration]] — ffuf vhost fuzzing reveals dev subdomain
- [[git-exposure]] — exposed .git directory on dev site with git-dumper
- [[credential-leak]] — password change in authentication.test.js Git diff
- [[cve-2023-40028]] — Ghost <5.59.1 arbitrary file read via symlink upload in zip archives
- [[symlink-race]] — double symlink bypass protected_symlinks for root file read
- [[toctou]] — race condition between symlink check and content display
- [[command-injection]] — abusing $CHECK_CONTENT variable execution in sudo script
- [[sudo-abuse]] — multiple methods to exploit clean_symlink.sh script

## Tools used
[[nmap]], ffuf, git-dumper, [[curl]], git, ssh, netexec

## Services / ports
- [[ssh]] (22)
- [[http]] (80) — Apache proxying Ghost CMS

## Lessons / notes
- Ghost CMS version 5.58 vulnerable to CVE-2023-40028 — allows authenticated file read via symlink uploads
- Git repository exposure can reveal credentials in commit diffs even if not in current files
- Sudo scripts with symlink handling can have multiple bypass methods (double symlinks, TOCTOU, variable injection)
- Protected symlinks (fs.protected_symlinks=1) prevents some but not all symlink attacks
- Apache ServerTokens Prod and ServerSignature Off hide version info in headers and error pages
