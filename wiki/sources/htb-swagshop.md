---
type: source
title: "HTB SwagShop writeup"
raw: raw/htb-swagshop.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[swagshop]]
---
# Source: HTB SwagShop writeup
> Beginner-friendly Linux box featuring Magento 1.x e-commerce platform. Initial access via Magento "Shoplift" authentication bypass exploit to add admin user, followed by PHP object injection (CVE-2015-2XXX) for authenticated RCE. Privilege escalation through sudo vi abuse using GTFOBins techniques.

## Key facts extracted
- Magento version < 1.9.0.1 vulnerable to authenticated PHP object injection
- Shoplift exploit adds admin user with credentials: ypwq:123
- Install date from /app/etc/local.xml: Wed, 08 May 2019 07:23:09 +0000
- PHP object injection requires install date for signature bypass
- sudo privileges: (root) NOPASSWD: /usr/bin/vi /var/www/html/*
- vi escape via `:set shell=/bin/sh` and `:shell` commands
- Alternative method: malicious Magento package upload (now patched)

## Filed into
[[swagshop]], [[magento-auth-bypass]], [[php-object-injection]], [[webshell-upload]], [[sudo-hijack]]