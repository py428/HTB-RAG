---
type: machine
title: RedPanda
platform: htb
os: linux
difficulty: easy
tags: [linux, web, java, ssti, xxe, privesc]
solved: 2026-07-09
sources: [[htb-redpanda]]
related: []
---
# RedPanda
> Linux box featuring a Spring Boot search application vulnerable to SSTI for initial foothold, and a log parsing Java application abused via log injection and XXE to read root's SSH key for privilege escalation.

## Attack path
1. [[ssti]] — Server-Side Template Injection in Spring Boot search to gain shell as woodenk
2. [[log-injection]] — Inject malicious log entry pointing to crafted image
3. [[xxe]] — XML External Entity via crafted JPG metadata and XML file to read root's SSH key as root
4. [[ssh-key-reuse]] — SSH as root using extracted private key

## Techniques used
- [[ssti]] — SSTI in Spring Boot Thymeleaf templates using `*{T(java.lang.Runtime).getRuntime().exec(...)` payload bypassing character filters
- [[log-injection]] — Injected log entries into `/opt/panda_search/redpanda.log` writable by logs group to control URI parsed by Java application
- [[xxe]] — XML External Entity injection via crafted XML file with `<!ENTITY foo SYSTEM 'file:///root/.ssh/id_rsa'>` parsed by root's Java cron job
- [[ssh-key-reuse]] — Extracted root's SSH private key from XXE output and used to SSH as root

## Tools used
- [[nmap]] — Port scanning
- feroxbuster — Directory brute forcing
- wfuzz — Fuzzing SSTI character filters
- [[exiftool]] — Reading and modifying JPG Artist metadata
- ssh, curl, nc — Shell access and file transfer

## Services / ports
- [[ssh]] (22)
- [[http]] (8080) — Spring Boot application

## Lessons / notes
- SSTI bypass: Spring blocks `$`, `_`, `~` but other expression prefixes work (`*{}`, `@{}`, `#{}`)
- Log injection abuse: Java application parsed logs in format `status||ip||user-agent||uri` to track image views, allowing URI control via User-Agent manipulation
- XXE via metadata: Combined directory traversal in JPG Artist field (`../tmp/0xdf`) with XXE in XML to read arbitrary files as root
- Group permissions: Reverse shell from webapp inherited logs group, allowing log file write; SSH shell did not have this group
- Cleanup script: `/opt/cleanup.sh` ran every 5 minutes to delete .xml and .jpg files from temp directories
