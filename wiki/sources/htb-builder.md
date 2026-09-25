---
type: source
title: "HTB Builder writeup"
raw: raw/htb-builder.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[builder]]
---
# Source: HTB Builder writeup
> Comprehensive analysis of exploiting CVE-2024-23897 in Jenkins CLI for file read, cracking Jenkins user bcrypt hash, and recovering SSH keys through Jenkins credential storage or SSH agent plugin for root access.

## Key facts extracted
- CVE-2024-23897 allows arbitrary file read through Jenkins CLI using @/filepath syntax
- Different CLI commands return varying amounts of data (reload-node gave 19 lines)
- Jennifer's bcrypt hash cracked to "princess" with hashcat mode 3200
- Root SSH key stored in Jenkins credential store for deployment automation
- SSH agent plugin allowed command execution with stored credentials
- Multiple methods available to recover SSH keys: Groovy script console, SSH agent, or credential dump

## Filed into
[[builder]], [[jenkins-cli-file-read]], [[hash-cracking]], [[ssh-key-recovery]]
