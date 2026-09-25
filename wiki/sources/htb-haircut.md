---
type: source
title: "HTB Haircut writeup"
raw: raw/htb-haircut.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[haircut]]
---
# Source: HTB Haircut writeup
> PHP curl parameter injection exploitation for webshell upload and SUID screen binary privilege escalation via ld.so.preload hijacking.

## Key facts extracted
- PHP application uses `shell_exec("curl " . $userurl)` with minimal character filtering
- Blocked characters: `%`, `!`, `|`, `;`, `python`, `nc`, `perl`, `bash`, `&`, `#`, `{`, `}`, `[`, `]`
- Parameter injection possible with curl options like `-o` for file output
- SUID screen binary 4.5.0 vulnerable to arbitrary file write via log file creation
- `/etc/ld.so.preload` hijack enables root code execution through shared library preloading

## Filed into
[[haircut]], [[parameter-injection]], [[webshell]], [[suid]]
