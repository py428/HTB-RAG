---
type: machine
title: Brainfuck
platform: htb
os: linux
difficulty: insane
tags: [ad, linux, web, privesc, crypto, wordpress]
solved: 2026-07-09
sources: [[htb-brainfuck]]
related: []
---
# Brainfuck
> Legacy CTF-style Linux box featuring WordPress exploitation, Vigenère cipher decryption, RSA cryptographic weaknesses, and LXD container privilege escalation.
## Attack path
1. [[wordpress-plugin-exploit]] — WP Support Plus privilege escalation to admin access
2. [[smtp-credentials-exposure]] — Extract SMTP creds from WordPress settings
3. [[vigenere-cipher]] — Decrypt forum messages to get SSH key URL
4. [[ssh-key-cracking]] — Crack encrypted SSH key with john
5. [[rsa-cryptography-weakness]] — Decrypt root flag with leaked RSA parameters
6. [[lxd-container-privilege-escalation]] — Alternative root via LXD group membership
## Techniques used
- [[wordpress-plugin-exploit]] — WP Support Plus Responsive Ticket System privilege escalation vulnerability (CVE-2017-17434)
- [[vigenere-cipher]] — Manual cryptanalysis of forum signatures to recover encryption key
- [[rsa-cryptography-weakness]] — Exploit leaked p, q, e parameters to calculate RSA private key and decrypt ciphertext
- [[lxd-container-privilege-escalation]] — Abuse LXD group permissions to mount host filesystem in container
## Tools used
- [[nmap]] — Port scanning and service enumeration
- [[wpscan]] — WordPress vulnerability scanner and plugin enumeration
- [[exiftool]] — Not used in this writeup
- [[curl]] — Download SSH key from HTTPS URL
- [[john]] — Crack SSH key passphrase using ssh2john.py
- [[openssl]] — RSA decryption and key manipulation
- [[ssh]] — Remote access with cracked SSH key
- python — Cryptanalysis and RSA attack implementation
## Services / ports
- [[ssh]] (22) — OpenSSH 7.2p2 Ubuntu
- [[smtp]] (25) — Postfix smtpd
- pop3 (110) — Dovecot pop3d
- imap (143) — Dovecot imapd  
- [[http]] (443) — nginx 1.10.0 with WordPress
## Lessons / notes
- WordPress plugin vulnerabilities can provide unauthorized authentication bypass
- Legacy CTF-style boxes may have unrealistic but educational attack chains
- Cryptographic implementations often have exploitable weaknesses when parameters are leaked
- LXD group membership is a powerful privilege escalation vector on Linux
- Multi-stage exploitation combining web, crypto, and system weaknesses