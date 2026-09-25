---
type: source
title: "HTB Previous writeup"
raw: raw/htb-previous.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[previous]]
---
# Source: HTB Previous writeup
> Comprehensive guide to exploiting Previous, a Medium NextJS box featuring CVE-2025-29927 middleware bypass, directory traversal, credential reuse, and multiple Terraform-based privilege escalation paths.

## Key facts extracted
- NextJS 15.2.2 on nginx 1.18.0 (Ubuntu 22.04)
- CVE-2025-29927 middleware bypass with x-middleware-subrequest: middleware:middleware:middleware:middleware:middleware
- Download API at /api/download?example= vulnerable to directory traversal
- NextAuth config with hardcoded credential: jeremy/MyNameIsJeremyAndILovePancakes
- Sudo rule: (root) /usr/bin/terraform -chdir=/opt/examples apply
- Terraform provider at /usr/local/go/bin/terraform-provider-examples
- !env_reset in sudo config preserves environment variables
- Multiple privesc paths: malicious provider, TF_VAR for read/write with symlinks

## Filed into
[[previous]], [[nextjs-middleware-bypass]], [[directory-traversal]], [[password-reuse]], [[path-hijack]], [[terraform-provider-abuse]]
