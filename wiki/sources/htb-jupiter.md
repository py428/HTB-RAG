---
type: source
title: "HTB Jupiter writeup"
raw: raw/htb-jupiter.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[jupiter]]
---
# Source: HTB Jupiter writeup
> Detailed 0xdf writeup covering Grafana SQL injection to PostgreSQL RCE, Shadow Simulator exploitation for user pivot, and Jupyter Notebook access for privilege escalation to root.

## Key facts extracted
- Ubuntu 22.04 with Grafana dashboard accessible via kiosk.jupiter.htb subdomain
- PostgreSQL RCE via Grafana's raw SQL query feature using COPY FROM PROGRAM
- Shadow Simulator config file in /dev/shm modified for SetUID binary creation
- Jupyter Notebook running as jovian with token logged in /opt/solar-flares/logs/
- Sattrack binary abuse via file:// protocol handler to read root.txt

## Filed into
[[jupiter]], [[sql-injection]], [[postgresql-copy-from-program]], [[setuid]], [[jupyter-rce]], [[sudo-abuse]]
