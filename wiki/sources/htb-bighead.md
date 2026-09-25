---
type: source
title: "HTB BigHead writeup"
raw: raw/htb-bighead.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[bighead]]
---
# Source: HTB BigHead writeup
> Complex exploitation chain involving custom buffer overflow, SSH tunneling, PHP file inclusion, and KeePass database cracking with keyfile extraction.
## Key facts extracted
- BigheadWebSvr 1.0 vulnerable to buffer overflow requiring custom exploit development
- Registry contains nginx service credentials: H73BpUY2Uq9U-Yugyt5FYUbY0-U87t87
- Bitvise SSH server on port 2020 accessible only via tunneling
- TestLink application vulnerable to PHP local file inclusion via linkto.php
- KeePass database stored as ADS on root.txt with keyfile at admin.png  
- Database password "darkness" unlocks root flag in KeePass entry
## Filed into
[[bighead]], [[buffer-overflow]], [[ssh-tunneling]], [[php-include]], [[ads-extraction]], [[keepass-cracking]]
