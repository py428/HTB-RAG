---
type: source
title: "HTB Celestial writeup"
raw: raw/htb-celestial.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[celestial]]
---
# Source: HTB Celestial writeup
> Node.js Express application writeup covering deserialization vulnerability in cookie handling using node-serialize library and cron hijacking for privilege escalation.

## Key facts extracted
- Machine: Celestial (Medium, Linux)
- Node.js Express framework on TCP 3000
- Vulnerable library: node-serialize
- Cookie-based authentication with base64-encoded JSON
- Root cron running every 5 minutes
- User script.py resets from /root/script.py

## Filed into
[[celestial]], [[cookie-analysis]], [[node-js-deserialization]], [[cron-hijack]]
