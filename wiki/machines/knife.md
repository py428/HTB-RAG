---
type: machine
title: Knife
platform: htb
os: linux
difficulty: easy
tags: [linux, web, backdoor, privesc]
solved: 2026-07-09
sources: [[htb-knife]]
related: []
---
# Knife
> Ubuntu 20.04 box exploiting a PHP 8.1.0-dev backdoor from the 2021 PHP source code compromise, with privilege escalation through the knife command.

## Attack path
1. [[php-backdoor]] via User-Agentt header → RCE as james
2. [[sudo-abuse]] of knife tool → root shell

## Techniques used
- [[php-backdoor]] — PHP 8.1.0-dev backdoor from March 2021 source compromise, triggered with User-Agentt: zerodium header
- [[sudo-abuse]] — Knife (Chef management tool) exec command for Ruby code execution

## Tools used
[[nmap]], [[feroxbuster]], [[curl]], [[netcat]], knife

## Services / ports
- 22/tcp — [[ssh]] (OpenSSH 8.2)
- 80/tcp — [[http]] (Apache 2.4.41 with PHP 8.1.0-dev)

## Lessons / notes
- PHP 8.1.0-dev was a compromised version with a backdoor inserted into the source code
- The backdoor required a specific User-Agentt header (note the double 't') starting with "zerodium"
- At release time this wasn't widely known, but became well-documented within days
- Knife tool can execute arbitrary Ruby code via the exec command
- GTFObins page for knife was created after this box's release
