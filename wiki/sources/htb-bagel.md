---
type: source
title: "HTB Bagel writeup"
raw: raw/htb-bagel.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[bagel]]
---
# Source: HTB Bagel writeup

> Detailed writeup for HackTheBox machine Bagel covering path traversal, .NET reverse engineering, JSON deserialization exploits, and sudo dotnet abuse for privilege escalation.

## Key facts extracted
- Flask app at :8000 with path traversal via ?page= parameter reading files with send_file
- .NET application at :5000 using websocket with JSON serialization (TypeNameHandling Auto)
- DLL location: /opt/bagel/bin/Debug/net6.0/bagel.dll
- Database credentials from DLL: dev/k8wdAYYKyhnjg3K
- Developer user can run /usr/bin/dotnet as root with sudo

## Filed into
[[bagel]], [[path-traversal]], [[binary-reverse-engineering]], [[json-deserialization]], [[file-read]], [[sudo-dotnet]]
