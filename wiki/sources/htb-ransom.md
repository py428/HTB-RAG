---
type: source
title: "HTB Ransom writeup"
raw: raw/htb-ransom.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[ransom]]
---
# Source: HTB Ransom writeup
> UHC qualifier box walkthrough covering Laravel authentication bypass via PHP type juggling, ZipCrypto archive decryption using known plaintext attack with bkcrack, and credential discovery in source code for privilege escalation.

## Key facts extracted
- Laravel login vulnerable to type juggling via JSON body with boolean true instead of string password
- GET request accepts JSON body when Content-Type header set to application/json
- Downloaded homedirectory.zip encrypted with ZipCrypto (not AES-256)
- bkcrack tool performs known plaintext attack using 12+ bytes of known file content
- .bash_logout file identical across Ubuntu systems serves as perfect known plaintext
- Hardcoded password "UHC-March-Global-PW!" found in AuthController.php customLogin function

## Filed into
[[ransom]], [[type-juggling]], [[zip-crypto-known-plaintext]], [[hardcoded-credentials]], [[laravel]], [[php]]