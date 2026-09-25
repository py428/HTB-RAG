---
type: machine
title: AI
platform: htb
os: linux
difficulty: medium
tags: [web, linux, privesc, audio, sql-injection, java]
solved: 2026-07-09
sources: [[htb-ai]]
related: []
---
# AI
> A smart speaker themed box featuring audio-based SQL injection through speech recognition, followed by Java Debug Wire Protocol exploitation for privilege escalation.

## Attack path
1. [[web-enumeration]] to discover audio file upload interface
2. [[audio-sql-injection]] via speech-to-text conversion exploiting SQL injection
3. Database enumeration to extract SSH credentials for alexa user
4. [[java-debug-exploitation]] via JDWP on port 8000 for root shell

## Techniques used
- [[audio-sql-injection]] — SQL injection through speech recognition using audio file manipulation
- [[database-credential-exposure]] — Password extraction from MySQL users table
- [[java-debug-exploitation]] — JDWP shellifier exploiting Tomcat debug port

## Tools used
[[nmap]] [[gobuster]] flite curl jdwp-shellifier nc

## Services / ports
- [[ssh]] 22 — OpenSSH 7.6p1 Ubuntu 4ubuntu0.3
- [[http]] 80 — Apache httpd 2.4.29
- MySQL 3306 — localhost only
- Tomcat 8080 — localhost only with JDWP debug enabled
- JDWP 8000 — Java Debug Wire Protocol on localhost

## Lessons / notes
- Audio-based SQL injection requires understanding speech recognition patterns and symbol mapping
- The speech recognition system maps spoken words to SQL symbols (single quote, union, etc.)
- Java Debug Wire Protocol can be exploited for remote code execution when exposed
- Tomcat running as root with debug mode enabled provides a privilege escalation path
- The box demonstrates creative attack vectors involving audio processing and development tools

## CVEs
- CVE-2019-0232 (Tomcat JDWP - implied vulnerability)
