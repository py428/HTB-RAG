---
type: source
title: "HTB Flustered writeup"
raw: raw/htb-flustered.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[flustered]]
---
# Source: HTB Flustered writeup
> Medium Linux box featuring GlusterFS exploitation, SSTI, and container escape. Accessing unauthenticated file systems, exploiting template injection, and breaking out of Azure Storage emulator container.

## Key facts extracted
- GlusterFS running on ports 111, 24007, 49152, 49153 with two volumes: vol1 and vol2
- vol2 mounted without authentication, contains MySQL data files with Squid credentials
- Squid credentials: lance.friedman / o>WJ5-jD<5^m3
- Flask application at 127.0.0.1 accessible only through authenticated Squid proxy
- SSTI vulnerability in Flask app using render_template_string with user-controlled data
- Docker container running Azure Storage emulator on port 10000
- Azure Storage key in /var/backups/key allows access to root SSH key

## Filed into
[[flustered]], [[glusterfs]], [[sqli]], [[ssti]], [[container-breakout]], [[ssh]]
