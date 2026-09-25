---
type: source
title: "HTB Sink writeup"
raw: raw/htb-sink.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[sink]]
---
# Source: HTB Sink writeup
> Comprehensive writeup covering Sink box exploitation including HTTP request smuggling (CVE-2019-18277) between HAProxy and Gunicorn, AWS LocalStack services abuse (Secrets Manager, KMS), SSH key recovery from Gitea, and Docker container scaling for race conditions.

## Key facts extracted
- HAProxy 1.9.10 and Gunicorn 20.0.0 vulnerable to request smuggling via Transfer-Encoding header with vertical tab (0x0b) character
- AWS LocalStack runs on localhost:4566 with Secrets Manager, KMS, and CloudWatch Logs endpoints
- Gitea contains Key_Management repository with SSH private key in commit history
- Root password stored in KMS-encrypted file servers.enc in david's Projects directory
- Docker scaled to 16 instances with iptables load balancing for concurrent exploitation

## Filed into
[[sink]], [[http-request-smuggling]], [[aws-secrets-manager]], [[aws-kms-decrypt]], [[git-privkey-enum]]