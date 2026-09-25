---
type: source
title: "HTB Breadcrumbs writeup"
raw: raw/htb-breadcrumbs.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[breadcrumbs]]
---
# Source: HTB Breadcrumbs writeup
> Hard Windows box featuring directory traversal for source code leaks, PHP session cookie and JWT token forgery, webshell upload, Sticky Notes password extraction, and password manager SQL injection.
## Key facts extracted
- Directory traversal in bookController.php: book=..\..\path\to\file
- PHP session cookie algorithm: username.md5("s4lTy_stR1nG_" . char . "(!528./9890")
- JWT secret: 6cb9c1a2786a483ca5e44571dcc5f3bfa298593a6376ad92185c3258acd5591e
- Database credentials: bread/jUli901 for MySQL
- Password hash format: MD5($salt . $password) with salt "NaCl"
- Sticky Notes location: plum.sqlite in user AppData
- Password manager at http://passmanager.htb:1234/index.php
- Admin password decrypted: p@ssw0rd!@#$9890./
## Filed into
[[breadcrumbs]], [[directory-traversal]], [[prng-prediction]], [[jwt-forgery]], [[php-deserialization]], [[hash-cracking]], [[sticky-notes-extraction]], [[sqli]]