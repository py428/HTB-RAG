---
type: source
title: "HTB Charon writeup"
raw: raw/htb-charon.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[charon]]
---
# Source: HTB Charon writeup

> Comprehensive guide for HTB Charon box covering SQL injection bypasses, file upload techniques, RSA cryptography, and SUID binary exploitation.

## Key facts extracted
- Forgot password form vulnerable to UNION-based SQL injection with WAF filtering
- Filter blocks "UNION", "INFORMATION_SCHEMA", and "union" (case-sensitive)
- Bypass achieved using "UNiON" case variation and proper column matching
- File upload validates both extension and magic bytes
- Hidden base64-encoded form field "dGVzdGZpbGUx" controls filename
- RSA public key only 256-bit allowing factorization via factordb.com
- SUID supershell binary validates input against character blacklist
- Binary compares first 7 chars to "/bin/ls" and executes via system()

## Filed into
[[charon]], [[sql-injection]], [[file-upload-bypass]], [[rsa-factorization]], [[command-injection]], [[suid-exploitation]]
