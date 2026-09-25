---
type: machine
title: Celestial
platform: htb
os: linux
difficulty: medium
tags: [web, nodejs, deserialization, privesc]
solved: 2026-07-09
sources: [[htb-celestial]]
related: []
---
# Celestial
> Celestial is a Node.js Express application vulnerable to deserialization attacks through insecure cookie handling. I'll exploit the node-serialize library to achieve RCE, then hijack a cron job running as root to escalate privileges.

## Attack path
1. Decode and analyze base64-encoded cookie
2. Craft malicious [[node-js-deserialization]] payload using node-serialize
3. Use [[cookie-analysis]] to bypass authentication and get RCE
4. Hijack root cron job with [[cron-hijack]] for privilege escalation

## Techniques used
- [[cookie-analysis]] — Decode base64 profile cookie to JSON, modify username field
- [[node-js-deserialization]] — Abuse node-serialize library with `_$$ND_FUNC$$_` function wrapper
- [[cron-hijack]] — Replace script.py in ~/Documents to run as root

## Tools used
- [[nmap]]
- [[curl]]
- nodejsshell.py
- node-serialize
- [[python]]

## Services / ports
- [[http]] (3000) — Node.js Express

## Lessons / notes
- Node.js Express app using node-serialize library
- Cookie: profile=eyJ1c2VybmFtZSI6... (base64 JSON)
- node-serialize vulnerable to function execution via `_$$ND_FUNC$$_function(){...}()`
- Reverse shell via Node.js net and child_process.spawn
- Root cron: `*/5 * * * * python /home/sun/Documents/script.py > /home/sun/output.txt`
- Script resets from /root/script.py after execution
