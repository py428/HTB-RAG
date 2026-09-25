---
type: machine
title: Fighter
platform: htb
os: windows
difficulty: insane
tags: [windows, web, active-directory, drivers]
solved: 2026-07-09
sources: [[htb-fighter]]
related: []
---
# Fighter
> A Windows Server 2012 R2 box requiring AppLocker bypass techniques, SQL injection for initial access, Capcom driver exploitation for SYSTEM, and custom password-protected executable for root flag.
## Attack path
1. Enumerate HTTP with [[nmap]], find members subdomain via [[wfuzz]]
2. Exploit [[sqli]] in login form using stacked queries and case-bypass
3. Bypass [[applocker]] using 32-bit PowerShell or extensionless executables
4. Get reverse shell as sqlserv, hijack clean.bat script for decoder user
5. Exploit vulnerable Capcom driver for SYSTEM privileges
6. Reverse engineer root.exe to extract password and get root flag
## Techniques used
- [[sqli]] — Stacked queries with xp_cmdshell for command execution, WAF bypass via case manipulation
- [[applocker]] — Multiple bypass techniques including 32-bit PowerShell, extensionless executables, and trusted directories
- [[script-hijack]] — Hijack scheduled task script execution by modifying file with write permissions
- [[capcom-sys]] — Exploit Capcom driver vulnerability for privilege escalation to SYSTEM
- [[binary-reverse-engineering]] — Analyze compiled executable to extract hardcoded password
## Tools used
- [[nmap]], [[feroxbuster]], [[wfuzz]], [[msfvenom]], [[ghidra]]
- [[powershell]], [[msfconsole]], [[netcat]], [[python]], [[wget]]
## Services / ports
- 80/tcp — [[http]] — Microsoft IIS 8.5 (ASP.NET application)
## Lessons / notes
- AppLocker can be bypassed using 32-bit PowerShell, extensionless files, or trusted directories like color folder
- Capcom driver (capcom.sys) contains arbitrary pointer write vulnerability for privilege escalation
- SQL injection with stacked queries enables xp_cmdshell even when initially disabled
- Binary reverse engineering can reveal hardcoded passwords for custom executables
