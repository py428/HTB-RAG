---
type: source
title: "HTB Soccer writeup"
raw: raw/htb-soccer.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[soccer]]
---
# Source: HTB Soccer writeup
> Detailed writeup covering Tiny File Manager exploitation, SQL injection over websockets, and doas plugin abuse for privilege escalation.

## Key facts extracted
- Tiny File Manager default credentials: admin/admin@123 and user/12345
- PHP webshell upload via file manager
- Second virtual host: soc-player.soccer.htb on port 9091
- Blind SQL injection over websocket connection
- Database contains user credentials in plaintext
- doas configuration allows dstat execution as root
- Malicious dstat plugin leads to root shell

## Filed into
[[soccer]], [[tiny-file-manager]], [[webshell]], [[sqli-websocket]], [[doas-plugin]]
