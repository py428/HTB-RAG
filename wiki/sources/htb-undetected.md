---
type: source
title: "HTB Undetected writeup"
raw: raw/htb-undetected.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[undetected]]
---
# Source: HTB Undetected writeup
> Detailed analysis of persistence mechanisms, backdoored binaries, and tracing previous attacker activities.

## Key facts extracted
- phpunit 5.6.2 vulnerable to CVE-2017-9841
- Kernel exploit backdoor adds "1" users to /etc/passwd and /etc/shadow
- steven1 backdoor hash: $6$zS7ykHfFMg3aYht4$1IUrhZanRuDZhf1oIdnoOvXoolKmlwbkegBXk.VtGg78eL7WBM6OrNtGbZxKBtPu8Ufm9hM0R/BLdACoQ0T9n/
- Apache mod_reader.so downloads backdoored sshd from sharefiles.xyz
- Backdoored sshd contains XOR-encoded hardcoded password
- Multiple persistence: SSH keys, cron jobs, backdoored users, replaced binaries

## Filed into
[[undetected]], [[cve-2017-9841]], [[binary-reverse-engineering]], [[hash-cracking]], [[backdoor-password]]
