---
type: machine
title: LaCasaDePapel
platform: htb
os: linux
difficulty: easy
tags: [ftp, php, ssl, ssh, linux, privesc]
solved: 2026-07-09
sources: [[htb-lacasadepapel]]
related: []
---
# LaCasaDePapel
> LaCasaDePapel is an easy Linux box themed after the TV show. The attack path exploits a modified VSFTPD backdoor that opens a Psy Shell, extracts a CA key to generate client certificates for mutual TLS authentication, performs path traversal to obtain SSH credentials, and abuses supervisor configuration for privilege escalation.

## Attack path
1. [[vsftpd-backdoor]] — Trigger modified VSFTPD backdoor with ":)" in username
2. [[psy-shell]] — Access Psy Shell PHP debugging tool
3. [[ca-key-theft]] — Extract CA private key from filesystem
4. [[mutual-tls-auth]] — Generate client certificate and authenticate to HTTPS site
5. [[path-traversal]] — Read arbitrary files including SSH keys via base64-encoded paths
6. [[supervisor-ini-replacement]] — Replace supervisor config file by deleting and recreating

## Techniques used
- [[vsftpd-backdoor]] — Modified VSFTPD 2.3.4 opens Psy Shell and adds iptables rule for attacker IP
- [[psy-shell]] — Limited PHP shell with disabled dangerous functions but file access capabilities
- [[ca-key-theft]] — Extract CA key to sign client certificates for mutual TLS
- [[mutual-tls-auth]] — Generate client certificate using extracted CA key for HTTPS authentication
- [[path-traversal]] — Base64-encoded path traversal to read arbitrary files from private area
- [[supervisor-ini-replacement]] — Delete and recreate supervisor .ini file in user-owned directory

## Tools used
- [[nmap]]
- [[netcat]]
- [[openssl]]
- [[curl]]
- [[ssh]]

## Services / ports
- [[ftp]] (21)
- [[ssh]] (22)
- [[http]] (80)
- [[https]] (443)

## Lessons / notes
- Modified VSFTPD backdoor uses iptables to restrict access to Psy Shell instead of binding to localhost
- Psy Shell is a PHP debugging REPL with system() and other dangerous functions disabled
- CA private key allows signing client certificates for mutual TLS authentication
- Supervisor includes .ini files from user-owned directories, enabling config file replacement
- Cannot edit files owned by root in user-owned directories, but can delete and recreate them