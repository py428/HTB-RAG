---
type: source
title: "HTB Ethereal writeup"
raw: raw/htb-ethereal.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[ethereal]]
---
# Source: HTB Ethereal writeup

> Comprehensive guide for Ethereal Windows box covering FTP enumeration, password vault recovery, HTTP basic auth bruteforcing, blind command injection with DNS exfiltration, LNK file poisoning, and code signing abuse.

## Key facts extracted
- FTP anonymous access contains disk images with PasswordBox database
- PasswordBox master password: "password" — contains multiple credentials including alan / !C414m17y57r1k3s4g41n!
- TCP 8080 requires HTTP basic auth; vulnerable to Hydra bruteforce
- Ping panel vulnerable to command injection via Windows conditional operators (&, &&, ||)
- Firewall blocks most outbound traffic except DNS, TCP 73, 136
- OpenSSL on target allows encrypted reverse shells
- Public Desktop shortcuts directory writable; used for LNK poisoning
- D:\Certs contains CA certificate (MyCA.cer) and private key (MyCA.pvk) for code signing
- MSI files in D:\DEV\MSIs executed automatically by rupal (Administrator)

## Filed into
[[ethereal]], [[command-injection]], [[dns-exfiltration]], [[lnk-poisoning]], [[code-signing]]
