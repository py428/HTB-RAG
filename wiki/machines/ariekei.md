---
type: machine
title: Ariekei
platform: htb
os: linux
difficulty: insane
tags: [linux, docker, shellshock, imagetragick, container-escape]
solved: 2026-07-09
sources: [[htb-ariekei]]
related: []
---
# Ariekei
> Insane Linux box with complex Docker environment featuring Shellshock and ImageTragick exploitation, container network pivoting, and Docker privilege escalation.

## Attack path
1. Virtual host enumeration reveals calvin.ariekei.htb and beehive.ariekei.htb
2. [[imagetragick]] on calvin upload for initial container shell
3. Docker network enumeration via mounted /common directory
4. SSH key access from .secrets to reach bastion container
5. [[shellshock]] exploitation from bastion to beehive container
6. SSH key extraction from container filesystem for host access
7. [[docker-escape]] via docker group membership for root access

## Techniques used
- [[imagetragick]] — CVE-2016-3714 command injection via malicious MVG file upload
- [[shellshock]] — CVE-2014-6271 CGI environment variable injection
- [[docker-escape]] — Mounting host filesystem into container for privilege escalation
- [[ssh-key-reuse]] — Extracting and cracking encrypted SSH private keys
- [[container-pivoting]] — Using Docker network access to reach internal services

## Tools used
- [[nmap]], [[feroxbuster]], [[wfuzz]], [[convert]], [[hashcat]], [[ssh2john]], [[docker]]

## Services / ports
- [[ssh]] (22, 1022), [[http]] (443 nginx reverse proxy)

## Lessons / notes
- Docker container networking allows lateral movement between services
- Common mounted directories provide configuration and credential information
- SSH key extraction from containers provides host authentication
- Docker group membership equivalent to root access via container filesystem mounting
- Virtual host routing requires careful enumeration to discover all services
- WAF can block direct exploitation but internal network bypasses restrictions
