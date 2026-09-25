---
type: source
title: "HTB Love writeup"
raw: raw/htb-love.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[love]]
---

# Source: HTB Love writeup
> Detailed writeup covering SSRF exploitation, credential leakage, authenticated file upload RCE in Voting System, and AlwaysInstallElevated MSI abuse for SYSTEM shell.

## Key facts extracted
- SSL certificate reveals staging.love.htb subdomain
- SSRF on staging.love.htb/beta.php accesses localhost-only services
- localhost:5000 returns voting system credentials: admin/@LoveIsInTheAir!!!!
- Voting System 1.0 vulnerable to authenticated file upload RCE
- Profile picture upload bypass allows PHP webshell upload
- AlwaysInstallElevated set to 1 in HKLM and HKCU enables MSI abuse
- MySQL filtered from external access, SSH key unavailable, WinRM present

## Filed into
[[love]], [[ssrf]], [[subdomain-enumeration]], [[credential-leak]], [[file-upload-rce]], [[searchsploit]], [[alwaysinstallelevated]], [[msi-abuse]], [[password-reuse]]
