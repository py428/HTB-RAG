---
type: machine
title: Irked
platform: htb
os: linux
difficulty: easy
tags: [irc, linux, steganography, privesc]
solved: 2026-07-09
sources: [[htb-irked]]
related: []
---
# Irked
> Irked is an easy Linux box featuring an IRC server with a backdoor vulnerability. The exploitation path involves exploiting the UnrealIRCd backdoor for initial access, using steganography to extract credentials from an image, and abusing a vulnerable setuid binary for privilege escalation.

## Attack path
1. [[unrealircd-backdoor]] via AB; prefix command execution
2. [[steganography]] to extract password from irked.jpg image
3. [[setuid-binary-abuse]] via /usr/bin/viewuser calling /tmp/listusers

## Techniques used
- [[unrealircd-backdoor]] — Exploiting backdoor in UnrealIRCd 3.2.8.1
- [[steganography]] — Extracting hidden data with steghide
- [[setuid-binary-abuse]] — Abusing setuid binary that executes script from /tmp
- [[command-injection]] — Writing commands to /tmp/listusers for execution as root

## Tools used
- [[nmap]] — Full TCP and UDP port scanning
- [[hexchat]] — IRC client for server exploration
- [[netcat]] — Exploit delivery and shell handling
- [[steghide]] — Extracting hidden data from steganographic image
- [[LinEnum]] — Linux privilege escalation enumeration script
- [[ltrace]] — Tracing library calls to analyze binary behavior

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 6.7p1 Debian
- 80/tcp — [[http]] — Apache 2.4.10 with steganographic image
- 111/tcp — [[rpcbind]]
- 6697/tcp — IRC (UnrealIRCd with backdoor)
- 8067/tcp — IRC (UnrealIRCd with backdoor)
- 65534/tcp — IRC (UnrealIRCd with backdoor)

## Lessons / notes
- UnrealIRCd 3.2.8.1 contains backdoor triggered by "AB;" prefix
- Simple backdoor payloads can execute commands without authentication
- Steganography often hides credentials in images on CTF-style boxes
- Setuid binaries that call user-writable scripts are common privesc vectors
- Scripts in /tmp are often writable and executable by low-priv users
- ltrace useful for understanding what system calls binaries make
- Exim 4.84_2 has vulnerabilities but requires Perl support (not present here)