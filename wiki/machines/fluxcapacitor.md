---
type: machine
title: FluxCapacitor
platform: htb
os: linux
difficulty: medium
tags: [linux, web, command-injection, sudo]
solved: 2026-07-09
sources: [[htb-fluxcapacitor]]
related: []
---
# FluxCapacitor
> Medium-difficulty Linux box featuring web application exploitation and privilege escalation. Exploiting command injection in a web application parameter protected by WAF, then abusing sudo privileges for root access through base64-encoded command execution.

## Attack path
1. [[command-injection]] in /sync?opt parameter
2. [[waf-bypass]] using quote splitting and space avoidance techniques
3. Execute commands to enumerate file system and find user.txt
4. [[privilege-escalation]] via sudo -l analysis
5. [[sudo]] abuse of /home/themiddle/.monit script with base64-encoded commands
6. Execute arbitrary commands as root via .monit wrapper script

## Techniques used
- [[command-injection]] — Injected commands into opt parameter processed by Lua application
- [[waf-bypass]] — Bypassed ModSecurity WAF using quote splitting (' pw''d') and space avoidance
- [[sudo]] — Abused NOPASSWD sudo entry for custom .monit script accepting base64-encoded commands
- [[base64-encoding]] — Used base64 encoding to pass commands through sudo script

## Tools used
- [[nmap]], [[gobuster]], [[wfuzz]]
- [[curl]], [[python]], [[bash]]
- [[sudo]]

## Services / ports
- [[http]] (80) - nginx with Lua application and SuperWAF
- OpenResty nginx with ModSecurity WAF

## Lessons / notes
- WAF can often be bypassed with creative encoding and command splitting
- Lua applications in OpenResty can be vulnerable to command injection
- Custom sudo scripts can be powerful attack vectors if they accept user input
- Base64 encoding is commonly used to bypass input filters
- The .monit script demonstrates poor security practice in accepting arbitrary base64-encoded commands
