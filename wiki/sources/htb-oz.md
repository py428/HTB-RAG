---
type: source
title: "HTB Oz writeup"
raw: raw/htb-oz.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[oz]]
---

# Source: HTB Oz writeup
> Detailed writeup for HackTheBox Oz machine covering SQL injection exploitation, server-side template injection for container compromise, SSH port knocking for access, and Docker management abuse for privilege escalation.

## Key facts extracted
- Linux environment with multiple Docker containers and web applications
- SQL injection vulnerability in users endpoint for database credential extraction
- Server-side template injection in Jinja2 templates for code execution
- SSH port knocking sequence (40809, 50212, 46969) to access main host
- Docker container breakout using Portainer web interface for root access
- Complex multi-environment scenario requiring network enumeration and pivot planning
- Multiple authentication methods including password-based and key-based SSH access
- Container management interfaces providing powerful exploitation opportunities

## Filed into
[[oz]], [[sqli]], [[ssti]], [[docker-rce]], [[ssh-port-knocking]], [[docker-abuse]]
