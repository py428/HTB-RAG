---
type: source
title: "HTB Reddish writeup"
raw: raw/htb-reddish.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[reddish]]
---
# Source: HTB Reddish writeup
> Multi-container Docker environment requiring exploitation of Node-Red, Redis webshell, rsync wildcard abuse, and privileged container breakout.

## Key facts extracted
- Node-Red on port 1880 provided JavaScript editor for IoT flows with exec capability
- Redis container shared /var/www/html volume with www container
- Redis CONFIG SET commands allowed writing PHP webshell to www directory
- Backup rsync job ran every 3 minutes with wildcard allowing command execution
- Backup container was privileged with access to host /dev devices

## Filed into
[[reddish]], [[node-red]], [[redis-webshell]], [[rsync-privesc]], [[privileged-container]]