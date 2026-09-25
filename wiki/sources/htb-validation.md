---
type: source
title: "HTB Validation writeup"
raw: raw/htb-validation.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[validation]]
---
# Source: HTB Validation writeup
> UHC qualifier box with second-order SQL injection in registration form, allowing database enumeration and FILE privilege abuse for webshell, with password reuse for root.

## Key facts extracted
- Second-order SQL injection in country parameter of registration form
- MySQL user `uhc` has FILE privilege for writing files
- Database credentials: `uhc:uhc-9qual-global-pw`
- Cookie format: MD5 hash of username
- Frontend runs in Docker container
- Root password reuse from database credentials

## Filed into
[[validation]], [[second-order-sqli]], [[sqli-file-write]], [[password-reuse]]
