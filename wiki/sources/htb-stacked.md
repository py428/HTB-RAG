---
type: source
title: "HTB Stacked writeup"
raw: raw/htb-stacked.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[stacked]]
---
# Source: HTB Stacked writeup
> Detailed writeup covering XSS exploitation via Referer header, LocalStack enumeration, CVE-2021-32090 command injection in Lambda function names, and Docker container escape for privilege escalation.
## Key facts extracted
- Contact form vulnerable to Referer-based XSS
- Internal mail application at `mail.stacked.htb` (localhost only)
- Selenium automation views emails, executing XSS payloads
- LocalStack instance at `s3-testing.stacked.htb` provides Lambda service
- CVE-2021-32090: command injection in Lambda function names when displayed on dashboard
- Lambda handler parameter injection point for command execution
- Docker socket accessible from LocalStack container

## Filed into
[[stacked]], [[xss-referer]], [[subdomain-enumeration]], [[mailbox-enumeration]], [[aws-lambda-enumeration]], [[cve-2021-32090]], [[docker-container-escape]]
