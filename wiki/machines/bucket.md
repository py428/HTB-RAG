---
type: machine
title: Bucket
platform: htb
os: linux
difficulty: medium
tags: [linux, aws, s3, webshell, dynamodb, file-read, privesc]
solved: 2026-07-09
sources: [[htb-bucket]]
related: []
---
# Bucket
> Linux box simulating an Amazon AWS stack with S3 bucket hosting and DynamoDB database. Initial foothold through S3 bucket misconfiguration allowing unauthenticated file upload leading to webshell deployment. User access via password reuse from DynamoDB credentials. Privilege escalation through PDF generation library file read vulnerability to extract SSH keys and gain root access.

## Attack path
1. [[s3-misconfiguration]] — Upload webshell to misconfigured S3 bucket via awscli
2. [[webshell-upload]] — Deploy PHP webshell to get www-data shell
3. [[dynamodb-enumeration]] — Access DynamoDB via awscli to find credentials
4. [[password-reuse]] — Reuse DynamoDB password for SSH access as roy
5. [[file-read]] — Exploit pd4ml attachment feature to read arbitrary files
6. [[ssh-key-reuse]] — Extract SSH private key via file read for root access

## Techniques used
- [[s3-misconfiguration]] — Anonymous read/write access to S3 bucket for webshell upload
- [[webshell-upload]] — PHP webshell uploaded via S3 to get initial foothold
- [[dynamodb-enumeration]] — Unauthenticated DynamoDB access to extract user credentials
- [[password-reuse]] — DynamoDB password "n2vM-<_K_Q:.Aa2" reused for roy SSH access
- [[file-read]] — pd4ml PDF library attachment feature for arbitrary file read
- [[ssh-key-reuse]] — Root SSH key extracted via file read vulnerability

## Tools used
[[nmap]], [[gobuster]], [[curl]], awscli, [[netcat]], [[crackmapexec]], sshpass, python, pdfdetach, xpdf

## Services / ports
[[ssh]] (22), [[http]] (80 - Apache), local services on localhost:8000, localhost:4566 (localstack)

## Lessons / notes
- S3 bucket allowed anonymous read/write with bogus AWS credentials
- PHP execution enabled on .php and .html files uploaded via S3
- DynamoDB accessible without authentication from both local and remote
- Apache config showed S3 (s3.bucket.htb) proxied to localstack on port 4566
- pd4ml library attachment feature enabled reading arbitrary files as PDF attachments
- Root SSH key found in /root/.ssh/ directory via file read vulnerability
- Localstack used to simulate AWS services within HTB environment
