---
type: source
title: "HTB Feline writeup"
raw: raw/htb-feline.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[feline]]
---
# Source: HTB Feline writeup
> 0xdf writeup covering Tomcat deserialization, SaltStack exploitation, and Docker socket abuse. Shows the complete attack chain from CVE exploitation to container escape.
## Key facts extracted
- Tomcat 9.0.27 vulnerable to CVE-2020-9484 session deserialization
- SaltStack exposed on localhost with CVE-2020-11651 authentication bypass
- Docker socket mounted in Salt container provides host filesystem access
- ysoserial CommonsCollections2 gadget works reliably for Tomcat exploitation
## Filed into
[[feline]], [[cve-2020-9484]], [[cve-2020-11651]], [[docker-socket-abuse]], [[port-tunneling]]
