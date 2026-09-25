---
type: source
title: "HTB Socket writeup"
raw: raw/htb-socket.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[socket]]
---
# Source: HTB Socket writeup
> Complete writeup covering QR application analysis, SQLite injection over websockets, and PyInstaller spec file abuse for file read privilege escalation.

## Key facts extracted
- PyInstaller binary contains websocket client code
- Websocket endpoint: ws://ws.qreader.htb:5789/version
- SQLite injection in version parameter with double-quote injection
- Database contains user credentials with crackable hash
- User tkeller with password denjanjade122566
- Sudo access to build-installer.sh PyInstaller build script
- Malicious spec file can include arbitrary files via datas parameter

## Filed into
[[socket]], [[sqli-websocket]], [[pyinstaller-abuse]], [[pyinstxtractor]]
