---
type: source
title: "HTB CarpeDiem writeup"
raw: raw/htb-carpediem.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[carpediem]]
---
# Source: HTB CarpeDiem writeup
> 0xdf's detailed writeup for HTB CarpeDiem covering multi-container exploitation, voicemail credential harvesting, TLS decryption, and Docker escape via CVE-2022-0492.

## Key facts extracted
- Multi-container Docker environment with 6 containers
- Portal subdomain on motorcycle booking site
- Trudesk ticket system contains voicemail credentials for new employee
- TLS_RSA_WITH_AES_256_CBC_SHA256 cipher allows decryption with private key
- Backdrop CMS vulnerable to malicious plugin upload
- Root cron executes backdrop.sh which includes modified index.php
- CVE-2022-0492 cgroups exploit for container escape

## Filed into
[[carpediem]], [[parameter-tampering]], [[file-upload]], [[network-pivoting]], [[voip-credential-harvesting]], [[tls-decryption]], [[cms-exploitation]], [[plugin-upload]], [[cron-job-abuse]], [[docker-escape]], [[ssh]], [[web]], [[rce]], [[privesc]], [[container-escape]]
