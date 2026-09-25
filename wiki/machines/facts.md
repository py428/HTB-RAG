---
type: machine
title: Facts
platform: htb
os: linux
difficulty: easy
tags: [linux, web, ruby-on-rails, minio, sudo, ruby]
solved: 2026-07-09
sources: [[htb-facts]]
related: []
---
# Facts
> Ruby on Rails Camaleon CMS with mass assignment vulnerability, MinIO S3 service, and facter privilege escalation.

## Attack path
1. [[mass-assignment]] to promote user to admin in Camaleon CMS
2. MinIO credentials from admin panel for [[s3-enum]]
3. Encrypted SSH key from S3 bucket, [[ssh-key-crack]] with john
4. [[facter-custom-dir]] — Load arbitrary Ruby code as root via custom facts directory

## Techniques used
- [[mass-assignment]] — CVE-2025-2304 in Camaleon CMS permit! vulnerability
- [[s3-enum]] — AWS CLI to enumerate MinIO buckets and extract SSH key
- [[ssh-key-crack]] — John the Ripper to crack encrypted SSH private key
- [[facter-custom-dir]] — Facter loads custom Ruby code from arbitrary directory

## Tools used
- [[nmap]], [[feroxbuster]], [[awscli]], [[john]], [[ssh-keygen]]

## Services / ports
- [[ssh]] (22), [[http]] (80, 54321 - MinIO S3)

## Lessons / notes
- Ruby permit! is dangerous — allows mass assignment without parameter filtering
- MinIO provides S3-compatible API locally; AWS CLI works with endpoint URL
- Puppet facter can load arbitrary Ruby code from custom directories
- Encrypted SSH keys can be cracked with john/ssh2john.py
- Alternative path: CVE-2024-46987 path traversal in Camaleon S3 uploader

## CVEs
- CVE-2025-2304 (Camaleon mass assignment)
- CVE-2024-46987 (Camaleon path traversal)
- CVE-2026-1776 (Camaleon S3 uploader path traversal)