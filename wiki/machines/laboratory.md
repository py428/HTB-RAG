---
type: machine
title: Laboratory
platform: htb
os: linux
difficulty: easy
tags: [web, gitlab, docker, linux, privesc]
solved: 2026-07-09
sources: [[htb-laboratory]]
related: []
---
# Laboratory
> Laboratory is an easy Linux box featuring a GitLab instance. The attack path exploits a GitLab arbitrary file read vulnerability to access secrets, achieves RCE via Rails deserialization, accesses a private repository with SSH credentials, and escalates privileges by hijacking the PATH in a SUID binary.

## Attack path
1. [[gitlab-arbitrary-file-read]] — Read arbitrary files via GitLab issue move vulnerability
2. [[rails-deserialization]] — Achieve RCE via Rails cookie deserialization with leaked secret_key_base
3. [[git-admin-privileges]] — Reset admin password or elevate own user to access private project
4. [[ssh-auth]] — Use SSH key from private GitLab repository
5. [[suid-path-hijacking]] — Exploit SUID binary calling chmod without full path

## Techniques used
- [[gitlab-arbitrary-file-read]] — Exploit CVE-2020-10977 to read arbitrary files via issue markdown image reference and move
- [[rails-deserialization]] — Craft malicious Rails cookie using leaked secret_key_base for code execution
- [[git-admin-privileges]] — Modify GitLab user objects via Rails console to gain admin access
- [[suid-path-hijacking]] — Place malicious chmod binary in PATH before SUID binary execution

## Tools used
- [[nmap]]
- [[wfuzz]]
- [[gobuster]]
- [[docker]]
- [[openssl]]
- [[curl]]
- python3
- [[netcat]]
- [[scp]]
- [[gcc]]

## Services / ports
- [[ssh]] (22)
- [[http]] (80)
- [[https]] (443)

## Lessons / notes
- GitLab 12.x vulnerable to arbitrary file read via issue markdown image reference and project move
- Rails secret_key_base from secrets.yml allows crafting valid signed cookies for deserialization
- Rails console running as root provides full control over GitLab user database
- SUID binaries calling system() without full path are vulnerable to PATH hijacking
- ProcMon for Linux can monitor process syscalls to capture sensitive data like passwords