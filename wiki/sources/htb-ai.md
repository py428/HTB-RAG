---
type: source
title: "HTB AI writeup"
raw: raw/htb-ai.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[ai]]
---
# Source: HTB AI writeup
> Detailed exploitation guide for AI, a medium Linux HackTheBox machine featuring audio-based SQL injection through speech recognition and Java Debug Wire Protocol exploitation for privilege escalation.

## Key facts extracted
- Speech recognition maps: "open single quote" → ', "union" → union, "comment database" → -- -
- MySQL credentials: dbuser / toor for alexa database
- User alexa password: H,Sq9t6}a<)?q93_
- Tomcat running as root with JDWP enabled on localhost:8000
- jdwp-shellifier exploits Java Debug Wire Protocol for remote code execution
- Python speech recognition script handles audio-to-text conversion with symbol replacement

## Filed into
[[ai]], [[audio-sql-injection]], [[java-debug-exploitation]], [[database-credential-exposure]]
