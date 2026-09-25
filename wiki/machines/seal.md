---
type: machine
title: Seal
platform: htb
os: linux
difficulty: medium
tags: [web, privesc, linux, ansible, nginx, tomcat]
solved: 2026-07-09
sources: [[htb-seal]]
related: []
---
# Seal
> Seal is a medium Linux box featuring a web application with NGINX reverse proxy to Tomcat, where exploiting URL parsing differences between the two servers allows bypassing mutual authentication. Initial access is gained through Tomcat manager access using credentials from a GitBucket repository, then by exploiting a scheduled Ansible backup playbook with symlink abuse to read user files. Privilege escalation involves abusing sudo permissions to run malicious Ansible playbooks as root.

## Attack path
1. [[nmap]] enumeration reveals SSH, HTTP/HTTPS, and HTTP-Proxy on port 8080
2. [[feroxbuster]] discovers Tomcat manager and GitBucket instance on port 8080
3. Enumerate GitBucket repository and find Tomcat credentials in commit history
4. Exploit [[url-traversal-bypass]] - abuse NGINX/Tomcat URL parsing difference with `/manager;name=0xdf/html` to bypass mutual authentication
5. Access Tomcat Manager using credentials from GitBucket and deploy malicious WAR file via [[msfvenom]]
6. Exploit scheduled Ansible backup playbook by creating symlink in writable uploads directory
7. Extract backup archive to obtain user SSH key and user.txt
8. Abuse sudo permissions to run [[ansible-playbook]] as root for reverse shell or SSH key addition

## Techniques used
- [[url-traversal-bypass]] — NGINX/Tomcat URL parsing difference allows bypassing mutual authentication checks
- [[war-file-deployment]] — Deploy malicious WAR file through Tomcat Manager application
- [[symlink-abuse]] — Create symlink in Ansible backup directory to capture user files in scheduled backups
- [[ansible-playbook-abuse]] — Abuse sudo permissions to run Ansible playbooks as root

## Tools used
[[nmap]], [[feroxbuster]], [[wfuzz]], [[msfvenom]], [[nc]], [[ansible-playbook]], [[git]]

## Services / ports
22/tcp — [[ssh]], 443/tcp — [[http]] (NGINX), 8080/tcp — [[http]] (Tomcat)

## Lessons / notes
- NGINX and Tomcat parse URLs differently - semicolons in paths are interpreted differently, allowing bypass of location-based authentication checks
- GitBucket repositories may contain sensitive configuration files in commit history
- Ansible synchronize modules with `copy_links=yes` will follow symlinks, potentially exposing unintended files
- SSH keys found in backups can be used for direct access even when original files are protected
