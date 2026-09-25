---
type: source
title: "HTB Squashed writeup"
raw: raw/htb-squashed.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[squashed]]
---
# Source: HTB Squashed writeup
> Comprehensive writeup covering NFS exploitation, userid spoofing for webshell upload, and X11 cookie theft for privilege escalation via KeePassXC password manager screenshot.
## Key facts extracted
- NFS exports: `/home/ross` and `/var/www/html` accessible to all
- Web root owned by UID 2017, requires matching local user for write access
- PHP execution enabled on web server
- `.Xauthority` cookie accessible via NFS for X11 authentication
- Root password visible in KeePassXC screenshot captured via X11

## Filed into
[[squashed]], [[nfs-enumeration]], [[userid-spoofing]], [[web-shell-upload]], [[x11-cookie-theft]], [[x11-screenshot]], [[credential-theft]]
