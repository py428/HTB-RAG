---
type: machine
title: Vessel
platform: htb
os: linux
difficulty: hard
tags: [git, express, mysqljs, owa, pyinstaller, crio, kernel-exploit]
solved: 2026-07-09
sources: [[htb-vessel]]
related: []
---
# Vessel
> Complex chain involving Git repo analysis, Express/mysqljs type confusion SQLi bypass, Open Web Analytics exploitation with CVE-2022-24637, mass assignment for RCE, PyInstaller reverse engineering for password recovery, and CVE-2022-0811 for CRI-O kernel manipulation.

## Attack path
1. [[git-exposure]] — Download repo from `/dev/.git` and analyze for vulnerability
2. [[mysqljs-type-confusion]] — Bypass parameterized query using nested object for SQL injection
3. [[cve-2022-24637]] — Cache file disclosure to get admin temp_passkey for password reset
4. [[mass-assignment]] — Abuse OWA configuration to write PHP webshell via log poisoning
5. [[pyinstaller-reverse]] — Extract and decompile PyInstaller executable to recover password
6. [[cve-2022-0811]] — Exploit CRI-O pinns binary to modify kernel parameters for root

## Techniques used
- [[git-exposure]] — Repo exposed at `/dev/.git` with vulnerability history
- [[mysqljs-type-confusion]] — Express passing nested objects to mysqljs bypasses parameterization
- [[cve-2022-24637]] — OWA cache files with broken PHP tags expose serialized data including temp_passkey
- [[mass-assignment]] — OWA allows arbitrary config parameters including log file location
- [[pyinstaller-reverse]] — Extract Python bytecode from Windows exe and decompile
- [[cve-2022-0811]] — CRI-O pinns allows unsafe kernel parameter modification via `+` separator
- [[webshell]] — Log poisoning with PHP code in `labelname` CDATA

## Tools used
- [[nmap]]
- [[ffuf]]
- [[git-dumper]]
- [[netcat]]
- [[pyinstxtractor]]
- [[uncompyle6]]
- [[uv]] (Python tool management)
- [[pdfcrack]]

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 8.2p1 Ubuntu
- 80/tcp — [[http]] — Apache httpd 2.4.41 (Ubuntu) (main site) / nginx (subdomains)

## Lessons / notes
- Code committed to fix SQLi but still vulnerable via type confusion (objects vs strings)
- OWA cache files broken due to single quotes in PHP string construction
- Password generator used weak seeding with `QTime.currentTime().msec()` (1000 possibilities)
- PyInstaller extraction requires matching Python version for best results
- CRI-O pinns binary custom-compiled for box, triggers on `-f -d` arguments
- Kernel parameter `core_pattern` with `|` prefix executes command on process crash
