---
type: source
title: "HTB Doctor writeup"
raw: raw/htb-doctor.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[doctor]]
---
# Source: HTB Doctor writeup
> Dual-path exploitation of healthcare messaging platform featuring SSTI via RSS feed and command injection through URL validation, followed by log analysis for credential discovery and Splunk exploitation for root access.

## Key facts extracted
- Website runs Python Flask with Jinja2 templating on Werkzeug server
- /archive endpoint renders message titles in RSS feed without sanitization
- URL validation uses os.system("curl " + url) allowing command injection
- Apache backup logs contain password "Guitar123" from failed reset: POST /reset_password?email=Guitar123
- Splunk service on TCP 8089 accepts shaun/Guitar123 credentials
- SplunkWhisperer2 exploits Splunk for reverse shell as root

## Filed into
[[doctor]], [[ssti]], [[command-injection]], [[log-analysis]], [[password-reuse]], [[splunk-rce]]
