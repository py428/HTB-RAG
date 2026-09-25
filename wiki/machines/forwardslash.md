---
type: machine
title: ForwardSlash
platform: htb
os: linux
difficulty: hard
tags: [linux, web, lfi, xxe, sudo, luks, crypto]
solved: 2026-07-09
sources: [[htb-forwardslash]]
related: []
---
# ForwardSlash
> ForwardSlash is a hard Linux box involving LFI and XXE vulnerabilities to leak source code and credentials, followed by abusing a time-based backup SUID binary and breaking custom encryption to mount an encrypted LUKS volume containing root's SSH key.

## Attack path
1. [[rfi]] in profile picture function to access localhost
2. [[lfi]] with PHP filters to leak source code and credentials  
3. Find FTP credentials in /dev/index.php source
4. SSH access as chiv with FTP credentials
5. Exploit backup SUID binary with [[time-based-race]] to read pain's files
6. Find database credentials in backup config
7. su to pain user
8. Break custom encryption to decrypt LUKS key
9. Mount LUKS volume and extract root SSH key

## Techniques used
- [[rfi]] — Remote file inclusion to access localhost from profile picture
- [[lfi]] — Local file inclusion with PHP filters to read source code
- [[xxe]] — XML external entity to read files from API test console  
- [[time-based-race]] — Race condition in backup binary using MD5 hash of current time
- [[crypto-weakness]] — Breaking weak custom encryption scheme
- [[luks-mount]] — Mounting encrypted LUKS volume with cryptsetup
- [[sudo-abuse]] — Abusing sudo permissions for cryptsetup and mount

## Tools used
[[nmap]], [[wfuzz]], [[gobuster]], [[curl]], Burp Suite, [[ssh]], [[openssl]], responder, [[linpeas]]

## Services / ports
- 22/tcp — [[ssh]] (OpenSSH 7.6)
- 80/tcp — [[http]] (nginx)

## Lessons / notes
- The backup binary uses MD5 hash of current timestamp for filename
- Weak crypto scheme where multiple passwords can decrypt the same message
- The intended path used XXE with FTP protocol to capture credentials
- sudo permissions can be abused to create and mount custom LUKS containers
