---
type: source
title: "HTB Bitlab writeup"
raw: raw/htb-bitlab.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[bitlab]]
---
# Source: HTB Bitlab writeup
> Complete walkthrough of Bitlab machine exploitation covering GitLab credential extraction, webshell deployment via CI/CD abuse, PostgreSQL tunneling and credential extraction, and binary reverse engineering for root access.

## Key facts extracted
- GitLab credentials stored in obfuscated JavaScript bookmark on /help page
- Webhook automation deploys code from Profile repo on merge to master branch
- PostgreSQL credentials found in GitLab snippets (profiles/profiles)
- SSH credentials for clave user stored in PostgreSQL profiles table
- RemoteConnection.exe Windows binary contains Putty connection string with root credentials
- Docker container environment with separate containers for GitLab, PostgreSQL, and application

## Filed into
[[bitlab]], [[javascript-deobfuscation]], [[web-shell]], [[git-webhook-abuse]], [[tunneling]], [[database-extraction]], [[binary-reverse-engineering]]
