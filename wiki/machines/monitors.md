---
type: machine
title: Monitors
platform: htb
os: linux
difficulty: hard
tags: [wordpress, cacti, docker, rce, privesc, kernel]
solved: 2026-07-09
sources: [[htb-monitors]]
related: []
---
# Monitors

> Linux host with WordPress and Cacti, requiring LFI discovery, SQL injection, Docker containerization, Apache OFBiz deserialization, and kernel module exploitation for full chain.

## Attack path

1. [[wordpress-enumeration]] — identify wp-with-spritz plugin via [[wpscan]]
2. [[lfi]] — exploit unauthenticated file inclusion in plugin to read `/etc/passwd` and Apache configs
3. [[virtual-host-discovery]] — discover `cacti-admin.monitors.htb` from Apache vhost configs
4. [[sql-injection]] — exploit CVE-2020-14295/CVE-2020-35701 in Cacti for RCE
5. [[docker-enumeration]] — identify Docker environment with Apache Solr in container
6. [[deserialization]] — exploit CVE-2020-9496 in Apache OFBiz via XML-RPC
7. [[container-escape]] — abuse privileged container with CAP_SYS_MODULE to load malicious kernel module

## Techniques used

- [[wordpress-lfi]] — WP with Spritz plugin 1.0 unauthenticated file inclusion via `wp.spritz.content.filter.php?url=`
- [[sql-injection]] — CVE-2020-14295: Stacked queries in `color.php` for Cacti RCE
- [[deserialization]] — CVE-2020-9496: Apache OFBiz XML-RPC Java deserialization via ysoserial
- [[container-escape]] — CAP_SYS_MODULE in privileged Docker container allows loading kernel modules on host

## Tools used

- [[nmap]], [[wpscan]], [[curl]], [[python]], [[ysoserial]], [[feroxbuster]]

## Services / ports

- 22/tcp — [[ssh]] — OpenSSH 7.6
- 80/tcp — [[http]] — Apache 2.4.29 (WordPress + Cacti)

## Lessons / notes

- LFI found via WPScan enumeration, used to discover Apache virtual host configurations
- Cacti SQLi requires database query stacking: `UNION SELECT;UPDATE settings SET value='cmd'`
- Apache OFBiz vulnerable via `/webtools/control/xmlrpc` with CommonsBeanutils1 gadget chain
- Privileged Docker containers share host kernel, allowing kernel module loading for host escape
