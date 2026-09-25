---
type: machine
title: Lantern
platform: htb
os: linux
difficulty: hard
tags: [web, dotnet, SSRF, sql-injection, linux, privesc]
solved: 2026-07-09
sources: [[htb-lantern]]
related: []
---
# Lantern
> Lantern is a hard Linux box featuring Skipper proxy and Blazor applications. The attack path exploits an SSRF vulnerability in Skipper to access an internal Blazor application, performs SQL injection to extract admin credentials or reverse-engineers a DLL, abuses arbitrary file write to upload a malicious Razor component, and uses ProcMon to capture a root password from process monitoring.

## Attack path
1. [[ssrf-skipper]] — Access internal services via X-Skipper-Proxy header
2. [[sql-injection]] — Extract admin password from SQLite database via UNION injection
3. [[dotnet-dll-reversing]] — Alternatively, decode admin password from InternaLantern.dll
4. [[blazor-file-upload]] — Exploit directory traversal in Blazor file upload component
5. [[razor-dll-upload]] — Upload malicious Razor component library for code execution
6. [[procmon-password-capture]] — Monitor process syscalls to extract root password

## Techniques used
- [[ssrf-skipper]] — Exploit CVE-2022-38580 in Skipper proxy via X-Skipper-Proxy header
- [[sql-injection]] — SQLite UNION injection in Blazor application to extract admin credentials
- [[dotnet-dll-reversing]] — Reverse-engineer Blazor DLL to extract base64-encoded credentials
- [[blazor-file-upload]] — Abuses lack of path sanitization in FileUpload.dll for directory traversal
- [[razor-dll-upload]] — Craft malicious Razor Class Library with OnInitialized shell
- [[procmon-password-capture]] — Use ProcMon to monitor write syscalls and capture password input

## Tools used
- [[nmap]]
- [[ffuf]]
- [[feroxbuster]]
- [[sqlite3]]
- [[dotnet]]
- [[curl]]
- [[burp]]
- [[procmon]]
- Visual Studio / DotPeek

## Services / ports
- [[ssh]] (22)
- [[http]] (80)
- Skipper proxy (3000)

## Lessons / notes
- Skipper proxy SSRF allows accessing internal services via X-Skipper-Proxy header
- Blazor uses binary message format—Blazor Traffic Processor Burp extension helps decode
- SQLite client-side runs in browser via WebAssembly
- Razor Class Libraries require .NET 6.0 and specific class name "Component"
- ProcMon for Linux captures process syscalls to SQLite database for later analysis
- Cron job periodically cleans uploaded DLLs from components directory