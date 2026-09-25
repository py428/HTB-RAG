---
type: machine
title: SwagShop
platform: htb
os: linux
difficulty: easy
tags: [linux, web, php, ecommerce, sudo]
solved: 2026-07-09
sources: [[htb-swagshop]]
related: []
---
# SwagShop
> Easy Linux box running vulnerable Magento e-commerce site. Exploit authentication bypass to add admin user, then use PHP object injection vulnerability to get RCE. Privilege escalation via sudo vi abuse.

## Attack path
1. [[magento-auth-bypass]] — Exploit "Shoplift" SQL injection to add admin user
2. [[php-object-injection]] — Abuse Magento CVE-2015-2XXX for authenticated RCE
3. [[webshell]] — Deploy PHP webshell via Magento package upload or object injection
4. [[reverse-shell]] — Upgrade to interactive shell via nc
5. [[sudo-hijack]] — Abuse sudo vi privileges to read root flag and get root shell

## Techniques used
- [[magento-auth-bypass]] — Shoplift exploit adds admin user via SQL injection
- [[php-object-injection]] — Magento < 1.9.0.1 vulnerable to authenticated object injection
- [[webshell-upload]] — Upload malicious Magento package containing PHP webshell
- [[sudo-hijack]] — GTFOBins vi escape to spawn root shell from sudo

## Tools used
[[nmap]], [[gobuster]], python (mechanize), [[nc]], [[msfvenom]], [[john]], [[zip2john]]

## Services / ports
[[ssh]] (22), [[http]] (80)

## Lessons / notes
- Magento Shoplift exploit bypasses authentication and adds admin user
- PHP object injection in Magento uses install date from local.xml for signature bypass
- sudo vi can be escaped with `:set shell=/bin/sh` and `:shell` commands
- GTFOBins provides reliable escape sequences for sudo-privileged binaries