---
type: machine
title: FluJab
platform: htb
os: linux
difficulty: hard
tags: [linux, web, sqli, ssh, kernel, rbash]
solved: 2026-07-09
sources: [[htb-flujab]]
related: []
---
# FluJab
> Hard-difficulty Linux box featuring complex multi-stage exploitation. Involves cookie manipulation, SMTP configuration abuse, SQL injection via email, SSH with deprecated keys and TCP wrappers, and local privilege escalation through vulnerable screen binary.

## Attack path
1. [[cookie-manipulation]] to access SMTP configuration page
2. Configure SMTP to point to attacker server via [[parameter-tampering]]
3. [[sqli]] on cancellation form, reading results via email
4. Database enumeration leads to Ajenti admin credentials
5. [[ssh]] access using [[cve-2008-0166]] deprecated SSH keys
6. [[tcp-wrapper]] manipulation to whitelist IP in /etc/hosts.allow
7. [[rbash]] escape using make command
8. [[suid-binary]] exploit via vulnerable screen binary (CVE-2017-5618)
9. [[kernel-exploit]] / [[ld.so.preload]] abuse for root shell

## Techniques used
- [[cookie-manipulation]] — Modified Modus and Registered cookies to access SMTP configuration and whitelist
- [[parameter-tampering]] — Intercepted and modified SMTP server parameter to point to attacker IP
- [[sqli]] — Union-based SQL injection on cancellation form to enumerate database and extract admin credentials
- [[cve-2008-0166]] — Exploited Debian OpenSSL weak key generation to crack SSH private key
- [[tcp-wrapper]] — Modified /etc/hosts.allow to whitelist attacking IP for SSH access
- [[rbash]] — Escaped restricted shell using make command with special syntax
- [[suid-binary]] — Exploited screen 4.5.0 SUID binary to write arbitrary files as root
- [[ld.so.preload]] — Used screen exploit to write /etc/ld.so.preload for shared library preloading

## Tools used
- [[nmap]], [[wfuzz]], [[openssl]]
- [[smtpd]], [[python]], [[hashcat]]
- [[ssh]], [[ssh-keygen]], [[make]]
- [[screen]], [[gcc]]

## Services / ports
- [[ssh]] (22), [[http]] (80, 443, 8080)
- SMTP (25, internal), nginx reverse proxy

## Lessons / notes
- Cookie manipulation can bypass access controls in web applications
- SQL injection results can be exfiltrated via email when direct access is blocked
- CVE-2008-0166 affects SSH keys generated on Debian systems between 2006-2008
- TCP Wrappers (/etc/hosts.allow) can be used to control SSH access by IP
- screen SUID vulnerability allows arbitrary file write, leading to root via ld.so.preload
