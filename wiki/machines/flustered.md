---
type: machine
title: Flustered
platform: htb
os: linux
difficulty: medium
tags: [linux, web, ssti, docker, glusterfs]
solved: 2026-07-09
sources: [[htb-flustered]]
related: []
---
# Flustered
> Medium-difficulty Linux box featuring GlusterFS file system access, server-side template injection, and container escape. Exploiting unauthenticated GlusterFS volume mount to extract Squid credentials, then SSTI in Flask application for initial access, and finally Azure Storage emulator escape for root privileges.

## Attack path
1. [[glusterfs]] enumeration to discover accessible volumes
2. Extract Squid credentials from mounted vol2 database files
3. Authenticate through Squid proxy to access internal application
4. [[ssti]] in Flask application at /app/app.py
5. Python-based reverse shell via SSTI payload execution
6. Extract SSL certificates from /etc/ssl for GlusterFS vol1 access
7. SSH key manipulation for user access
8. [[container-breakout]] via Azure Storage emulator access
9. Extract root SSH key from Azure Storage blob container

## Techniques used
- [[glusterfs]] — Mounted unauthenticated GlusterFS volumes to access file systems directly
- [[sqli]] — Read MySQL/MariaDB database files to extract Squid authentication credentials
- [[ssti]] — Server-side template injection in Flask/Jinja2 application to execute Python code
- [[container-breakout]] — Docker container escape via Azure Storage emulator on port 10000
- [[ssh]] — SSH key manipulation and access via extracted private keys

## Tools used
- [[nmap]], [[feroxbuster]], [[gobuster]]
- [[glusterfs-client]], [[mount]]
- [[curl]], [[python]], [[nc]]
- [[ssh]], [[storage-explorer]]

## Services / ports
- [[ssh]] (22), [[http]] (80, nginx)
- squid-proxy (3128), GlusterFS ports (111, 24007, 49152, 49153)
- Docker container on 172.17.0.2:10000 (Azure Storage emulator)

## Lessons / notes
- GlusterFS volumes can sometimes be mounted without authentication, exposing sensitive data
- Squid proxy logs and databases may contain credentials in plaintext
- SSTI in Flask/Jinja2 can be exploited for RCE through Python subprocess calls
- Azure Storage emulator runs in Docker and can store SSH keys
- SSL certificates may be required for certain GlusterFS volume mounts
