---
type: source
title: "HTB PermX writeup"
raw: raw/htb-permx.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[permx]]
---
# Source: HTB PermX writeup
> Chamilo e-learning platform exploitation featuring unauthenticated file upload vulnerability leading to webshell access, credential reuse for user escalation, and ACL abuse through symbolic link manipulation for root access.

## Key facts extracted
- Target: Chamilo 1.11.24 e-learning platform on lms.permx.htb subdomain
- Vulnerability: CVE-2023-4220 unauthenticated file upload in bigUpload.php
- Credentials: Database password "03F6lY3uXAP2bkW8" reused for mtz user
- Privilege escalation: Sudo access to /opt/acl.sh for setfacl manipulation
- Root method: Symlink /etc/passwd modification via crafted ACL script

## Filed into
[[permx]], [[file-upload]], [[password-reuse]], [[acl-abuse]], [[symbolic-link]]
