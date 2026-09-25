---
type: source
title: "HTB Valentine writeup"
raw: raw/htb-valentine.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[valentine]]
---
# Source: HTB Valentine writeup
> Classic writeup for HTB Valentine covering Heartbleed exploitation, SSH key decryption, tmux session hijacking, and DirtyCow kernel exploit as alternative privesc.

## Key facts extracted
- OpenSSL 1.0.1f vulnerable to Heartbleed (CVE-2014-0160)
- Memory leak reveals base64 encoded password for encrypted SSH key
- Root tmux session running with accessible socket file
- Ubuntu 12.04 kernel vulnerable to DirtyCow exploit
- Multiple privilege escalation paths available

## Filed into
[[valentine]], [[heartbleed]], [[ssh-key-reuse]], [[tmux-session-hijack]], [[dirty-cow]]
