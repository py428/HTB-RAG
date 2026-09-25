---
type: source
title: "HTB MonitorsThree writeup"
raw: raw/htb-monitorsthree.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[monitorsthree]]
---
# Source: HTB MonitorsThree writeup

> Complete exploitation chain from SQL injection in password reset to Duplicati backup tool abuse for root access on Cacti monitoring server.

## Key facts extracted

- Boolean-based blind SQL injection in forgot password form (username parameter)
- Cacti 1.2.26 with CVE-2024-25642 arbitrary file upload via package import
- Duplicati backup solution running in Docker with host filesystem mounted
- Duplicati server passphrase stored in SQLite database for authentication bypass
- Multiple root paths: backup `/root`, write SSH key via backup/restore, container escape

## Filed into

[[monitorsthree]], [[sqli-blind]], [[hash-cracking]], [[file-upload]], [[backup-tool-abuse]], [[docker-mount]]
