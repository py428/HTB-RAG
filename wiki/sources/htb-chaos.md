---
type: source
title: "HTB Chaos writeup"
raw: raw/htb-chaos.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[chaos]]
---
# Source: HTB Chaos writeup

> Detailed walkthrough for HTB Chaos box covering web exploitation, AES decryption, LaTeX RCE, and Firefox credential extraction.

## Key facts extracted
- WordPress site with protected post reveals human/human credentials
- Webmail access via Roundcube on webmail.chaos.htb subdomain
- Encrypted message in drafts folder with AES-256-CBC encrypted attachment
- LaTeX PDF generation service with \write18 enabled at hidden URL
- ayush user in rbash restricted shell with limited PATH
- Firefox profile contains saved password for Webmin/root access
- Root password works for both system login and Webmin interface

## Filed into
[[chaos]], [[webmail-exploitation]], [[aes-decryption]], [[latex-rce]], [[rbash-escape]], [[password-reuse]]
