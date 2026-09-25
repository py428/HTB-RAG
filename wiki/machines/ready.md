---
type: machine
title: Ready
platform: htb
os: linux
difficulty: medium
tags: [web, linux, docker, container, gitlab]
solved: 2026-07-09
sources: [[htb-ready]]
related: []
---
# Ready
> GitLab container exploitation leveraging SSRF and CRLF injection vulnerabilities to achieve Redis RCE, followed by Docker privileged container escape via cgroups attack and host filesystem mounting for full system compromise.

## Attack path
1. Register account on exposed GitLab instance (version 11.4.7)
2. Exploit [[ssrf]] vulnerability (CVE-2018-19571) using IPv6 localhost bypass via project import
3. Combine with [[crlf-injection]] (CVE-2018-19585) to inject Redis commands for RCE
4. Gain shell as git user in container and find root password in gitlab.rb configuration
5. Escape privileged container using [[cgroups-escape]] technique or direct host filesystem mounting
6. Access host filesystem and root flag via mounted disk or cgroups command execution

## Techniques used
- [[ssrf]] — Bypass localhost restrictions using IPv6 representation [0:0:0:0:0:ffff:127.0.0.1]
- [[crlf-injection]] — Inject newline characters in URL to send Redis commands after Git protocol
- [[redis-rce]] — Exploit Redis to execute arbitrary commands via GitLab webhook queue
- [[privileged-container-escape]] — Escape Docker container with privileged flag using cgroups or filesystem access
- [[cgroups-escape]] — Execute commands on host via release_agent cgroup manipulation

## Tools used
- [[nmap]] — Port and service enumeration identifying GitLab on TCP 5080
- [[python3]] — Custom exploit script for GitLab SSRF + CRLF injection
- [[nc]] — Reverse shell connections and HTTP request capture
- [[curl]] — Web requests and payload delivery
- [[mount]] — Host filesystem access from privileged container

## Services / ports
- SSH (22) — OpenSSH 8.2p1 Ubuntu
- HTTP (5080) — GitLab 11.4.7 with known SSRF and CRLF injection vulnerabilities

## Lessons / notes
- GitLab 11.4.7 contains unpatched SSRF (CVE-2018-19571) and CRLF injection (CVE-2018-19585)
- IPv6 localhost representation bypasses IP-based access controls
- Redis can be exploited for RCE via GitLab webhook queue manipulation
- Privileged Docker containers provide full host system access
- cgroups release_agent can execute commands on host from container
- GitLab configuration files often contain sensitive credentials in plain text
- docker-compose.yml reveals container security settings including privileged mode