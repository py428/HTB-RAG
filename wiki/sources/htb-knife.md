---
type: source
title: "HTB Knife writeup"
raw: raw/htb-knife.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[knife]]
---
# Source: HTB Knife writeup
> Brief 0xdf writeup covering the PHP 8.1.0-dev backdoor vulnerability from the 2021 PHP source compromise and privilege escalation via the knife tool.

## Key facts extracted
- Ubuntu 20.04 with Apache 2.4.41 running PHP 8.1.0-dev (backdoored version)
- PHP source repository was compromised in March 2021, adding backdoor to ext/zlib/zlib.c
- Backdoor triggered via User-Agentt header starting with "zerodium" (note the double 't')
- James user had sudo access to /usr/bin/knife for Ruby code execution
- GTFObins page for knife was created after Knife's release

## Filed into
[[knife]], [[php-backdoor]], [[sudo-abuse]]
