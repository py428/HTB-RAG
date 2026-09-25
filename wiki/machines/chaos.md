---
type: machine
title: Chaos
platform: htb
os: linux
difficulty: medium
tags: [linux, web, crypto, mail]
solved: 2026-07-09
sources: [[htb-chaos]]
related: []
---
# Chaos

> Medium Linux box featuring webmail exploitation, AES decryption, LaTeX RCE, restricted shell escape, and Firefox password recovery for privilege escalation.

## Attack path
1. WordPress credential discovery → [[webmail]] access → encrypted message in Drafts
2. AES decryption → hidden PDF generation service URL
3. [[latex-rce]] via \write18 enabled → www-data shell
4. Password reuse su → ayush user
5. [[rbash-escape]] via tar → proper shell
6. Firefox saved passwords → root password (also works for Webmin)

## Techniques used
- [[webmail-exploitation]] — WordPress credentials grant access to Roundcube webmail
- [[aes-decryption]] — Manual AES-256-CBC decryption with known IV and password
- [[latex-rce]] — Exploited \write18 enabled in pdfTeX for command injection
- [[rbash-escape]] — Used tar with checkpoint action to break out of restricted shell
- [[password-reuse]] — Firefox-saved password reused for system root access

## Tools used
- [[nmap]] — Port scanning identifying HTTP, email services, and Webmin
- [[gobuster]] — Directory brute forcing for web application discovery
- [[wfuzz]] — Virtual host enumeration finding webmail subdomain
- [[imap]] — Email access and attachment retrieval via openssl
- python crypto — AES decryption script reconstruction
- [[curl]] — Command injection via LaTeX service
- [[netcat]] — Reverse shell connections
- firefox_decrypt.py — Firefox saved password extraction

## Services / ports
- [[http]] (80) — WordPress site and PDF generation service
- [[imap]] (143/993) — Email access for credential discovery
- [[pop3]] (110/995) — Email retrieval
- [[smtp]] —隐含 email sending capability
- http (10000) — Webmin administration interface

## Lessons / notes
- WordPress author enumeration can reveal usernames for credential guessing
- Webmail drafts folder often contains sensitive information not in inbox
- LaTeX with \write18 enabled allows arbitrary command execution
- AES-256-CBC decryption requires key, IV, and ciphertext (all found in this case)
- Restricted shells (rbash) can often be escaped using commands with checkpoint features
- Firefox saved passwords can be extracted even without master password known
- Service passwords (Webmin) are often reused for system access
- Hidden URLs discovered in encrypted messages may lead to additional attack surfaces
