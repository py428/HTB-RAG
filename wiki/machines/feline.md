---
type: machine
title: Feline
platform: htb
os: linux
difficulty: hard
tags: [linux, web, java, privesc]
solved: 2026-07-09
sources: [[htb-feline]]
related: []
---
# Feline
> A Tomcat/GlassFish server box exploiting CVE-2020-9484 for session deserialization, CVE-2020-11651 for SaltStack RCE, then Docker socket abuse for container escape to root.
## Attack path
1. Exploit CVE-2020-9484 session deserialization in Tomcat to upload [[ysoserial]] payload
2. Trigger deserialization via JSESSIONID cookie pointing to uploaded session file
3. Get shell as tomcat, identify SaltStack on ports 4505/4506
4. Tunnel through [[chisel]] to access localhost SaltStack ports
5. Exploit CVE-2020-11651 for unauthenticated RCE as root in container
6. Abuse Docker socket access from container to mount host filesystem and get root flag
## Techniques used
- [[cve-2020-9484]] — Tomcat session deserialization via manipulated JSESSIONID cookie
- [[cve-2020-11651]] — SaltStack ClearFuncs authentication bypass for RCE
- [[docker-socket-abuse]] — Mount host filesystem via Docker API to access root files
- [[port-tunneling]] — Use chisel to tunnel through restricted network access
## Tools used
- [[nmap]], [[ysoserial]], [[chisel]], [[docker]]
- [[curl]], [[netcat]], [[python]], [[proxychains]]
## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 8.2p1 Ubuntu
- 8080/tcp — [[http]] — Apache Tomcat 9.0.27
- 4505-4506/tcp — SaltStack (localhost only)
## Lessons / notes
- CVE-2020-9484 allows deserialization by pointing JSESSIONID cookie to arbitrary files via path traversal
- SaltStack CVE-2020-11651 provides unauthenticated RCE via ClearFuncs method
- Docker socket mounted in containers provides complete control over host system
- Chisel enables SOCKS proxy tunneling for accessing restricted network services
