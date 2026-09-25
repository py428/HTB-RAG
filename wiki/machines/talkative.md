---
type: machine
title: Talkative
platform: htb
os: linux
difficulty: hard
tags: [linux, web, docker, rce, php, javascript, mongodb, container-escape]
solved: 2026-07-09
sources: [[htb-talkative]]
related: []
---
# Talkative
> Hard Linux box running communications platform with multiple Docker containers. Chain through Jamovi R script execution, Bolt CMS template injection, MongoDB manipulation for Rocket Chat admin, then Docker container escape via CAP_DAC_READ_SEARCH capability abuse.

## Attack path
1. [[r-code-execution]] — Execute system commands via Jamovi built-in R editor
2. [[password-extraction]] — Extract Bolt CMS credentials from jamovi .omv document
3. [[template-injection]] — Inject malicious Twig template in Bolt CMS for RCE
4. [[docker-pivot]] — Pivot through containers to find MongoDB on 172.17.0.2
5. [[mongodb-privilege-escalation]] — Modify Rocket Chat user roles to admin
6. [[webhook-rce]] — Create malicious Rocket Chat webhook for JavaScript reverse shell
7. [[container-capability-abuse]] — Exploit CAP_DAC_READ_SEARCH to read/write host files

## Techniques used
- [[r-code-execution]] — Jamovi Rj editor allows arbitrary R code execution with system() calls
- [[zip-archive-extraction]] — Extract credentials from jamovi .omv (zip) documents
- [[template-injection]] — Twig SSTI payload: {{_self.env.display("id")}}
- [[mongodb-privilege-escalation]] — Update user roles array to ["admin"] in MongoDB
- [[javascript-reverse-shell]] — Node.js reverse shell via Rocket Chat webhook
- [[docker-capability-abuse]] — Shocker exploit abuses CAP_DAC_READ_SEARCH

## Tools used
[[nmap]], [[feroxbuster]], [[nc]], [[mongo]], [[chisel]], [[gcc]]

## Services / ports
[[ssh]] (22), [[http]] (80), tcp/3000 (Rocket Chat), tcp/8080 (Jamovi), tcp/27017 (MongoDB)

## Lessons / notes
- Jamovi R editor executes R code with system() for shell commands
- .omv files are zip archives containing JSON with credential data
- Twig template injection works via cached template files in Bolt CMS
- MongoDB Rocket Chat stores users in meteor database with roles array
- Shocker exploit abuses file descriptors to bypass container boundaries
- CAP_DAC_READ_SEARCH allows reading arbitrary host files from container