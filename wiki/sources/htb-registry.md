---
type: source
title: "HTB Registry writeup"
raw: raw/htb-registry.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[registry]]
---
# Source: HTB Registry writeup
> Detailed exploitation of private Docker registry with default credentials, container filesystem analysis for SSH credentials, Bolt CMS webshell upload, and Restic backup abuse for privilege escalation on Linux host.

## Key facts extracted
- Docker registry accessible with admin:admin credentials
- Container filesystem extracted to find SSH key at /root/.ssh/ with passphrase in /etc/profile.d/01-ssh.sh
- Bolt CMS database accessible locally containing bcrypt hash for admin user
- Sudo rule allows www-data to run restic backup as root: `/usr/bin/restic backup -r rest*`
- Cron job runs cleanup script every 2 minutes removing PHP uploads from Bolt CMS
- Restic local repos fail due to permission issues when root creates files
- SSH reverse tunnel bypasses egress restrictions to pipe backups to external rest-server

## Filed into
[[registry]], [[docker-registry]], [[ssh-key-reuse]], [[sqlite-extraction]], [[web-shell]], [[sudo-abuse]], [[backup-abuse]], [[ssh-tunnel]]
