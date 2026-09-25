---
type: machine
title: Valentine
platform: htb
os: linux
difficulty: easy
tags: [linux, web, heartbleed, ssh, easy]
solved: 2026-07-09
sources: [[htb-valentine]]
related: []
---
# Valentine
> Easy box featuring Heartbleed vulnerability to extract SSH key password, tmux session hijacking for root access, and DirtyCow kernel exploit as alternative privesc path.

## Attack path
1. [[heartbleed]] — exploit OpenSSL Heartbleed to leak encoded password from memory
2. [[ssh-key-reuse]] — use decoded password to decrypt SSH private key from `/dev/hype_key`
3. [[tmux-session-hijack]] — attach to root tmux session via socket in `/.devs/`
4. Alternative: [[dirty-cow]] — exploit DirtyCow kernel vulnerability to add root user

## Techniques used
- [[heartbleed]] — OpenSSL Heartbleed (CVE-2014-0160) leaks memory contents including base64 encoded password
- [[ssh-key-reuse]] — Encrypted SSH private key uses leaked password for authentication
- [[tmux-session-hijack]] — Root tmux session socket accessible via group permissions
- [[dirty-cow]] — Kernel race condition exploit (CVE-2016-5195) for privilege escalation

## Tools used
- [[nmap]] — port scanning and SSL certificate detection
- heartbleed exploit script — memory leak exploitation
- openssl — RSA key decryption
- gobuster — directory brute forcing
- [[ssh]] — key-based authentication
- DirtyCow exploit — kernel race condition exploit

## Services / ports
- [[ssh]] — 22/tcp
- [[http]] — 80/tcp (Apache)
- [[https]] — 443/tcp (Apache with Heartbleed vulnerability)
- mdns — 5353/udp

## Lessons / notes
- Heartbleed vulnerability can leak sensitive data from server memory
- Base64 encoded passwords in memory can be decrypted and reused
- Encrypted SSH keys can be decrypted with openssl if password is known
- tmux sockets can be accessible to non-root users via group permissions
- Ubuntu 12.04 (3.2.0 kernel) vulnerable to DirtyCow exploit
- Old kernels often have known privilege escalation vulnerabilities
