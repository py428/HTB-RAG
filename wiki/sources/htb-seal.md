---
type: source
title: "HTB Seal writeup"
raw: raw/htb-seal.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[seal]]
---
# Source: HTB Seal writeup
> Detailed writeup for HTB Seal machine covering NGINX/Tomcat URL parsing bypass, GitBucket credential enumeration, Ansible playbook symlink abuse, and sudo-based privilege escalation via malicious playbooks.

## Key facts extracted
- Seal runs NGINX as reverse proxy to Tomcat with mutual authentication on `/manager/html` and `/admin/dashboard`
- GitBucket on port 8080 contains configuration repositories with Tomcat credentials in commit history
- Scheduled Ansible backup playbook runs every minute using synchronize module with `copy_links=yes`
- User luis has sudo permissions to run ansible-playbook as root without password

## Filed into
[[seal]], [[url-traversal-bypass]], [[war-file-deployment]], [[symlink-abuse]], [[ansible-playbook-abuse]]
