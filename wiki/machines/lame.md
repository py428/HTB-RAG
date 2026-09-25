---
type: machine
title: Lame
platform: htb
os: linux
difficulty: easy
tags: [smb, ftp, linux, privesc]
solved: 2026-07-09
sources: [[htb-lame]]
related: []
---
# Lame
> Lame is a very easy Linux box and the first released on HTB. The attack path exploits a Samba username map script vulnerability that allows command execution by using shell metacharacters in the username, directly yielding a root shell without requiring privilege escalation.

## Attack path
1. [[samba-usermap-script]] — Execute arbitrary commands via username with shell metacharacters
2. [[reverse-shell]] — Get root shell via netcat callback

## Techniques used
- [[samba-usermap-script]] — Exploit CVE-2007-2447 in Samba 3.0.20-3.0.25rc3 username map script configuration
- [[reverse-shell]] — Establish interactive shell via netcat reverse connection

## Tools used
- [[nmap]]
- [[smbmap]]
- [[smbclient]]
- [[netcat]]
- [[metasploit]]
- python

## Services / ports
- [[ftp]] (21)
- [[ssh]] (22)
- [[smb]] (139/445)
- distcc (3632)

## Lessons / notes
- VSFTPD 2.3.4 backdoor exists but is blocked by firewall—port 6200 not accessible externally
- Samba 3.0.20 username map script vulnerability allows command execution without authentication
- Exploit works by sending username with backticks containing commands
- Metasploit module exploit/multi/samba/usermap_script automates this attack
- This is the first HTB box released, designed to be very easy for beginners