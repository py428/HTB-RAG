---
type: machine
title: Shrek
platform: htb
os: linux
difficulty: hard
tags: [linux, web, steganography, ftp, privesc]
solved: 2026-07-09
sources: [[htb-shrek]]
related: []
---
# Shrek
> Shrek-themed website with file upload functionality leading to steganography in MP3 file, FTP credentials extraction, and a wildcard chown privilege escalation.
## Attack path
1. Directory brute force → /uploads with malicious files → Secret dir hint in PHP webshell
2. [[steganography-audio]] → Spectrogram analysis of MP3 reveals FTP credentials (donkey:d0nk3y1337!)
3. [[ftp-access]] → Download encrypted SSH key + base64-encoded files
4. [[ecc-decryption]] → Decrypt blob with seccure using "PrinceCharming" password → SSH key password (shr3k1sb3st!)
5. [[ssh]] as sec → [[wildcard-exploit]] with chown → Modify /etc/passwd → root
## Techniques used
- [[steganography-audio]] — Hidden data in MP3 spectrogram at high frequencies reveals FTP credentials
- [[ecc-decryption]] — Elliptic Curve Cryptography decryption using seccure library to decrypt password blob
- [[wildcard-exploit]] — Abuse chown with wildcard and --reference flag to change file ownership
- [[passwd-modification]] — Add root user to /etc/passwd after gaining ownership via wildcard exploit
## Tools used
[[nmap]], [[gobuster]], audacity, [[seccure]], [[john]], [[openssl]], [[ssh]]
## Services / ports
- [[http]] (80) - Apache 2.4.27
- [[ftp]] (21) - vsftpd 3.0.3
- [[ssh]] (22) - OpenSSH 7.5
## Lessons / notes
- Always check spectrogram view in audio analysis tools for hidden data beyond visible waveform
- Wildcard exploits with commands like chown can be devastating if cron jobs run them unattended
- File modified times can reveal cron jobs and automation when traditional enumeration fails
- ECC decryption with seccure requires specific parameters from encrypted blob structure
- The immutable flag (chattr +i) protects files even from root modifications
