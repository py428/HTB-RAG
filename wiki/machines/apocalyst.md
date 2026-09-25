---
type: machine
title: Apocalyst
platform: htb
os: linux
difficulty: medium
tags: [wordpress, web, steganography, linux, privesc, ctf]
solved: 2026-07-09
sources: [[htb-apocalyst]]
related: []
---
# Apocalyst

> Apocalyst is a WordPress site that requires building custom wordlists from website content, using steganography to extract passwords, and exploiting writable /etc/passwd for root access through password manipulation.

## Attack path

1. [[cewl-wordlist]] — Generate custom wordlist from website content
2. [[steganography]] — Extract password list from steganographically hidden image
3. [[wordpress-enumeration]] — Brute force WordPress credentials using extracted list
4. [[wordpress-plugin-abuse]] — Edit WordPress theme files for webshell
5. [[etc-passwd-write]] — Modify /etc/passwd to create root user with UID 0

## Techniques used

- [[subdomain-enumeration]] — Host header-based virtual host discovery
- [[cewl-wordlist]] — Custom wordlist generation from website content
- [[steganography]] — StegHide extraction of password list from image file
- [[wordpress-enumeration]] — WPScan for user enumeration and vulnerability assessment
- [[directory-brute-force]] — Web directory and file discovery with wfuzz
- [[password-brute-force]] — WordPress password brute force with custom wordlist
- [[theme-editor-abuse]] — WordPress theme file editing for webshell deployment
- [[webshell]] — PHP webshell for command execution
- [[linpeas]] — Linux privilege escalation enumeration
- [[etc-passwd-write]] — Writable /etc/passwd exploitation for root access

## Tools used

- [[nmap]] — TCP port scanning and service fingerprinting
- [[wpscan]] — WordPress vulnerability scanner and user enumeration
- [[gobuster]] — Web directory brute forcing
- [[wfuzz]] — Advanced web fuzzing with response filtering
- cewl — Custom wordlist generation from web content
- [[steghide]] — Steganography tool for data extraction
- [[wpscan]] — WordPress password brute forcing
- [[netcat]] — Reverse shell connections
- linpeas — Linux privilege enumeration script

## Services / ports

- 22/tcp — ssh — OpenSSH 7.2p2 Ubuntu
- 80/tcp — http — Apache httpd 2.4.18 with WordPress 4.8

## Lessons / notes

- WordPress sites often require domain names to load properly (add to /etc/hosts)
- Custom wordlists from website content more effective than generic lists
- Steganography can hide critical information in benign-looking files
- WordPress theme editing provides easy webshell deployment with admin access
- Writable /etc/passwd is a serious security misconfiguration
- CTF-style challenges sometimes require building custom tools rather than using standard exploits
- Comments in HTML source can provide important hints for further exploitation

## CVEs

- No specific CVEs exploited — relies on misconfigurations and CTF-style challenges
