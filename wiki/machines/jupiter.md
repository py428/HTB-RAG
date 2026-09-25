---
type: machine
title: Jupiter
platform: htb
os: linux
difficulty: medium
tags: [linux, web, database, privesc]
solved: 2026-07-09
sources: [[htb-jupiter]]
related: []
---
# Jupiter
> Ubuntu 22.04 box featuring a Grafana dashboard with PostgreSQL SQL injection, leading to RCE and multiple privilege escalation paths through Shadow Simulator and Jupyter Notebook.

## Attack path
1. [[sql-injection]] via Grafana PostgreSQL plugin → [[postgresql-copy-from-program]] RCE as postgres
2. [[setuid]] abuse via Shadow Simulator config file → shell as juno
3. [[jupyter-rce]] via accessible notebook token in logs → shell as jovian
4. [[sudo-abuse]] of sattrack with file:// protocol to read root.txt

## Techniques used
- [[sql-injection]] — Raw SQL execution through Grafana's PostgreSQL data source plugin
- [[postgresql-copy-from-program]] — PostgreSQL command execution via COPY FROM PROGRAM feature
- [[setuid]] — Shadow Simulator config modification to create SetUID binary
- [[jupyter-rce]] — Code execution through Jupyter Notebook with token from log files
- [[sudo-abuse]] — Sattrack configuration abuse using file:// URI scheme

## Tools used
[[nmap]], [[ffuf]], [[feroxbuster]], [[curl]], [[ssh]], Python HTTP server, pspy, Jupyter Notebook, strace

## Services / ports
- 22/tcp — [[ssh]] (OpenSSH 8.9)
- 80/tcp — [[http]] (nginx 1.18)
- 5432/tcp — PostgreSQL (localhost only)
- 8888/tcp — Jupyter Notebook (localhost only)

## Lessons / notes
- Grafana's raw SQL feature is dangerous when exposed (CVE-2019-9193)
- Shadow Simulator config files in /dev/shm can be modified for code execution
- Jupyter Notebook tokens are often logged to files
- The sattrack binary could be abused with file:// URIs to read arbitrary files
- Multiple user pivots (postgres → juno → jovian → root) demonstrated group membership exploitation
