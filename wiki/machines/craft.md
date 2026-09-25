---
type: machine
title: Craft
platform: htb
os: linux
difficulty: medium
tags: [web, linux, docker, git, python-eval, rce, vault, otp, container-escape]
solved: 2026-07-09
sources: [[htb-craft]]
related: []
---
# Craft
> Beer company website with Gogs Git service, Python eval vulnerability in API allowing code execution, Docker container breakout, and Vault SSH OTP for root access.
## Attack path
1. [[subdomain-enumeration]] — discover multiple subdomains via fuzzing
2. [[git-repository-analysis]] — explore Gogs instance, find credentials in commit history
3. [[python-eval-code-injection]] — abuse `eval()` in API brew endpoint for RCE
4. [[container-escape]] — pivot from container to host via SSH keys
5. [[vault-ssh-otp]] — abuse Vault SSH OTP to get root shell
## Techniques used
- [[subdomain-enumeration]] — found api.craft.htb, gogs.craft.htb, vault.craft.htb via wfuzz
- [[git-repository-analysis]] — found API credentials in Gogs commit history
- [[python-eval-code-injection]] — injected `__import__('os').system()` into eval statement
- [[container-escape]] — extracted SSH keys from database, used to access host
- [[vault-ssh-otp]] — used Vault SSH OTP functionality for root access
## Tools used
- [[nmap]], gobuster, wfuzz, [[curl]], nc, python
## Services / ports
- SSH (22, 6022), HTTPS (443), DNS (53)
## Lessons / notes
- Git commit history may contain credentials that were later removed
- Python eval statements are extremely dangerous when user input is involved
- Container environments often have different attack surfaces than hosts
- Vault SSH OTP can provide one-time passwords for root access
- Multiple SSH ports suggest containerized environments