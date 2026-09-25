---
type: source
title: "HTB FluxCapacitor writeup"
raw: raw/htb-fluxcapacitor.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[fluxcapacitor]]
---
# Source: HTB FluxCapacitor writeup
> Medium Linux box with command injection and sudo abuse. Exploiting WAF-protected web parameter and custom sudo script for privilege escalation.

## Key facts extracted
- OpenResty nginx with ModSecurity WAF protecting /sync endpoint
- Command injection in opt parameter processed by Lua application
- WAF bypass techniques: quote splitting, space avoidance
- Sudo entry allowing NOPASSWD execution of /home/themiddle/.monit
- .monit script accepts base64-encoded commands and executes them as root

## Filed into
[[fluxcapacitor]], [[command-injection]], [[waf-bypass]], [[sudo]], [[base64-encoding]]
