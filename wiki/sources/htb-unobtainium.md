---
type: source
title: "HTB Unobtainium writeup"
raw: raw/htb-unobtainium.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[unobtainium]]
---
# Source: HTB Unobtainium writeup
> Comprehensive writeup for HTB Unobtainium covering Electron app reverse engineering, prototype pollution, npm package command injection, Kubernetes token abuse, and container escape through malicious pod creation.

## Key facts extracted
- Electron chat application vulnerable to LFI and prototype pollution
- Vulnerable `google-cloudstorage-commands` npm package allows command injection
- Kubernetes cluster with exposed API server and service account tokens
- Multiple containerized applications running on the host
- Container escape via host filesystem mount in malicious pod

## Filed into
[[unobtainium]], [[local-file-include]], [[prototype-pollution]], [[command-injection]], [[kubernetes-token-abuse]], [[container-escape]]
