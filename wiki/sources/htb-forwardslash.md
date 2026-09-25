---
type: source
title: "HTB ForwardSlash writeup"
raw: raw/htb-forwardslash.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[forwardslash]]
---
# Source: HTB ForwardSlash writeup
> Complete writeup for ForwardSlash HTB machine covering RFI/LFI vulnerabilities, XXE exploitation, time-based backup binary abuse, and LUKS encryption mounting.

## Key facts extracted
- Ubuntu 18.04 system with nginx webserver
- Profile picture function vulnerable to RFI/LFI
- API test console at /dev with XXE vulnerability
- FTP credentials embedded in source code: chiv:N0bodyL1kesBack/
- backup SUID binary uses time-based MD5 hash for file access
- Custom encryption scheme broken with rockyou.txt wordlist
- sudo permissions for cryptsetup and mount commands

## Filed into
[[forwardslash]], [[rfi]], [[lfi]], [[xxe]], [[time-based-race]], [[crypto-weakness]], [[luks-mount]]
