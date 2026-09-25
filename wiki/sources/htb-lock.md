---
type: source
title: "HTB Lock writeup"
raw: raw/htb-lock.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[lock]]
---

# Source: HTB Lock writeup
> Detailed writeup covering Gitea exploitation from API token leak through CI/CD abuse, mRemoteNG decryption, and CVE-2023-49147 PDF24 repair exploit for SYSTEM access.

## Key facts extracted
- Hardcoded Gitea API token 43ce39bb0bd6bc489284f2905f033ca467a6362f in commit history
- Private website repo with CI/CD auto-deployment on push
- mRemoteNG config.xml contains Gale.Dekarios RDP credentials encrypted with AES/GCM
- PDF24 Creator v11.15.1 vulnerable to CVE-2023-49147 — oplock on faxPrnInst.log during repair
- netexec can execute commands via RDP protocol without full GUI session

## Filed into
[[lock]], [[git-leak]], [[api-token-leak]], [[ci-cd-abuse]], [[web-shell-upload]], [[mremoteng-decrypt]], [[cve-2023-49147]], [[oplock]]
