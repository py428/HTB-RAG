---
type: machine
title: Keeper
platform: htb
os: linux
difficulty: easy
tags: [linux, web, password-recovery, privesc]
solved: 2026-07-09
sources: [[htb-keeper]]
related: []
---
# Keeper
> Ubuntu 22.04 box featuring a Request Tracker helpdesk with default credentials, leading to KeePass password recovery from a memory dump exploiting CVE-2022-32784.

## Attack path
1. [[default-credentials]] on Request Tracker → user creds for lnorgaard
2. SSH access → memory dump with KeePass database
3. [[keepass-password-dump]] (CVE-2022-32784) to recover master password
4. Extract SSH private key from KeePass → convert PuTTY format → root access

## Techniques used
- [[default-credentials]] — Request Ticket (RT) system default root:password credentials
- [[keepass-password-dump]] — CVE-2022-32784 password recovery from memory dump using DotNet or Python exploit
- [[putty-key-conversion]] — PuTTY private key to OpenSSH format conversion using puttygen

## Tools used
[[nmap]], [[ffuf]], [[ssh]], scp, kpcli, keepass-password-dumper, puttygen

## Services / ports
- 22/tcp — [[ssh]] (OpenSSH 8.9)
- 80/tcp — [[http]] (nginx 1.18)

## Lessons / notes
- RT default credentials are often unchanged in production environments
- KeePass 2.x before 2.54 has a critical vulnerability where master password can be recovered from memory dumps
- The first character of the password cannot be recovered, but context clues often reveal it
- PuTTY key format requires conversion to OpenSSH for Linux SSH clients
- Memory dumps can include KeePass databases even after the application is closed
