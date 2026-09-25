---
type: source
title: "HTB SecNotes writeup"
raw: raw/htb-secnotes.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[secnotes]]
---
# Source: HTB SecNotes writeup
> Complete writeup for HTB SecNotes machine covering both intended XSRF exploitation and unintended second-order SQL injection paths, SMB webshell upload techniques, and WSL-based credential extraction for privilege escalation.

## Key facts extracted
- SecNotes application has password change form accessible via GET without current password
- Admin bot checks contact form messages and visits any URLs found
- SMB share new-site maps to IIS web directory on port 8808 allowing webshell upload
- WSL Ubuntu installation accessible with bash.exe contains administrator credentials in bash history
- Unintended second-order SQLi path exists via registration with malicious username

## Filed into
[[secnotes]], [[xsrf]], [[second-order-sqli]], [[smb-webshell-upload]], [[wsl-credential-extraction]]
