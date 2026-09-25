---
type: source
title: "HTB ScriptKiddie writeup"
raw: raw/htb-scriptkiddie.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[scriptkiddie]]
---
# Source: HTB ScriptKiddie writeup
> Easy Linux box exploiting a novice hacker toolkit website. Covers CVE-2020-7384 msfvenom APK template command injection, incron-based command injection via log manipulation, and sudo rights abuse for root access through msfconsole.

## Key facts extracted
- Website offers nmap scanning, searchsploit, and msfvenom payload generation
- CVE-2020-7384: msfvenom APK template processing allows command injection  
- Metasploit exploit module generates malicious APK for reverse shell
- incron monitors /home/kid/logs/hackers file for automated scanning
- scanlosers.sh script reads log file, vulnerable to command injection
- Script uses cut -f3- to extract IPs, then passes to nmap via sh -c
- pwn user has NOPASSWD sudo for /opt/metasploit-framework-6.0.9/msfconsole
- msfconsole irb (Ruby shell) provides system() command execution

## Filed into
[[scriptkiddie]], [[cve-2020-7384]], [[incron-abuse]], [[command-injection]], [[sudo-abuse]], [[ruby-shell]]
