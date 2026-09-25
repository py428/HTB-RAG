---
type: machine
title: ScriptKiddie
platform: htb
os: linux
difficulty: easy
tags: [web, linux, command-injection]
solved: 2026-07-09
sources: [[htb-scriptkiddie]]
related: []
---
# ScriptKiddie
> ScriptKiddie is an easy Linux box themed around a novice hacker's toolkit website. The exploitation involves CVE-2020-7384 command injection in msfvenom APK templates, incron-based command injection via log file manipulation, and sudo rights abuse for root access.

## Attack path
1. Enumerate web application with nmap, searchsploit, and msfvenom tools
2. Exploit [[cve-2020-7384]] — command injection in msfvenom APK template upload
3. Get reverse shell as kid user
4. Discover incron-triggered script reading from hackers log file
5. [[command-injection]] in log file processed by scanlosers.sh script
6. Inject reverse shell command into hackers log for pwn user access
7. Abusing sudo rights: pwn can run msfconsole as root
8. Use msfconsole Ruby shell for root access

## Techniques used
- [[cve-2020-7384]] — msfvenom APK template command injection
- [[incron-abuse]] — File system event triggers for command execution
- [[command-injection]] — Log file manipulation for script injection
- [[sudo-abuse]] — SUID privileges on msfconsole binary
- [[ruby-shell]] — msfconsole irb for system command execution

## Tools used
[[nmap]], [[searchsploit]], msfconsole, [[nc]], [[hydra]]

## Services / ports
- [[ssh]] (22) — OpenSSH 8.2p1 Ubuntu
- HTTP (5000) — Werkzeug httpd 0.16.1 (Python 3.8.5) - Hacker tools website

## Lessons / notes
- msfvenom APK template processing injects arbitrary commands
- incron monitors hackers log file for automated scanning
- scanlosers.sh script is vulnerable to command injection via cut processing
- Must account for cut -f3- processing when crafting payloads
- Comment remainder of line with # to prevent shell errors
- msfconsole irb provides simple system() for command execution

## Beyond Root
- incron configuration shows two triggers: nmap output sanitization and hacker scanning
- Web filtering prevents scanning non-HTB IPs
- msfconsole Ruby shell (irb) is simpler than full shell escape
