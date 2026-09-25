---
type: machine
title: Stacked
platform: htb
os: linux
difficulty: insane
tags: [xss, aws, docker, container, insane, linux, web]
solved: 2026-07-09
sources: [[htb-stacked]]
related: []
---
# Stacked
> Insane difficulty Linux box featuring LocalStack AWS simulation environment. Initial foothold through XSS in Referer header to automate browser interaction, leading to discovery of LocalStack dashboard. Exploit CVE-2021-32090 (command injection in Lambda function names) for initial container access, then escape via Docker socket to compromise host.
## Attack path
1. [[xss-referer]] — inject XSS payload via Referer header in contact form
2. [[subdomain-enumeration]] — discover `dev.stocker.htb` via ffuf
3. [[mailbox-enumeration]] — use XSS to read internal mail application
4. [[aws-lambda-enumeration]] — discover LocalStack instance via leaked email
5. [[cve-2021-32090]] — command injection in Lambda function names
6. [[docker-container-escape]] — mount host filesystem via Docker socket

## Techniques used
- [[xss-referer]] — XSS via HTTP Referer header in form submission
- [[subdomain-enumeration]] — virtual host discovery with ffuf
- [[mailbox-enumeration]] — XSS to enumerate internal mail app
- [[aws-lambda-enumeration]] — interact with LocalStack Lambda service
- [[cve-2021-32090]] — LocalStack Lambda function name command injection
- [[docker-container-escape]] — escape container via Docker socket abuse

## Tools used
- [[nmap]] — port scanning
- ffuf — subdomain fuzzing
- feroxbuster — directory brute force
- awscli — AWS Lambda interaction
- awslocal — LocalStack CLI wrapper
- [[curl]] — HTTP requests and file transfer
- [[nc]] — reverse shell listener
- docker — container management for escape

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 8.2p1 Ubuntu
- 80/tcp — [[http]] — Apache 2.4.41
- 2376/tcp — Docker daemon (TLS)

## Lessons / notes
- XSS in Referer headers can automate interaction with internal applications
- LocalStack provides AWS service simulation (Lambda, S3, etc.)
- CVE-2021-32090: command injection in LocalStack Lambda function names displayed on dashboard
- Lambda handler parameter vulnerable to command injection: `--handler 'index.handler;$(command)'`
- Docker socket access allows container escape and host compromise
- Selenium automation can be exploited for XSS delivery
