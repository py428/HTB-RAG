---
type: machine
title: Socket
platform: htb
os: linux
difficulty: medium
tags: [linux, web, sqli, python, privesc]
solved: 2026-07-09
sources: [[htb-socket]]
related: []
---
# Socket
> Medium Linux box featuring a QR code application with websocket communication, SQLite injection over websocket to leak credentials, and PyInstaller spec file abuse for arbitrary file read as root.

## Attack path
1. Download and analyze PyInstaller binary to find websocket endpoint
2. Intercept websocket communication and identify [[sqli-websocket]] in version check
3. Exploit SQLite injection to leak user credentials from database
4. Brute force username variations to SSH as tkeller
5. Abuse sudo PyInstaller build script to create malicious [[pyinstaller-abuse]] spec file
6. Extract sensitive files (root SSH key) from compiled binary

## Techniques used
- [[sqli-websocket]] — SQLite injection over websocket protocol
- [[pyinstaller-abuse]] — Malicious spec file with datas parameter for file read
- [[pyinstxtractor]] — Extract embedded files from PyInstaller executable

## Tools used
- [[nmap]]
- [[feroxbuster]]
- [[wireshark]]
- burp
- crackmapexec
- pyinstxtractor
- [[netcat]]

## Services / ports
- [[ssh]] (22)
- [[http]] (80) — Flask application
- websocket (5789) — Python websockets server

## Lessons / notes
- Dynamic analysis of binaries with Wireshark reveals websocket communication
- SQL injection exists over websocket connections, not just HTTP
- SQLite injection uses GROUP_CONCAT for data retrieval
- Username variations from name-anarchy useful for SSH brute forcing
- PyInstaller spec files can include arbitrary files via datas parameter
- Compiled binaries can be extracted with pyinstxtractor
