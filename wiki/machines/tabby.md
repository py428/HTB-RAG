---
type: machine
title: Tabby
platform: htb
os: linux
difficulty: easy
tags: [linux, web, php, tomcat, lxd, container]
solved: 2026-07-09
sources: [[htb-tabby]]
related: []
---
# Tabby
> Easy Linux box with Tomcat server and website vulnerable to LFI. Leak Tomcat credentials via LFI, use Tomcat manager API to deploy WAR file, then crack password from backup archive for user access. Final privilege escalation via LXD container group membership.

## Attack path
1. [[lfi]] — Local file inclusion in news.php reads arbitrary files
2. [[tomcat-credentials-leak]] — Read tomcat-users.xml via LFI
3. [[war-deployment]] — Deploy malicious WAR via Tomcat text-based manager API
4. [[zip-cracking]] — Crack password from backup zip archive using john/zip2john
5. [[password-reuse]] — Reuse cracked password to SSH as ash user
6. [[lxd-privilege-escalation]] — Exploit lxd group membership to mount host filesystem

## Techniques used
- [[lfi]] — PHP file inclusion vulnerability in news.php parameter
- [[tomcat-war-deployment]] — Use manager API to upload WAR via HTTP PUT
- [[password-cracking]] — Crack protected zip with john/rockyou.txt
- [[lxd-container-abuse]] — Create privileged container to mount host root filesystem

## Tools used
[[nmap]], [[gobuster]], [[curl]], [[msfvenom]], [[nc]], [[zip2john]], [[john]], [[ssh]], lxc

## Services / ports
[[ssh]] (22), [[http]] (80), tcp/8080 (Tomcat)

## Lessons / notes
- LFI allows reading tomcat-users.xml even outside standard paths
- Tomcat manager-script role permits text-based API access without GUI
- m0noc's 656-byte base64 LXD image is faster than full alpine build
- LXC privileged container with mounted host FS allows full system access