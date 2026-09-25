---
type: machine
title: Skyfall
platform: htb
os: linux
difficulty: insane
tags: [web, cloud, privesc, linux]
solved: 2026-07-09
sources: [[htb-skyfall]]
related: []
---
# Skyfall
> Insane-difficulty Linux box focused on cloud service enumeration and exploitation, featuring nginx/Flask HTTP parser inconsistency to access MinIO metrics, CVE-2023-28432 for credential leakage, Vault token abuse, and FUSE filesystem manipulation to read root-owned debug files.

## Attack path
1. [[http-parser-inconsistency]] to bypass nginx ACL and access MinIO metrics endpoint
2. [[cve-2023-28432]] to leak MinIO admin credentials from bootstrap endpoint  
3. [[vault-token-abuse]] to get SSH access via OTP key role
4. [[fuse-filesystem]] to intercept root-written debug.log containing Vault master token
5. [[vault-admin-access]] to generate SSH certificate for root login

## Techniques used
- [[http-parser-inconsistency]] — Exploited difference in URL normalization between nginx 1.18.0 and Flask, using 0x0c, 0x0b, 0x09 (tab), or 0x0a (newline) characters to bypass /metrics block
- [[cve-2023-28432]] — POST to /minio/bootstrap/v1/verify exposed MINIO_ROOT_USER and MINIO_ROOT_PASSWORD environment variables in cluster deployment
- [[object-storage-versioning]] — Retrieved previous versions of askyy's home_backup.tar.gz from MinIO to find Vault token in .bashrc
- [[vault-token-abuse]] — Used Vault token with developers policy to access dev_otp_key_role for SSH authentication
- [[fuse-filesystem]] — Abused user_allow_other in /etc/fuse.conf with memfs to capture root-written debug.log in writable FUSE mount
- [[sudo-abuse]] — Executed vault-unseal binary with sudo to generate root-owned debug.log containing master token

## Tools used
- [[nmap]] for port and service discovery
- [[feroxbuster]] for web directory brute forcing
- [[ffuf]] for subdomain fuzzing
- [[mc]] (MinIO Client) for S3-compatible object storage interaction
- [[vault]] CLI for HashiCorp Vault interaction
- [[go]] and [[go-fuse]] memfs example for FUSE filesystem creation
- [[ssh]] and [[vault-ssh]] for SSH access

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 8.9p1 Ubuntu 3ubuntu0.6
- 80/tcp — [[http]] — nginx 1.18.0 (Ubuntu)

## Lessons / notes
- HTTP parser inconsistencies occur when front-end proxy (nginx) and back-end application (Flask) normalize URLs differently — nginx blocks /metrics but Flask strips control characters
- CVE-2023-28432 affects MinIO clusters where environment variables including MINIO_ROOT_PASSWORD are returned in bootstrap endpoint response
- MinIO object versioning allows retrieval of previous file versions even after deletion/overwrites
- Vault tokens can be used for SSH authentication when configured with OTP key roles
- FUSE filesystems with user_allow_other enable non-owners to access mounted files, useful for intercepting root output
- The sys/internal/ui/resultant-acl Vault endpoint reveals all token permissions without needing direct policy access