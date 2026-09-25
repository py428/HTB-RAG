---
type: machine
title: Attended
platform: htb
os: openbsd
difficulty: insane
tags: [openbsd, linux, web, privesc]
solved: 2026-07-09
sources: [[htb-attended]]
related: []
---
# Attended

> Insane OpenBSD box requiring sophisticated exploitation chaining from SMTP-based phishing through SSH configuration abuse to binary buffer overflow. The attack demonstrates advanced techniques including Vim modeline exploitation, HTTP exfiltration through restricted networks, and ROP chain development for privilege escalation.

## Attack path
1. [[nmap]] reveals [[smtp]] and [[ssh]] services
2. [[smtp-phishing]] to guly user with Vim modeline exploit attachment
3. [[vim-cve]] exploitation for RCE via modelines (CVE-2019-12735)
4. [[http-exfiltration]] through Python requests library due to firewall restrictions
5. [[ssh-proxycommand]] abuse to write SSH keys for freshness user
6. Reverse engineer authkeys binary to find buffer overflow
7. [[buffer-overflow]] exploitation with crafted SSH key and ROP chain
8. [[rop]] chain to execute reverse shell on gateway

## Techniques used
- [[smtp-phishing]] — Email-based social engineering with malicious attachments
- [[vim-cve]] — CVE-2019-12735 modeline command execution
- [[http-exfiltration]] — Base64-encoded command output over HTTP GET requests
- [[ssh-proxycommand]] — ProxyCommand directive for command execution
- [[buffer-overflow]] — Stack-based overflow in SSH authkeys binary
- [[rop]] — Return-oriented programming for arbitrary code execution

## Tools used
- [[nmap]], [[swaks]], [[python2]], [[ssh]], [[gdb]], [[ropper]], [[msf-pattern]]

## Services / ports
- 22/tcp [[ssh]] — OpenSSH 8.0
- 25/tcp [[smtp]] — OpenSMTPD
- 2222/tcp — SSH gateway (internal network)

## Lessons / notes
- Vim modelines can execute arbitrary commands when files are opened
- Firewall restrictions may require creative exfiltration methods (HTTP GET, ICMP)
- SSH ProxyCommand directive executes commands before SSH connection
- OpenBSD authkeys binary handles SSH key validation with fixed buffer size
- Buffer overflow allows ROP chain construction for syscall execution
- Static buffer addresses enable reliable payload construction
- SSH public key structure must be maintained for successful exploitation
