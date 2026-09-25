---
type: source
title: "HTB Craft writeup"
raw: raw/htb-craft.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[craft]]
---
# Source: HTB Craft writeup
> Beer company website with Gogs Git service containing Python API vulnerable to eval code injection. Initial access through containerized API, then pivoting to host via SSH keys from database. Root access through Vault SSH OTP functionality.
## Key facts extracted
- Multiple subdomains: api.craft.htb, gogs.craft.htb, vault.craft.htb
- Gogs Git service exposed with repository containing API source code
- API credentials found in git commit history (dinesh:4aUh0A8PbVJxgd)
- Python eval vulnerability in brew endpoint accepting ABV values
- Database credentials in settings.py for MySQL connection
- SSH keys stored in database for container-to-host pivot
- Vault SSH OTP enabled for root access with role `root_otp`
## Filed into
[[craft]], [[subdomain-enumeration]], [[git-repository-analysis]], [[python-eval-code-injection]], [[container-escape]], [[vault-ssh-otp]]