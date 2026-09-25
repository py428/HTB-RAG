---
type: source
title: "HTB Fatty writeup"
raw: raw/htb-fatty.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[fatty]]
---
# Source: HTB Fatty writeup
> Detailed 0xdf writeup covering complex Java reverse engineering, JAR modification, SQL injection, and Java deserialization exploitation. Shows the entire process from client modification to root escalation via log file poisoning.
## Key facts extracted
- Anonymous FTP provides fatty-client.jar which must be decompiled and modified to connect to correct ports
- Server JAR contains SQL injection allowing role manipulation for admin access
- changePW function accepts serialized User objects vulnerable to ysoserial exploitation
- Container runs cron job using SCP to archive log files, which can be abused to overwrite root's SSH authorized_keys
- Python-based brute forcing of SSH keys character-by-character using cmatch SUID binary
## Filed into
[[fatty]], [[jar-modification]], [[sqli]], [[directory-traversal]], [[java-deserialization]], [[log-file-poisoning]]
