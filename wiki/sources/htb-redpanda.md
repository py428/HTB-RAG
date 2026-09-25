---
type: source
title: "HTB RedPanda writeup"
raw: raw/htb-redpanda.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[redpanda]]
---
# Source: HTB RedPanda writeup
> Detailed writeup of exploiting SSTI in a Spring Boot application for initial access and chaining log injection with XXE to read root's SSH key for privilege escalation on a Linux host.

## Key facts extracted
- Spring Boot application on port 8080 with search feature vulnerable to SSTI
- Character filtering blocks `$`, `_`, `~` but other Thymeleaf expressions work
- Java log parser runs as root every 2 minutes via cron, reading `/opt/panda_search/redpanda.log`
- Log injection allows controlling the URI field parsed by the log parser
- XXE payload in XML file read by root's process to extract `/root/.ssh/id_rsa`
- Root SSH key extracted via XXE and used for SSH access

## Filed into
[[redpanda]], [[ssti]], [[log-injection]], [[xxe]], [[ssh-key-reuse]]
