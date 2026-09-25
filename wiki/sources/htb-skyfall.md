---
type: source
title: "HTB Skyfall writeup"
raw: raw/htb-skyfall.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[skyfall]]
---
# Source: HTB Skyfall writeup
> Comprehensive exploitation guide covering nginx/Flask parser inconsistency for ACL bypass, MinIO CVE-2023-28432 credential exposure, object versioning for Vault token recovery, Vault SSH OTP authentication, and FUSE filesystem abuse to capture root-written log files.

## Key facts extracted
- nginx 1.18.0 front-end with Flask back-end on demo.skyfall.htb for MinIO storage interface
- MinIO cluster vulnerable to CVE-2023-28432 exposing admin credentials at /minio/bootstrap/v1/verify
- Vault token stored in askyy's .bashrc file in previous version of home backup on MinIO
- Vault admin token leaked by vault-unseal debug log when run via sudo by unprivileged user
- FUSE configuration with user_allow_other enabled creation of accessible filesystems

## Filed into
[[skyfall]], [[http-parser-inconsistency]], [[cve-2023-28432]], [[object-storage-versioning]], [[vault-token-abuse]], [[fuse-filesystem]]