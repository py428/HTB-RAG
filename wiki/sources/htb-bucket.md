---
type: source
title: "HTB Bucket writeup"
raw: raw/htb-bucket.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[bucket]]
---
# Source: HTB Bucket writeup
> Complete walkthrough of exploiting an AWS-like environment starting with S3 bucket misconfiguration for webshell upload, accessing DynamoDB for credential discovery, and leveraging PDF generation library file read vulnerability to extract SSH keys for root access.

## Key facts extracted
- S3 bucket at s3.bucket.htb allowed anonymous read/write with bogus credentials
- PHP webshell execution worked on .php and .html extensions
- DynamoDB contained user credentials with password "n2vM-<_K_Q:.Aa2" for roy
- pd4ml PDF library attachment feature allowed arbitrary file read via <pd4ml:attachment> tags
- Root SSH key extracted via file read vulnerability in /root/.ssh/ directory
- Localstack simulated AWS services on localhost:4566

## Filed into
[[bucket]], [[s3-misconfiguration]], [[webshell-upload]], [[dynamodb-enumeration]], [[file-read]], [[ssh-key-reuse]]
