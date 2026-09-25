---
type: machine
title: Registry
platform: htb
os: linux
difficulty: hard
tags: [linux, docker, web, privesc, backup-abuse]
solved: 2026-07-09
sources: [[htb-registry]]
related: []
---
# Registry
> Docker registry abuse box: weak credentials allow pulling container image with SSH credentials, then exploit Bolt CMS to get www-data shell, and finally abuse Restic backup agent running as root to read root.txt and extract root SSH key.

## Attack path
1. [[docker-registry]] — Access Docker registry with admin:admin credentials to pull container
2. [[ssh-key-reuse]] — Extract SSH key and passphrase from container filesystem
3. [[web-shell]] — Upload PHP webshell via Bolt CMS admin panel
4. [[sudo-abuse]] — Abuse sudo rule for www-data to run restic backup as root
5. [[backup-abuse]] — Restic backup exploitation to read root.txt and extract root SSH key
6. [[ssh-key-reuse]] — SSH as root using extracted private key

## Techniques used
- [[docker-registry]] — Enumerated catalog, pulled blobs, and extracted filesystem from private Docker registry
- [[exiftool]] — Image metadata analysis to find SSH key passphrase in /etc/profile.d/01-ssh.sh
- [[ssh-key-reuse]] — Used extracted id_rsa and passphrase to SSH as bolt user
- [[sqlite-extraction]] — Downloaded Bolt CMS database to extract admin bcrypt hash
- [[hashcat]] — Cracked bcrypt hash (mode 3200) to get admin:password
- [[web-shell]] — Uploaded PHP webshell via Bolt CMS after modifying accepted_file_types configuration
- [[sudo-abuse]] — Exploited sudo rule allowing www-data to run `/usr/bin/restic backup -r rest*` as root
- [[backup-abuse]] — Created local Restic repo, backed up /root, then read root.txt via dump command
- [[ssh-tunnel]] — SSH reverse tunnel to bypass egress restrictions and pipe backup to attacker's rest-server

## Tools used
- [[nmap]] — Port scanning
- gobuster — Directory brute forcing
- docker — Container image pulling and running
- curl — Docker registry API interaction
- docker_fetch — Alternative container filesystem extraction
- [[sqlite3]] — Bolt CMS database extraction
- [[hashcat]] — Bcrypt hash cracking (mode 3200)
- ssh — Shell access and tunneling
- restic — Backup exploitation
- rest-server — Local REST backup server

## Services / ports
- [[ssh]] (22) — Shell access
- [[http]] (80) / [[https]] (443) — nginx / Bolt CMS
- Docker registry (5000) — Private container registry

## Lessons / notes
- Docker registry v2 API: `/v2/_catalog` lists repos, `/v2/[repo]/tags/list` shows tags, `/v2/[repo]/manifests/[tag]` gets layers
- Container extraction: download blobs and extract with tar, or use docker_pull after adding CA certificate
- Bolt CMS 3.6.4 vulnerable to webshell upload after modifying config to accept PHP files
- Cleanup script cron.sh runs every 2 minutes removing uploaded files from /bolt/files/ directory
- Sudo rule for www-data allows running restic backup with wildcards, allowing creation of local repos
- Local Restic repos fail due to permission issues when root creates files (index/snapshot ownership)
- SSH reverse tunnel (`-R:4433:localhost:4433`) bypasses egress restrictions to pipe backups to attacker
- Backup script at `/var/www/html/backup.php` shows sudo configuration
