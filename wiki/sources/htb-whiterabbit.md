---
type: source
title: "HTB WhiteRabbit writeup"
raw: raw/htb-whiterabbit.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[whiterabbit]]
---
# Source: HTB WhiteRabbit writeup
> Advanced exploitation guide covering websocket manipulation, SQL injection with signature bypass, restic backup forensics, Docker container escape, and PRNG prediction for password generation on an insane difficulty Linux box.

## Key facts extracted
- Uptime Kuma v1.23.13 vulnerable to websocket response manipulation for login bypass
- n8n webhook vulnerable to SQL injection with HMAC-SHA256 signature requirement
- Database contains restic backup commands with embedded passwords
- Container SSH keys stored in restic backup archive protected by 7z encryption
- Custom password generator uses timestamp as PRNG seed allowing prediction
- Neo user has full sudo privileges for root access
- Secret key for webhook signatures: 3CWVGMndgMvdVAzOjqBiTicmv7gxc6IS

## Filed into
[[whiterabbit]], [[websocket-manipulation]], [[sql-injection]], [[signature-bypass]], [[backup-forensics]], [[command-injection]], [[container-escape]], [[prng-prediction]], [[sudo-abuse]], [[uptime-kuma]], [[n8n]], [[wikijs]], [[restic]]
