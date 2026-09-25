---
type: machine
title: Moderators
platform: htb
os: linux
difficulty: hard
tags: [linux, web, wordpress, virtualization, encryption]
solved: 2026-07-09
sources: [[htb-moderators]]
related: []
---
# Moderators

> Moderators is a Hard-level Linux box featuring multiple web exploitation stages, including IDOR vulnerabilities, file upload bypasses, WordPress plugin vulnerabilities, and VirtualBox encryption cracking, culminating in LUKS password recovery to achieve root access.

## Attack path
1. Discover [[idor]] vulnerability in blog reports system to find hidden upload functionality
2. Bypass file upload filters using PDF magic bytes and .php.pdf double extension
3. Upload PHP webshell using popen() function to bypass disable_functions restrictions
4. Exploit Brandfolder WordPress plugin LFI to gain lexi user access
5. Extract WordPress database credentials and decrypt stored SSH key for john user
6. Download and crack VirtualBox encrypted disk image using pyvboxdie-cracker
7. Mount LUKS-encrypted volume and crack password using custom script
8. Use recovered password for sudo access to obtain root shell

## Techniques used
- [[idor]] — Discover hidden blog reports by iterating through MD5-hashed report IDs
- [[file-upload-bypass]] — Bypass PDF upload validation using magic bytes (%PDF-) and double extension (.pdf.php)
- [[disable-functions-bypass]] — Use popen() instead of exec/system/shell_exec to bypass PHP disable_functions
- [[wordpress-lfi]] — Exploit Brandfolder plugin wp_abspath parameter for local file inclusion
- [[encryption-decryption]] — Decrypt WordPress passwords-manager plugin AES-128 encrypted data
- [[virtualbox-encryption-cracking]] — Crack VirtualBox VDI encryption using pyvboxdie-cracker or hashcat
- [[luks-cracking]] — Brute force LUKS passphrase using cryptsetup and wordlist
- [[password-reuse]] — Reuse cracked VirtualBox password for sudo access

## Tools used
- [[nmap]] — Port scanning and service enumeration
- [[feroxbuster]] — Directory brute force on web application
- [[wfuzz]] — IDOR fuzzing to discover hidden report numbers
- [[hydra]] — Web form brute force for WordPress authentication
- [[curl]] — Web shell interaction and HTTP requests
- [[chisel]] — SOCKS proxy tunneling to access internal WordPress site
- [[php]] — Webshell creation and encryption/decryption operations
- [[openssl]] — Certificate conversion for Rubeus authentication
- [[rubeus]] — Extract NTLM hash from PKINIT certificate
- [[ssh]] — Remote access using private keys
- [[pyvboxdie-cracker]] — VirtualBox VDI password recovery tool
- [[hashcat]] — VirtualBox encryption hash cracking (mode 27600)
- [[cryptsetup]] — LUKS volume testing and mounting
- [[python]] — Custom LUKS brute force script

## Services / ports
- [[ssh]] (22) — Secure shell access
- [[http]] (80) — Public web application with upload functionality
- [[mysql]] (3306) — WordPress database backend (localhost only)

## Lessons / notes
- IDOR vulnerabilities can be exploited when object IDs follow predictable patterns like MD5 hashes
- File upload filters that check magic bytes can often be bypassed with minimal headers
- PHP's popen() function can execute commands even when shell_exec/system are disabled
- WordPress plugins may have file inclusion vulnerabilities that don't require authentication
- AES-128 encryption in WordPress can be cracked when the encryption key is stored in the database
- VirtualBox VDI encryption uses PBKDF2-HMAC-SHA256 with AES-256-XTS that can be cracked with dictionary attacks
- LUKS encryption can be tested non-destructively using luksOpen --test-passphrase
- WordPress wp-config.php files often contain database credentials with high privileges
- Internal web applications on non-standard ports may be missed during basic enumeration
