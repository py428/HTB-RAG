---
type: machine
title: Smasher2
platform: htb
os: linux
difficulty: insane
tags: [web, kernel, exploit, linux]
solved: 2026-07-09
sources: [[htb-smasher2]]
related: []
---
# Smasher2
> Insane-difficulty Linux box featuring binary exploitation of a Python C extension, WAF bypass techniques, and kernel driver exploitation. Exploits reference counting bug in compiled session manager module to leak API keys, bypasses WAF with character encoding, and abuses vulnerable kernel module for root via mmap credential structure manipulation.

## Attack path
1. [[python-reference-counting-bug]] in ses.so C extension to leak API key via garbage collection confusion
2. [[waf-bypass]] using backslash escapes to execute commands through API endpoint  
3. [[kernel-mmap-exploitation]] to manipulate process credentials structure and gain root privileges

## Techniques used
- [[python-reference-counting-bug]] — Exploited missing Py_INCREF in error path allowing garbage collection to free data_object while still referenced, causing secret_token_info to be allocated at same memory location
- [[waf-bypass]] — Evaded WAF filtering using backslash escapes (i\\d for id, mk\\dir for mkdir) and single quotes (i''d) to break up command names
- [[kernel-mmap-exploitation]] — Mapped vulnerable dhid kernel module via mmap, scanned memory for credential structures by matching repeated UIDs, modified UID/GID values to 0, set capabilities to 0xffffffff, and spawned root shell
- [[ssh-key-injection]] — Uploaded base64-encoded SSH public key via API and decoded into authorized_keys

## Tools used
- [[nmap]] for port and service discovery
- [[hydra]] for brute forcing backup directory credentials
- [[curl]] for API interaction
- [[base64]] for encoding SSH public key
- [[gcc]] for kernel exploit compilation
- [[strings]] for analyzing kernel module

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 7.6p1 Ubuntu 4ubuntu0.2
- 53/tcp — [[dns]] — ISC BIND 9.11.3-1ubuntu1.3  
- 80/tcp — [[http]] — Apache 2.4.29 (Ubuntu)

## Lessons / notes
- Python C extensions require manual reference counting with Py_INCREF/Py_DECREF macros to prevent premature garbage collection
- WAF evasion techniques include character encoding variations, backslash escapes, and string splitting
- Kernel credential structures contain 8 consecutive UID/GID values followed by capabilities — useful identification pattern for memory scanning
- mmap with PROT_WRITE allows direct kernel memory manipulation when vulnerable module is loaded
- The session manager binary also contained logic bug where get_internal_pwd returned first list element (username) instead of second (password), enabling Administrator:Administrator authentication