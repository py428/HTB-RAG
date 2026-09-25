---
type: source
title: "HTB Monitors writeup"
raw: raw/htb-monitors.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[monitors]]
---
# Source: HTB Monitors writeup

> Complex multi-stage exploitation chain from WordPress LFI through Cacti SQLi to Docker container escape via kernel module loading in privileged container.

## Key facts extracted

- WordPress with wp-with-spritz plugin vulnerable to unauthenticated LFI
- Cacti monitoring application with SQL injection vulnerabilities (CVE-2020-14295/35701)
- Docker environment with Apache Solr running in privileged container
- Apache OFBiz with CVE-2020-9496 Java deserialization vulnerability
- Privileged Docker container with CAP_SYS_MODULE capability for host kernel access

## Filed into

[[monitors]], [[wordpress-lfi]], [[sql-injection]], [[deserialization]], [[container-escape]], [[kernel-module-loading]]
