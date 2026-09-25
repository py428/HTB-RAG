---
type: machine
title: Bagel
platform: htb
os: linux
difficulty: medium
tags: [dotnet, flask, json-deserialization, file-read, sudo]
solved: 2026-07-09
sources: [[htb-bagel]]
related: []
---
# Bagel

> Bagel features a Flask frontend and .NET backend connected via websocket. I'll exploit file read in Flask to access the .NET DLL, reverse engineer it to find JSON deserialization vulnerability, abuse it for file read to get SSH key, then exploit sudo dotnet for root.

## Attack path
1. Exploit [[path-traversal]] in Flask application to read arbitrary files
2. Use file read to download and analyze .NET DLL binary
3. Discover [[json-deserialization]] vulnerability with TypeNameHandling Auto
4. Craft malicious payload to read SSH private key via deserialization
5. Authenticate via SSH and pivot to developer user using credentials from DLL
6. Exploit [[sudo-dotnet]] rule to execute arbitrary commands as root

## Techniques used
- [[path-traversal]] — Abusing ?page= parameter to read files via send_file
- [[binary-reverse-engineering]] — Decompling .NET DLL with dnSpy to find vulnerabilities
- [[json-deserialization]] — Exploiting TypeNameHandling Auto to instantiate arbitrary objects
- [[file-read]] — Using crafted JSON payloads to read arbitrary files via File class
- [[sudo-dotnet]] — Abusing sudo dotnet fsi for F# interactive execution as root

## Tools used
[[nmap]], [[feroxbuster]], [[ffuf]], [[wscat]], dnSpy, [[curl]], [[jq]]

## Services / ports
[[ssh]] (22), [[http]] (5000 - .NET), [[http]] (8000 - Flask)

## Lessons / notes
- Flask send_file with user-controlled paths is vulnerable to path traversal
- .NET applications can be decompiled to source-like code with dnSpy
- JSON deserialization with TypeNameHandling Auto is a critical vulnerability
- WebSocket protocols require manual frame construction for exploitation
- Sudo rules allowing dotnet execution can be abused via fsi interactive shell
