---
type: machine
title: Cereal
platform: htb
os: windows
difficulty: hard
tags: [windows, web, git, jwt, deserialization, xss, graphql, potato, privesc]
solved: 2026-07-09
sources: [[htb-cereal]]
related: []
---
# Cereal
> Cereal is a C#/.NET backend with React frontend where I'll leak the JWT signing key from Git history, forge tokens to bypass authentication, chain XSS with deserialization to upload a webshell, crack hashes from the SQLite database, and exploit a GraphQL SSRF with GenericPotato to get SYSTEM.

## Attack path
1. Access [[git-exposure]] on source.cereal.htb to find JWT secret
2. Forge [[jwt-forging]] to bypass authentication
3. Submit XSS cereal request to trigger admin viewing
4. Chain [[xss]] with [[deserialization]] to upload ASPX webshell via DownloadHelper
5. Extract SQLite database with sonny credentials
6. Exploit [[graphql-ssrf]] with [[generic-potato]] for SYSTEM

## Techniques used
- [[git-exposure]] — Download .git directory with gitdumper to access source code
- [[jwt-forging]] — Create JWT tokens with leaked secret key from git history
- [[xss]] — Stored XSS in cereal title via react-marked-markdown vulnerability (CVE-668)
- [[deserialization]] — JSON.NET TypeNameHandling.Auto with DownloadHelper gadget
- [[sqlite-sqli]] — Read SQLite database at C:\inetpub\cereal\db\cereal.db
- [[hash-cracking]] — Crack MD5 hash from Users table
- [[graphql-ssrf]] — updatePlant mutation with sourceURL parameter for SSRF
- [[generic-potato]] — Use SSRF to impersonate SYSTEM token via named pipe
- [[named-pipe-impersonation]] — Abuse SeImpersonatePrivilege with HTTP listener

## Tools used
- [[nmap]]
- gitdumper
- jwt python library
- [[curl]]
- react-marked-markdown exploit
- ysoserial (blocked, custom gadget)
- sqlite3
- hashcat
- [[ssh]]
- graphql-playground
- GenericPotato

## Services / ports
- [[ssh]] (22)
- [[http]] (80, 443)
- internal [[http]] (8080)
- [[winrm]] (5985)

## Lessons / notes
- .NET application with React frontend
- Exposed .git on source.cereal.htb
- JWT secret: secretlhfIH&FY*#oysuflkhskjfhefesf
- IP whitelist (127.0.0.1, ::1) on /requests endpoints
- DownloadHelper class with URL/FilePath auto-download
- XSS via react-marked-markdown sanitize bypass
- sonny/mutual.madden.manner38974 credentials
- Windows Server Core without Print Spooler
- GraphQL on localhost:8080 with updatePlant mutation
- SeImpersonatePrivilege enabled but TCP 135 blocked
- GenericPotato works with HTTP SSRF instead of DCOM

## CVEs
- CVE-668 (react-marked-markdown XSS)
