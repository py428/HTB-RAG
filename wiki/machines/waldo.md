---
type: machine
title: Waldo
platform: htb
os: linux
difficulty: medium
tags: [linux, web, container, capabilities, file-read]
solved: 2026-07-09
sources: [[htb-waldo]]
related: []
---
# Waldo
> Waldo is a medium Linux box featuring a PHP web application with file read functionality. I'll exploit a str_replace filter bypass to read arbitrary files, find an SSH key in the user's .ssh directory, use it to access a container where I can SSH back to the host with a restricted rbash shell, escape the shell using ed editor commands, and finally exploit Linux capabilities assigned to the tac program to read the root flag.

## Attack path
1. Enumerate HTTP service and discover file read functionality via POST requests
2. Bypass [[str_replace-bypass]] filters using double-encoded traversal sequences (....//)
3. Read SSH key from /home/nobody/.ssh/.monitor and access container as nobody
4. SSH from container to localhost on port 8888 to reach host with [[rbash-escape]]
5. Escape restricted shell using ed editor's !/bin/sh command
6. Exploit [[linux-capabilities]] on tac binary with CAP_DAC_READ_SEARCH for full system read
7. Use tac to read /root/root.txt flag

## Techniques used
- [[str_replace-bypass]] — Bypassing PHP str_replace filters with double-encoded path traversal
- [[ssh-key-auth]] — Using exfiltrated SSH private key for container access
- [[container-pivot]] — SSH from container back to host via localhost:8888
- [[rbash-escape]] — Breaking restricted bash shell using ed editor system commands
- [[linux-capabilities]] — Exploiting CAP_DAC_READ_SEARCH capability on tac for full read access

## Tools used
- [[nmap]] — Port scanning and service identification
- curl — HTTP POST requests to file read endpoints
- jq — JSON parsing for file read responses
- [[ssh]] — Container and host access
- ed — Text editor for rbash escape
- getcap — Linux capabilities enumeration
- tac — Reverse cat command with file read capabilities

## Services / ports
- 22/tcp — [[ssh]] (OpenSSH 7.5)
- 80/tcp — [[http]] (nginx 1.12.2)
- 8888/tcp — [[ssh]] (filtered, container SSH)

## Lessons / notes
- str_replace filter bypass: Non-recursive replacement can be defeated with double-encoded payloads
- Container architecture: SSH from container back to host requires alternative port (8888)
- rbash restrictions: Limited to specific PATH binaries but editors like ed may provide shell escape
- Linux capabilities: CAP_DAC_READ_SEARCH allows full file read regardless of permissions
- Alpine container: Minimal Linux distribution often used for Docker/containers
- SSH key discovery: Keys in .ssh directories may have comments revealing target usernames
- Port filtering: Filtered ports (8888) may still be accessible from localhost
