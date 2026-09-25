---
type: source
title: "HTB Ready writeup"
raw: raw/htb-ready.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[ready]]
---
# Source: HTB Ready writeup
> GitLab exploitation guide combining SSRF and CRLF injection vulnerabilities to achieve Redis RCE, followed by multiple Docker container escape techniques including cgroups attack and host filesystem mounting for full system compromise.

## Key facts extracted
- GitLab 11.4.7 vulnerable to CVE-2018-19571 (SSRF) and CVE-2018-19585 (CRLF injection)
- IPv6 localhost [0:0:0:0:0:ffff:127.0.0.1] bypasses 127.0.0.1 blocking
- Redis accessible via git:// protocol on localhost with command injection via CRLF
- Container runs with privileged: true flag enabling full host access
- cgroups release_agent technique executes commands on host system
- Host filesystem directly mountable from privileged container
- GitLab root password stored in gitlab.rb configuration file

## Filed into
[[ready]], [[ssrf]], [[crlf-injection]], [[redis-rce]], [[privileged-container-escape]], [[cgroups-escape]], [[gitlab]], [[docker]], [[redis]]