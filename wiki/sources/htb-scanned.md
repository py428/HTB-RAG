---
type: source
title: "HTB Scanned writeup"
raw: raw/htb-scanned.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[scanned]]
---
# Source: HTB Scanned writeup

> Advanced sandbox escape walkthrough covering ptrace exploitation, chroot jailbreak, database exfiltration via syscalls, Django hash cracking, and SetUID binary hijacking with LD_PRELOAD for root access.

## Key facts extracted

- Django malware sandbox with chroot jails and ptrace syscall logging
- File descriptor leakage in ptrace parent processes enables jailbreak
- Django SQLite database at `/var/www/malscanner/malscanner.db`
- Clarence password hash: `md5$kL2cLcK2yhbp3za4w3752m$9886e17b091eb5ccdc39e436128141cf`
- Cracked password: `onedayyoufeellikecrying`
- Sandbox capabilities: CAP_SETUID, CAP_SETGID, CAP_SYS_CHROOT, CAP_SYS_ADMIN
- SetUID su binary at `/usr/bin/su` hijacked via malicious library in jail
- Custom SetUID binary created at `/tmp/0xdf` for root shell

## Filed into

[[scanned]], [[chroot-escape]], [[ptrace]], [[database-extraction]], [[password-cracking]], [[ld-preload]], [[capabilities-abuse]]
