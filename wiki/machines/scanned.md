---
type: machine
title: Scanned
platform: htb
os: linux
difficulty: insane
tags: [linux, web, sandbox-escape, ptrace, privesc, chroot]
solved: 2026-07-09
sources: [[htb-scanned]]
related: []
---
# Scanned

> Insane-difficulty malware analysis sandbox escape featuring chroot jail breakout via ptrace file descriptor hijack, Django database extraction, SetUID binary abuse with LD_PRELOAD library hijacking, and capabilities exploitation for root access.

## Attack path

1. [[chroot-escape]] — Exploit ptrace implementation to access file descriptor outside jail
2. [[database-extraction]] — Read Django SQLite database through log file exfiltration
3. [[password-cracking]] — Crack Django admin hash with hashcat
4. [[suid-exploitation]] — Hijack SetUID su binary execution with malicious library
5. [[capabilities-abuse]] — Use sandbox capabilities for privilege escalation

## Techniques used

- [[chroot-escape]] — Access `/proc/1/fd/3` file descriptor to read files outside chroot jail
- [[ptrace]] — Exploit open file descriptor in parent process for jailbreak
- [[database-extraction]] — Exfiltrate SQLite database contents 8 bytes at a time via syscalls
- [[password-cracking]] — Crack Django MD5 salted hash with hashcat and rockyou
- [[ld-preload]] — Hijack library loading in SetUID binary execution
- [[capabilities-abuse]] — Use Linux capabilities in sandbox binary for root access

## Tools used

- [[nmap]] — Port scanning
- [[curl]] — Web interaction
- [[feroxbuster]] — Directory brute force
- gcc — Exploit development and compilation
- [[python]] — Database reconstruction and web interaction
- [[hashcat]] — Django password hash cracking
- [[sqlite3]] — Database analysis
- ssh — Remote access with cracked credentials

## Services / ports

- [[ssh]] — 22/tcp
- [[http]] — 80/tcp — Django malware analysis web application
- Custom sandbox service — Python application analyzing uploaded binaries

## Lessons / notes

- Sandbox uses chroot jails with ptrace-based syscall logging
- File descriptor leakage allows reading files outside jail via `/proc/1/fd/3`
- Django database at `/var/www/malscanner/malscanner.db` contains user hashes
- Clarence password: `onedayyoufeellikecrying` (Django admin and SSH)
- SetUID su binary can be hijacked by placing malicious library in jail
- Sandbox capabilities include CAP_SETUID, CAP_SETGID, CAP_SYS_CHROOT, CAP_SYS_ADMIN
- Custom SetUID copy of su created as `/tmp/0xdf` with 4777 permissions
- PTRACE_TRACEME and file descriptor exploitation core to jailbreak
