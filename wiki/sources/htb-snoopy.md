---
type: source
title: "HTB Snoopy writeup"
raw: raw/htb-snoopy.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[snoopy]]
---
# Source: HTB Snoopy writeup
> Comprehensive writeup covering file read vulnerability, DNS TSIG hijacking, SSH honeypot usage, and exploitation of two CVEs (git apply and ClamAV XXE) for full system compromise.

## Key facts extracted
- File read via directory traversal (....// bypass) in download.php
- DNS zone transfer and TSIG key leak from Bind configuration
- Mattermost slash command abuse for SSH server provisioning
- SSH honeypot (cowrie) to capture credentials
- CVE-2023-23946: git apply arbitrary file write via symlinks
- CVE-2023-20052: XXE in ClamAV DMG processing for file disclosure

## Filed into
[[snoopy]], [[path-traversal]], [[dns-tsig]], [[ssh-honeypot]], [[cve-2023-23946]], [[cve-2023-20052]]
