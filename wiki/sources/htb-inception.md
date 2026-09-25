---
type: source
title: "HTB Inception writeup"
raw: raw/htb-inception.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[inception]]
---
# Source: HTB Inception writeup
> Detailed writeup for HTB Inception machine covering LFI exploitation, WebDAV webshell upload, forward shell techniques, sudo abuse, and network pivoting via FTP/TFTP for cron hijacking.

## Key facts extracted
- Target: Inception container-based system with web server and SSH
- Primary attack vector: dompdf LFI → WebDAV webshell → Forward shell → Cron hijacking
- Initial foothold: dompdf 0.6.0 LFI vulnerability for configuration file disclosure
- Privilege escalation: Full sudo access in container environment
- Root access: Cron job hijacking via TFTP and FTP write access
- Network pivoting: Container to host access via FTP and TFTP services
- The box demonstrates early container hacking concepts and network pivoting techniques

## Filed into
[[inception]], [[lfi]], [[webdav]], [[forward-shell]], [[sudo]], [[cron-hijack]]
