---
type: machine
title: Luanne
platform: htb
os: linux
difficulty: easy
tags: [linux, web, bsd, privesc]
solved: 2026-07-09
sources: [[htb-luanne]]
related: []
---

# Luanne
> First NetBSD box with Supervisord default credentials, Lua command injection in weather API, SSH key in public_html, and doas abuse with encrypted backup containing root password.

## Attack path
1. [[default-credentials]] — Supervisord accessible with user/123
2. [[credential-leak]] — process list reveals httpd command with weather.lua path
3. [[lua-injection]] — os.execute() in city parameter for command injection
4. [[ssh-key-reuse]] — SSH key found in ~/public_html accessible via HTTP with auth
5. [[doas-abuse]] — encrypted backup contains password for doas as root

## Techniques used
- [[default-credentials]] — Supervisord default user/123 credentials
- [[supervisord]] — process manager exposes running commands and arguments
- [[lua-injection]] — string.format with load() allows arbitrary code execution
- [[command-injection]] — os.execute() in Lua for reverse shell
- [[ssh-key-reuse]] — private key in public_html directory accessible via HTTP
- [[http-auth]] — .htpasswd with hashcatable md5crypt credentials (webapi_user/iamthebest)
- [[doas-abuse]] — doas.conf allows r.michaels to run as root with password
- [[backup-decryption]] — netpgp decrypts encrypted tar.gz backup containing password
- [[password-reuse]] — littlebear from backup works for doas authentication

## Tools used
[[nmap]], feroxbuster, [[curl]], hashcat, nc, ssh, netpgp, tar

## Services / ports
- [[ssh]] (22) — OpenSSH 8.0 on NetBSD
- [[http]] (80) — nginx with basic auth
- tor-orport (9001) — Supervisord process manager

## Lessons / notes
- NetBSD uses doas instead of sudo for privilege escalation
- Supervisord often has default credentials and exposes process information
- Lua's load() function is equivalent to JavaScript's eval() — dangerous with user input
- NetBSD httpd -u flag enables ~user/public_html directory access
- Protected symlinks on NetBSD prevents some symlink attacks in world-writable directories
- PGP encryption common on *nix systems for backup files, netpgp available on NetBSD
- .htpasswd files with $1$ prefix use md5crypt easily cracked with hashcat
- doas configuration in /usr/pkg/etc/doas.conf on NetBSD (vs /etc/sudoers)
