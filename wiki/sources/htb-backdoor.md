---
type: source
title: "HTB Backdoor writeup"
raw: raw/htb-backdoor.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[backdoor]]
---
# Source: HTB Backdoor writeup
> Detailed exploitation guide for a WordPress site with plugin vulnerabilities leading to gdbserver exploitation and screen session hijacking.

## Key facts extracted
- WordPress 5.8.1 with vulnerable Ebook Download plugin
- Directory traversal vulnerability allows reading arbitrary files
- gdbserver process discovered listening on port 1337
- gdbserver can be exploited to upload and execute payloads
- Screen configured for multiuser access with root session running
- Multiple exploitation methods available (manual gdb and Metasploit)

## Filed into
[[backdoor]], [[directory-traversal]], [[process-enumeration]], [[gdbserver-exploit]], [[screen-session-hijacking]]
