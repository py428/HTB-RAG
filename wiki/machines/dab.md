---
type: machine
title: Dab
platform: htb
os: linux
difficulty: hard
tags: [linux, web, privesc, memcached, steganography, brute-force, library-hijacking, ldconfig]
solved: 2026-07-09
sources: [[htb-dab]]
related: []
---
# Dab

> Hard Linux box with two web applications where brute-forced credentials populate a memcached instance accessible through a TCP proxy, leading to user access, then privilege escalation via library hijacking and ldconfig abuse to create a malicious shared library.

## Attack path

1. [[nmap]] port scan → [[ftp]], [[ssh]], and two [[http]] services
2. [[steghide]] extraction from FTP image reveals troll message
3. [[hydra]] brute force → login credentials for admin on port 80
4. Login populates [[memcached]] → enumerate users and hashes via TCP proxy on port 8080
5. [[hashcat]] crack MD5 hashes → credentials for genevieve user
6. [[ssh]] access → shell as genevieve
7. [[library-hijacking]] → create malicious `libseclogin.so` and use [[ldconfig]] to load it via [[myexec]] SUID binary → root shell

## Techniques used

- [[memcached-enumeration]] — TCP proxy on port 8080 provides access to memcached for data exfiltration and enumeration
- [[steganography]] — Steghide extraction from FTP image reveals troll message (not intended path)
- [[brute-force]] — Hydra used for username enumeration and password brute force on web login
- [[hash-cracking]] — MD5 hashes from memcached cracked using hashcat and rockyou.txt
- [[password-reuse]] — Credentials from memcached work for SSH access
- [[library-hijacking]] — Create malicious shared library loaded by SUID binary to execute arbitrary code as root
- [[ldconfig-abuse]] — SUID `ldconfig` binary allows modifying library search paths to load malicious libraries

## Tools used

- [[nmap]] — Full port scanning and service version detection
- [[hydra]] — Username enumeration and password brute forcing on web login form
- [[steghide]] — Steganography tool for extracting hidden data from FTP image
- [[wfuzz]] — Cookie fuzzing to discover password authentication on port 8080
- [[memcached]] — In-memory data store enumerated via TCP proxy for user credentials
- [[hashcat]] — MD5 hash cracking using rockyou.txt wordlist
- [[gdb]] — Debugging myexec binary to extract hardcoded password
- [[gcc]] — Compile malicious shared library with position-independent code
- [[ldconfig]] — SUID binary abused to load malicious library for privilege escalation

## Services / ports

- 21/tcp [[ftp]] — vsftpd 3.0.3 with anonymous access
- 22/tcp [[ssh]] — OpenSSH 7.2p2 Ubuntu
- 80/tcp [[http]] — nginx 1.10.3 hosting Flask application
- 8080/tcp [[http]] — nginx 1.10.3 hosting TCP proxy service
- 11211/tcp — memcached (localhost only, accessed via proxy)

## Lessons / notes

- Memcached can contain sensitive authentication data and is worth enumerating when accessible
- TCP proxy services can be abused to interact with otherwise restricted services
- SUID binaries like `ldconfig` that modify system library loading paths are powerful privilege escalation vectors
- Library hijacking requires creating a shared object with position-independent code (-fPIC flag)
- Steganography in CTF challenges often contains troll messages rather than useful information
- Brute forcing can be effective when you have small, targeted user lists