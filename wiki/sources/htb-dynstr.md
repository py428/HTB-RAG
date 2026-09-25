---
type: source
title: "HTB Dynstr writeup"
raw: raw/htb-dynstr.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[dynstr]]
---
# Source: HTB Dynstr writeup
> Medium Linux box with dynamic DNS service. Exploited command injection in DNS API, extracted SSH keys from debugging logs, bypassed SSH restrictions via DNS manipulation, and abused wildcard injection in sudo script. Writeup covers DNS API exploitation, strace analysis, and Bash number comparison quirks.

## Key facts extracted
- Dynamic DNS service with no-ip.com compatible API on /nic/update
- Command injection in hostname parameter via $(cmd) syntax
- Private key leaked in strace logs from SFTP debugging session
- SSH authorized_keys restricted connections from *.infra.dyna.htb
- bindmgr.sh script used unsafe cp command with wildcards
- DNS zone updates possible with infra.key credentials

## Filed into
[[dynstr]], [[command-injection]], [[ssh-key-reuse]], [[dns-manipulation]], [[wildcard-injection]]
