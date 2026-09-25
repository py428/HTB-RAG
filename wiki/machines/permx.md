---
type: machine
title: "HTB PermX"
platform: htb
os: linux
difficulty: easy
tags: [web, linux, privesc]
solved: 2026-07-09
sources: [[htb-permx]]
related: []
---
# HTB PermX
> Chamilo e-learning platform with unauthenticated file upload vulnerability leading to webshell, followed by credential reuse and ACL abuse via symbolic links for privilege escalation.

## Attack path
1. Enumerate subdomains with [[ffuf]] to find lms.permx.htb
2. Identify Chamilo 1.11.24 with [[file-upload]] vulnerability (CVE-2023-4220)
3. Upload PHP webshell to get initial shell as www-data
4. Extract database credentials from configuration file
5. Reuse database password to access mtz user via [[su]]/[[ssh]]
6. Abuse [[acl-abuse]] through [[symbolic-link]] manipulation of /etc/passwd to create root user

## Techniques used
- [[file-upload]] — Unauthenticated PHP upload via bigUpload.php in Chamilo plugin
- [[password-reuse]] — Database password reused for user authentication
- [[acl-abuse]] — Abuse setfacl script using symlinks to modify system files
- [[symbolic-link]] — Create symlinks in /home/mtz to point to /etc/passwd for ACL modification

## Tools used
- [[nmap]] — Port scanning identifying HTTP and SSH
- [[ffuf]] — Subdomain fuzzing with Host header injection
- [[curl]] — Webshell interaction and file upload testing
- [[hashcat]] — Not used but available for cracking

## Services / ports
- [[ssh]] (22) — OpenSSH 8.9p1 Ubuntu 3ubuntu0.10
- [[http]] (80) — Apache 2.4.52 with permx.htb redirect
- [[http]] (lms.permx.htb) — Chamilo 1.11.24 e-learning platform

## Lessons / notes
- Chamilo bigUpload.php allows unauthenticated file upload with controlled filename
- ACL scripts can be abused using symlinks when path validation doesn't follow links
- /etc/passwd modification requires both write ACL and execute permission on parent directories
- SetUID bit is automatically removed when files are modified by non-owners
