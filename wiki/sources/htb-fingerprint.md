---
type: source
title: "HTB Fingerprint writeup"
raw: raw/htb-fingerprint.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[fingerprint]]
---
# Source: HTB Fingerprint writeup
> Extremely detailed 0xdf writeup covering the complete multi-stage exploitation including execute-after-redirect, HQL injection, XSS, Java deserialization, ECB padding oracle, and SSH key brute forcing. Shows complex vulnerability chaining.
## Key facts extracted
- EAR vulnerability allows viewing admin page content despite 302 redirect
- HQL injection used to brute force usernames, passwords, and fingerprints
- XSS used to steal admin fingerprint for authentication to GlassFish application
- Custom Java deserialization payload exploits command injection in UserProfileStorage
- SUID cmatch binary enables character-by-character SSH key brute forcing
- ECB padding oracle attack leaks SECRET key from beta Flask application
- Cookie manipulation and directory traversal provide root access
## Filed into
[[fingerprint]], [[execute-after-redirect]], [[hqli]], [[xss]], [[java-deserialization]], [[ecb-padding-oracle]], [[cookie-manipulation]]
