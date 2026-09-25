---
type: machine
title: Interface
platform: htb
os: linux
difficulty: medium
tags: [web, php, linux, privesc]
solved: 2026-07-09
sources: [[htb-interface]]
related: []
---
# Interface
> Interface is a medium Linux box featuring a web application with an API that converts HTML to PDF using DomPDF. The exploitation path involves discovering the API endpoint, exploiting a DomPDF vulnerability to achieve RCE via font poisoning, and then leveraging a cleanup script with arithmetic expression injection for privilege escalation.

## Attack path
1. [[subdomain-enumeration]] to discover prd.m.rendering-api.interface.htb
2. [[directory-enumeration]] to find /api/html2pdf endpoint
3. [[dompdf-rce]] (CVE-2022-28368) to poison font cache and inject PHP webshell
4. [[arithmetic-expression-injection]] in cleancache.sh script via exiftool metadata for privesc

## Techniques used
- [[dompdf-rce]] — Exploiting DomPDF 1.2.0 font caching to inject PHP webshell
- [[arithmetic-expression-injection]] — Abusing bash [[ expression syntax in cleancache.sh
- [[subdomain-enumeration]] — Using ffuf to discover rendering-api subdomain
- [[directory-enumeration]] — Finding API endpoints with feroxbuster and ffuf

## Tools used
- [[nmap]] — Initial port scanning and service detection
- [[feroxbuster]] — Directory brute forcing on web endpoints
- ffuf — Subdomain and API fuzzing with filtering
- exiftool — Injecting malicious metadata for privesc
- tcpdump — Verifying RCE with ICMP ping tests
- netcat — Shell handling and reverse connections
- [[pspy]] — Monitoring cron jobs and processes

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 7.6p1 Ubuntu
- 80/tcp — [[http]] — nginx 1.14.0 / Next.js application
- API endpoint — /api/html2pdf (DomPDF conversion service)

## Lessons / notes
- DomPDF font caching vulnerability allows arbitrary PHP code execution by poisoning font files
- Bash arithmetic expression injection with `[[ "$VAR" -eq "value" ]]` syntax can execute commands
- Using `${IFS}` as space replacement bypasses filters in injection attacks
- Different 404 response sizes can indicate valid endpoints during fuzzing
- Cleanup scripts running as root often present privilege escalation opportunities