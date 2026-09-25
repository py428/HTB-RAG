---
type: machine
title: Previous
platform: htb
os: linux
difficulty: medium
tags: [nextjs, web, privesc, terraform, sudo, auth-bypass]
solved: 2026-07-09
sources: [[htb-previous]]
related: []
---
# Previous
> NextJS application with middleware authentication bypass via CVE-2025-29927, leading to directory traversal, hardcoded credentials in NextAuth config, password reuse for SSH, and Terraform misconfiguration abuse for root.

## Attack path
1. Enumerate [[http]] (80) with [[nmap]] and [[feroxbuster]]
2. Exploit NextJS middleware bypass (CVE-2025-29927) with x-middleware-subrequest header
3. Use directory traversal in download API to read application files
4. Extract hardcoded password from NextAuth config
5. Login via [[ssh]] with reused credentials
6. Abuse [[terraform]] sudo rule with [[path-hijack]] to get root

## Techniques used
- [[nextjs-middleware-bypass]] — CVE-2025-29927 auth bypass via x-middleware-subrequest header
- [[directory-traversal]] — Read arbitrary files including .env and NextAuth config
- [[password-reuse]] — Hardcoded NextAuth password worked for SSH user jeremy
- [[path-hijack]] — Modified .terraformrc to point terraform provider to malicious binary
- [[terraform-provider-abuse]] — Created malicious terraform-provider-examples binary for privesc

## Tools used
- [[nmap]]
- [[feroxbuster]]
- [[netexec]]
- [[sshpass]]
- terraform
- ssh-keygen

## Services / ports
- [[http]] (80) — nginx 1.18.0 with NextJS 15.2.2
- [[ssh]] (22) — OpenSSH 8.9p1

## Lessons / notes
- NextJS middleware bypass requires multiple "middleware:" values in x-middleware-subrequest header
- NextJS stores build manifest and routes in _next/static for enumeration
- NextAuth config files may contain hardcoded credentials
- Terraform provider_installation dev_overrides in .terraformrc can redirect to arbitrary binaries
- Sudo with !env_reset preserves environment variables including $HOME and $PATH
- TF_VAR_ environment variables can override terraform variable defaults even with validation
- Symbolic links can bypass path validation in terraform configurations
