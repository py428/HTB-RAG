---
type: machine
title: Ambassador
platform: htb
os: linux
difficulty: medium
tags: [grafana, mysql, consul, ad]
solved: 2026-07-09
sources: [[htb-ambassador]]
related: []
---
# Ambassador
> Active Directory environment with Grafana instance vulnerable to directory traversal, MySQL database containing user credentials, and Consul service with script check execution leading to root.

## Attack path
1. [[grafana-file-read]] vulnerability → Read Grafana configuration
2. Extract admin password from config → Access Grafana dashboard
3. Read MySQL provisioning config → Database credentials
4. Query MySQL for user hashes → Crack and SSH as developer
5. Git repository contains leaked Consul token → Consul access
6. [[consul-script-exec]] → Root shell

## Techniques used
- [[grafana-file-read]] — CVE-2021-43798 directory traversal in plugin endpoint
- [[grafana-config-read]] — Read grafana.ini and provisioning datasources
- [[mysql-credential-extraction]] — User credentials stored in MySQL database
- [[git-token-leak]] — Sensitive token exposed in git history
- [[consul-script-exec]] — Register malicious service check for code execution

## Tools used
- [[nmap]], [[feroxbuster]], [[curl]], [[mysql]], sshpass, [[git]], consul, Metasploit

## Services / ports
- [[ssh]] (22), [[http]] (80, 3000), [[mysql]] (3306)

## Lessons / notes
- Grafana plugins directory traversal allows reading arbitrary files
- MySQL provisioning files often contain plaintext credentials
- Git history frequently contains accidentally committed secrets
- Consul script checks execute as the Consul service user (often root)
- Metasploit has modules for Consul service execution exploits
