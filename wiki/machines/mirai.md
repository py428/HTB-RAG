---
type: machine
title: Mirai
platform: htb
os: linux
difficulty: easy
tags: [linux, iot, credentials, data-recovery]
solved: 2026-07-09
sources: [[htb-mirai]]
related: []
---
# Mirai

> Mirai is an Easy-level Linux box featuring a Raspberry Pi running PiHole with default credentials, where the root flag must be recovered from a deleted file on a USB drive using forensic techniques.

## Attack path
1. Enumerate open ports including SSH, HTTP, and unusual UPnP/Plex ports
2. Find PiHole admin interface via directory brute force and basic authentication 
3. Use default Raspberry Pi credentials (pi:raspberry) for SSH access
4. Escalate to root using sudo privileges (NOPASSWD: ALL)
5. Recover deleted root.txt flag from USB drive using forensic tools

## Techniques used
- [[default-credentials]] — Raspberry Pi default username pi with password raspberry for SSH access
- [[sudo-abuse]] — NOPASSWD: ALL configuration allows pi user to run any command as root without password
- [[data-recovery]] — Recover deleted files from ext4 filesystem using extundelete, grep/strings, and forensic techniques

## Tools used
- [[nmap]] — Port scanning and service version detection
- [[feroxbuster]] — Directory brute force to discover /admin and other hidden paths
- [[sshpass]] — SSH authentication with password
- [[extundelete]] — File recovery utility for deleted files on ext filesystem
- [[grep]] — Search for hex patterns (32-character flag strings) in raw disk data
- [[strings]] — Extract readable strings from binary files
- [[dd]] — Copy raw disk data for offline forensic analysis

## Services / ports
- [[ssh]] (22) — Secure shell access with default Raspberry Pi credentials
- [[http]] (80) — PiHole web interface on lighttpd
- [[dns]] (53) — dnsmasq DNS server
- [[upnp]] (1877, 32469) — Universal Plug and Play services
- [[http]] (32400) — Plex media server

## Lessons / notes
- Raspberry Pi devices often ship with default pi:raspberry credentials that should be changed immediately
- IoT devices like PiHole may run administrative interfaces that are accessible from the network
- Deleted files on filesystems can often be recovered using forensic tools like extundelete
- USB drives may contain backup copies of important files when primary copies are deleted
- The Mirai malware was designed to exploit default credentials on IoT devices
- Simple forensic techniques like grep with hex patterns can recover flags from raw disk images
