---
type: machine
title: Oz
platform: htb
os: linux
difficulty: hard
tags: [linux, web, sqli, ssti, docker, ssh, privesc]
solved: 2026-07-09
sources: [[htb-oz]]
related: []

# Oz
> Multi-environment challenge involving SQL injection for database access, server-side template injection for container compromise, SSH port knocking for access, and Docker management abuse for privilege escalation.

## Attack path
1. [[sqli]] on users endpoint to dump database and crack wizard.oz credentials
2. Login to GBR Support portal and discover [[ssti]] in ticket description field
3. [[ssti]] exploitation in Jinja2 templates for [[docker-rce]] as root in tix-app container
4. [[ssh-port-knocking]] to access main Oz host as dorthi using stolen SSH key
5. [[docker-abuse]] via Portainer web interface for container escape and root access

## Techniques used
- [[sqli]] — Union-based SQL injection to extract user credentials from database
- [[hash-cracking]] — John the Ripper to crack PBKDF2-SHA256 hashes with rockyou.txt wordlist
- [[ssti]] — Server-side template injection in Jinja2 templates for code execution
- [[docker-rce]] — Root shell in tix-app container via SSTI payload execution
- [[ssh-port-knocking]] — Sequential UDP port knocking (40809, 50212, 46969) to open SSH port
- [[ssh-key-reuse]] — SSH private key extracted from database via SQL load_file() function
- [[docker-abuse]] — Container breakout using Portainer to mount host filesystem and gain root access
- [[container-enumeration]] — Docker network and container enumeration for pivot opportunities

## Tools used
- [[nmap]] — Port scanning and service enumeration
- [[wfuzz]] — Web directory and endpoint fuzzing
- [[curl]] — HTTP client for testing and exploitation
- [[john]] — Password cracking for PBKDF2-SHA256 hashes
- [[python]] — Exploit script development and automation
- [[tplmap]] — Automated SSTI detection and exploitation tool
- [[ssh]] — Shell access using port knocking and key-based authentication
- [[nc]] — Netcat for reverse shell handling
- [[docker]] — Container enumeration and management
- [[http]] — HTTP client for Portainer interaction

## Services / ports
- [[ssh]] (22) — Secure shell (protected by port knocking)
- [[http]] (80, 8080, 9000) — Multiple web services including GBR Support and Portainer
- [[mysql]] (3306) — MySQL database accessible from container

## Lessons / notes
- SQL injection remains a prevalent vulnerability even in modern applications
- SSTI vulnerabilities in template engines can lead to complete system compromise
- Port knocking is an effective security through obscurity measure that can be bypassed
- Docker containerization introduces complex attack surfaces and pivot opportunities
- SSH private keys stored in databases can be extracted using SQL functions
- Container management interfaces like Portainer provide powerful capabilities for container abuse
- Multi-environment scenarios require careful network enumeration and pivot planning
