---
type: source
title: "HTB Facts writeup"
raw: raw/htb-facts.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[facts]]
---
# Source: HTB Facts writeup
> Ruby on Rails Camaleon CMS exploitation with MinIO S3 access and facter privilege escalation.

## Key facts extracted
- Camaleon CMS 2.9.0 mass assignment via updated_ajax permit! method
- MinIO S3 credentials leaked in admin panel: AKIA3ADAF4DE0BB0FAA2
- Encrypted SSH key cracked: dragonballz
- Facter custom directory loads arbitrary Ruby as root
- Alternative: CVE-2024-46987 path traversal in S3 uploader

## Filed into
[[facts]], [[mass-assignment]], [[s3-enum]], [[ssh-key-crack]], [[facter-custom-dir]]