---
type: source
title: "HTB Inject writeup"
raw: raw/htb-inject.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[inject]]
---
# Source: HTB Inject writeup
> Detailed writeup covering file read to source disclosure, Spring Cloud Function SpEL injection (CVE-2022-22963), and Ansible privilege escalation via cron job abuse.

## Key facts extracted
- Spring Cloud Function 3.2.2 vulnerable to SpEL injection via routing expression header
- Maven settings.xml contains hardcoded credentials
- Ansible cron runs with writeable playbooks allowing privilege escalation
- Second-order SQL injection in gallery feed functionality

## Filed into
[[inject]], [[spring-cloud-function-spel]], [[ansible]], [[directory-traversal]], [[file-read]], [[sqli]], [[setuid]]
