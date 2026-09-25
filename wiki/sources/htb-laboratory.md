---
type: source
title: "HTB Laboratory writeup"
raw: raw/htb-laboratory.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[laboratory]]
---
# Source: HTB Laboratory writeup
> Complete guide to exploiting Laboratory, an easy HTB box centered on GitLab vulnerabilities. Covers CVE-2020-10977 arbitrary file read, Rails deserialization RCE, GitLab admin access techniques, and SUID binary PATH hijacking for privilege escalation.

## Key facts extracted
- **GitLab vulnerability**: Version 12.8.1 vulnerable to arbitrary file read via issue markdown image reference and move
- **Rails RCE**: Secret key base from /opt/gitlab/embedded/service/gitlab-rails/config/secrets.yml enables deserialization
- **Docker setup**: Local GitLab Docker container used to generate malicious Rails cookie payload
- **Admin access**: Can either reset dexter's password or elevate own user to admin via Rails console
- **Private repo**: Contains SSH private key for user dexter
- **Privesc**: /usr/local/bin/docker-security SUID binary calls system("chmod ...") without full path

## Filed into
[[laboratory]], [[gitlab-arbitrary-file-read]], [[rails-deserialization]], [[git-admin-privileges]], [[suid-path-hijacking]]