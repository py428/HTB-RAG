---
type: source
title: "HTB FriendZone writeup"
raw: raw/htb-friendzone.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[friendzone]]
---
# Source: HTB FriendZone writeup
> Complete writeup for FriendZone HTB machine covering DNS zone transfer, SMB enumeration, LFI exploitation, and Python library hijacking for privilege escalation.

## Key facts extracted
- Ubuntu 18.04 system with multiple web services
- DNS zone transfer exposed friendzone.red and friendzoneportal.red domains
- SMB shares accessible with credentials: admin:WORKWORKHhallelujah@#
- LFI vulnerability in dashboard.php parameter
- MySQL credentials: friend:Agpyu12!0.213$
- Writable Python module: /usr/lib/python2.7/os.py
- Root cron job executing /opt/server_admin/reporter.py

## Filed into
[[friendzone]], [[dns-zone-transfer]], [[smb-enum]], [[lfi]], [[python-library-hijack]], [[cronjob-abuse]]
