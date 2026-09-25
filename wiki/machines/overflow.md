---
type: machine
title: Overflow
platform: htb
os: linux
difficulty: hard
tags: [linux, web, crypto, sqli, rce, privesc, pwn, binary]
solved: 2026-07-09
sources: [[htb-overflow]]
related: []

# Overflow
> Linux web application server featuring padding oracle attack on encrypted cookies, SQL injection for database access, Exiftool CVE-2021-22204 exploitation for initial shell, and buffer overflow with TOCTOU vulnerability for root access.

## Attack path
1. [[padding-oracle]] attack on auth cookie to forge admin session
2. [[sqli]] in logs panel to dump database and crack developer credentials
3. [[cve-2021-22204]] in Exiftool (version 11.92) via malicious image upload for [[web-rce]]
4. Credential reuse and [[hosts-file-abuse]] to pivot to tester user
5. [[buffer-overflow]] in setuid binary with [[toctou]] vulnerability for arbitrary file read as root

## Techniques used
- [[padding-oracle]] — Decrypt and forge encrypted cookies using PadBuster by exploiting padding oracle vulnerability in cookie validation
- [[sqli]] — Union-based SQL injection in logs.php parameter to extract database contents and user credentials
- [[cve-2021-2021-22204]] — Exiftool arbitrary code execution via crafted DjVu file embedded in uploaded image
- [[credential-reuse]] — Database credentials (developer:sh@tim@n) work across multiple services and SSH access
- [[hosts-file-abuse]] — Modify /etc/hosts (with network group permissions) to redirect taskmanage.overflow.htb for RCE
- [[buffer-overflow]] — Stack-based buffer overflow in file_encrypt binary's name parameter to return to encrypt function
- [[toctou]] — Time-of-check/time-of-use race condition in encrypt function to bypass root file ownership check

## Tools used
- [[nmap]] — Port scanning and service version detection
- [[feroxbuster]] — Web directory brute forcing
- [[padbuster]] — Padding oracle attack tool for cookie decryption and forgery
- [[sqlmap]] — Automated SQL injection testing and database dumping
- [[exiftool]] — Image metadata tool (vulnerable to CVE-2021-22204)
- [[python]] — Exploit script generation and automation
- [[bzz]] — DjVu compression tool for exploit payload creation
- [[djvumake]] — DjVu file creation for Exiftool exploitation
- [[gdb]] — Binary analysis and debugging
- [[hashcat]] — Password cracking for MD5 hashes with sitemask
- [[ssh]] — Shell access and pivoting
- [[nc]] — Netcat for reverse shell handling

## Services / ports
- [[ssh]] (22) — Secure shell access
- [[http]] (80) — Apache web server with PHP applications
- [[smtp]] (25) — Mail server for potential phishing

## Lessons / notes
- Padding oracle attacks can decrypt and forge encrypted cookies when padding validation errors leak information
- SQL injection in blind contexts requires techniques like UNION-based injection or time-based attacks
- Exiftool file parsing vulnerabilities can be exploited through specially crafted file formats
- Credential reuse across services is common and provides effective pivoting opportunities
- File permission issues (network group writable /etc/hosts) can enable powerful redirection attacks
- TOCTOU vulnerabilities in setuid binaries can bypass security checks when there's a delay between check and use
- Buffer overflow exploitation requires careful address calculation and payload construction
