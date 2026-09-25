---
type: source
title: "HTB Irked writeup"
raw: raw/htb-irked.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[irked]]
---
# Source: HTB Irked writeup
> Concise writeup for HTB Irked covering UnrealIRCd backdoor exploitation, steganography credential extraction, and setuid binary abuse for privilege escalation.

## Key facts extracted
- UnrealIRCd 3.2.8.1 backdoor responds to "AB;" + command
- Steganography password: UPupDOWNdownLRlrBAbaSSss
- Extracted SSH password: Kab6h+m+bbp2J:HG
- /usr/bin/viewuser setuid binary calls /tmp/listusers with system()
- Binary executes with setuid(0) after calling who command
- Multiple IRC ports running same vulnerable service

## Filed into
[[irked]], [[unrealircd-backdoor]], [[steganography]], [[setuid-binary-abuse]]