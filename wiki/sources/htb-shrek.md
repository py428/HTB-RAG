---
type: source
title: "HTB Shrek writeup"
raw: raw/htb-shrek.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[shrek]]
---
# Source: HTB Shrek writeup
> Comprehensive walkthrough of steganography in MP3 files, FTP credential extraction, ECC decryption, and wildcard chown exploitation for root.
## Key facts extracted
- FTP credentials hidden in MP3 spectrogram: donkey:d0nk3y1337!
- Encrypted SSH key password decrypted via ECC: shr3k1sb3st!
- Cron job runs `chown nobody:nobody *` in /usr/src every 5 minutes
- Wildcard exploit with --reference flag changes /etc/passwd ownership
- thoughts.txt file has immutable flag preventing chown modification
## Filed into
[[shrek]], [[steganography-audio]], [[ecc-decryption]], [[wildcard-exploit]], [[ftp-access]], [[passwd-modification]]
