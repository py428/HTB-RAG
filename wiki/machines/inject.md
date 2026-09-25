---
type: machine
title: Inject
platform: htb
os: linux
difficulty: easy
tags: [web, sqli, java, spring, ansible, privesc]
solved: 2026-07-09
sources: [[htb-inject]]
related: []
---
# Inject
> Inject is a Linux box featuring a file read vulnerability that exposes source code for a Spring Cloud Function application, which is vulnerable to SpEL injection leading to code execution. Privilege escalation abuses an Ansible cron job with writeable playbooks.

## Attack path
1. [[directory-traversal]] via `/show_image?img=` parameter to read file system
2. [[file-read]] to leak Maven `pom.xml` and source code
3. Identify [[spring-cloud-function-spel]] via dependency version enumeration
4. Exploit SpEL injection for [[rce]] using brace expansion payload
5. Find credentials in [[maven]] `settings.xml` for lateral movement
6. Privilege escalation via [[ansible]] cron job with writeable playbooks in `/opt/automation/tasks/`

## Techniques used
- [[directory-traversal]] — Path traversal in image view parameter
- [[file-read]] — Source code disclosure via directory traversal
- [[spring-cloud-function-spel]] — CVE-2022-22963 in spring-cloud-function-web 3.2.2
- [[sqli]] — Second-order SQL injection in gallery feed
- [[ansible]] — Cron job executes playbooks from group-writable directory
- [[setuid]] — SetUID binary creation via Ansible shell module

## Tools used
- [[nmap]], [[feroxbuster]], [[exiftool]], [[curl]], [[python]], [[pspy]], [[john]]

## Services / ports
- 22/tcp — [[ssh]]
- 8080/tcp — [[http]] (Tomcat/Spring Boot)

## Lessons / notes
- Second-order SQL injection requires testing injection storage and retrieval separately
- Spring Cloud Function SpEL injection requires special payload formatting (brace expansion)
- Maven settings.xml often contains credentials for repository authentication
- Ansible cron jobs can be abused when task directories are writable by low-privilege users
