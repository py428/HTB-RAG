---
type: machine
title: Pressed
platform: htb
os: linux
difficulty: hard
tags: [wordpress, web, privesc, xml-rpc, php, kernel-exploit]
solved: 2026-07-09
sources: [[htb-pressed]]
related: []
---
# Pressed
> WordPress box with 2FA that blocks admin login, requiring abuse of XML-RPC to inject a webshell via the PHPEverywhere plugin, then exploiting PwnKit (CVE-2021-4034) for root through the webshell since outbound shells are blocked by firewall.

## Attack path
1. Enumerate [[http]] service with [[nmap]] and [[wpscan]]
2. Leak wp-config.php.bak for database credentials
3. Abuse [[xml-rpc]] to bypass 2FA and edit posts as admin
4. Identify [[webshell-injection]] via PHPEverywhere plugin
5. Exploit [[pwnkit]] (CVE-2021-4034) through webshell for root
6. Modify [[iptables]] to allow reverse shell (Beyond Root)

## Techniques used
- [[config-file-leak]] — wp-config.php.bak exposed database credentials
- [[xml-rpc-abuse]] — Bypassed 2FA by editing posts via XML-RPC API
- [[webshell-injection]] — Injected PHP webshell via PHPEverywhere plugin in WordPress post
- [[pwnkit]] — CVE-2021-4034 local privilege escalation through pkexec
- [[iptables-modification]] — Poked hole in firewall to enable reverse shell (Beyond Root)

## Tools used
- [[nmap]]
- [[wpscan]]
- python-wordpress-xmlrpc
- [[curl]]
- [[bash]]
- [[netcat]]

## Services / ports
- [[http]] (80) — Apache httpd 2.4.41 with WordPress 5.9

## Lessons / notes
- XML-RPC is often enabled in WordPress and can be abused even when 2FA blocks normal login
- PHPEverywhere plugin allows executing PHP code within WordPress posts
- PwnKit (CVE-2021-4034) exploits polkit's pkexec and works even when binary appears patched by version number
- Time-based file swapping can bypass security checks (TOCTOU vulnerability in include)
- Webshell parameter filtering by IP is a stealth technique in shared environments
