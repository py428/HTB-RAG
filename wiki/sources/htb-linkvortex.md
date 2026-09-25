---
type: source
title: "HTB LinkVortex writeup"
raw: raw/htb-linkvortex.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[linkvortex]]
---

# Source: HTB LinkVortex writeup
> Comprehensive writeup covering LinkVortex exploitation from subdomain enumeration through Git exposure, CVE-2023-40028 Ghost arbitrary file read, and multiple sudo privesc methods.

## Key facts extracted
- Exposed Git repository on dev.linkvortex.htb with modified authentication test file containing password
- Ghost CMS version 5.58 vulnerable to CVE-2023-40028 — arbitrary file read via symlink upload
- Three methods for sudo abuse: double symlinks, TOCTOU race condition, and $CHECK_CONTENT command injection
- SMTP credentials for bob user found in Ghost config.production.json
- Apache configured with ServerTokens Prod and ServerSignature Off to hide version

## Filed into
[[linkvortex]], [[git-exposure]], [[credential-leak]], [[cve-2023-40028]], [[symlink-race]], [[toctou]], [[sudo-abuse]], [[command-injection]], [[subdomain-enumeration]]
