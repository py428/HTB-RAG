---
type: machine
title: Dynstr
platform: htb
os: linux
difficulty: medium
tags: [linux, web, dns, ssh, command-injection, wildcard-injection]
solved: 2026-07-09
sources: [[htb-dynstr]]
related: []
---
# Dynstr
> Dynamic DNS provider box with vulnerable DNS update API. Exploit command injection in hostname parameter to get shell, extract SSH private key from strace logs, manipulate DNS records to bypass SSH authorized_keys restrictions, and abuse wildcard injection in sudo script for root.

## Attack path
1. [[command-injection]] — Inject commands via DNS update API hostname parameter using `$()` syntax
2. [[ssh-key-reuse]] — Extract private key from strace debugging logs in support case directory
3. [[dns-manipulation]] — Update DNS records to bypass authorized_keys `from="*.infra.dyna.htb"` restriction
4. [[wildcard-injection]] — Abuse wildcard in cp command in bindmgr.sh script to write SUID binary as root

## Techniques used
- [[command-injection]] — DNS API hostname parameter vulnerable to command execution via subshell syntax
- [[ssh-key-reuse]] — Found SSH private key exposed in strace debugging output
- [[dns-manipulation]] — Used nsupdate with key to add A/PTR records for SSH access bypassing from restriction
- [[wildcard-injection]] — Created files like `--preserve=mode` and SUID bash to exploit cp wildcard as root

## Tools used
[[nmap]], [[feroxbuster]], curl, [[nsupdate]], ssh, scriptreplay

## Services / ports
[[ssh]] (22), [[dns]] (53), [[http]] (80)

## Lessons / notes
- Command injection in DNS API required valid domain suffix, used `$(cmd).no-ip.htb` format
- Private key leaked in strace logs because admin was debugging SFTP connection issues
- SSH authorized_keys had `from="*.infra.dyna.htb"` restriction, bypassed by DNS manipulation
- bindmgr.sh used unsafe `cp .version *` allowing file option injection via crafted filenames
- Bash number comparison quirks allowed flag leak via symlink to root.txt in version check
