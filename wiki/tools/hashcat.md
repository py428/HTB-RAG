---
type: tool
title: Hashcat
category: crypto
tags: [password-cracking, gpu]
updated: 2026-07-09
---

# Hashcat

## What it does
Fast password-hash cracker (GPU/CPU) supporting hundreds of modes via `-m`. Pairs with wordlists like `rockyou.txt` and rule files.

## Common usage
```
hashcat -m 18200 asrep.hash /usr/share/wordlists/rockyou.txt   # Kerberos AS-REP
hashcat -m 1000 ntlm.hash rockyou.txt                          # NTLM
hashcat --show -m 18200 asrep.hash                             # reveal cracked result
```

## Used on
- [[absolute]] — `-m 18200` cracked `d.klay`'s AS-REP to `Darkmoonsky248girl` (see [[as-rep-roasting]]).
- [[active]] — `-m 13100` cracked the Administrator TGS (see [[kerberoasting]]).
- [[forest]] — `-m 18200` cracked `svc-alfresco`'s AS-REP to `s3rvice`.
