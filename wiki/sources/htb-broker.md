---
type: source
title: "HTB Broker writeup"
raw: raw/htb-broker.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[broker]]
---
# Source: HTB Broker writeup
> Easy Linux box featuring unauthenticated ActiveMQ RCE via CVE-2023-46604, followed by nginx abuse for file read/write and alternative LD_PRELOAD privilege escalation.
## Key facts extracted
- ActiveMQ 5.15.15 vulnerable to CVE-2023-46604 (CVSS 10.0)
- Activemq user has NOPASSWD sudo for /usr/sbin/nginx
- Spring XML deserialization payload for reverse shell
- nginx file read: serve root directory on custom port
- nginx file write: DAV PUT method for arbitrary file creation
- Alternative: nginx error_log poisoning of /etc/ld.so.preload
## Filed into
[[broker]], [[activemq-rce]], [[nginx-file-read]], [[nginx-file-write]], [[ld-so-preload]]