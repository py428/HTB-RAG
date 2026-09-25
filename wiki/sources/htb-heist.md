---
type: source
title: "HTB Heist writeup"
raw: raw/htb-heist.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[heist]]
---
# Source: HTB Heist writeup
> Detailed walkthrough of Heist HackTheBox machine covering Cisco password cracking, RPC enumeration, WinRM access, and Firefox process memory dumping to obtain administrator credentials.
## Key facts extracted
- Cisco Type 5 passwords are salted MD5 hashes cracked with john using rockyou.txt
- Cisco Type 7 passwords use XOR encryption with static key "tfd;kfoA,.iyewrkldJKD"
- RPC null session with credentials allows SID brute forcing to enumerate users
- Firefox process memory contains POST request data with login credentials
- Web administrator password (4dD!5}x/re8]FBuZ) matches local administrator password
## Filed into
[[heist]], [[password-cracking]], [[rpc-null-session]], [[process-memory-dump]], [[password-reuse]]
