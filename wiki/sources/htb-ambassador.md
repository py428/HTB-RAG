---
type: source
title: "HTB Ambassador writeup"
raw: raw/htb-ambassador.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[ambassador]]
---
# Source: HTB Ambassador writeup
> Complete walkthrough of exploiting Grafana directory traversal, accessing MySQL database, finding leaked Consul token in git history, and achieving root through Consul script execution.

## Key facts extracted
- Grafana version 8.2.0 vulnerable to CVE-2021-43798 directory traversal
- MySQL provisioning config file contains database credentials
- User passwords stored in MySQL whackywidget database
- Git commit history contains hardcoded Consul ACL token
- Consul running with script checks enabled allows code execution

## Filed into
[[ambassador]], [[grafana-file-read]], [[mysql-credential-extraction]], [[git-token-leak]], [[consul-script-exec]]
