---
type: source
title: "HTB Lantern writeup"
raw: raw/htb-lantern.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[lantern]]
---
# Source: HTB Lantern writeup
> In-depth guide to exploiting Lantern, a hard HTB box with complex web application stack. Covers SSRF in Skipper proxy, Blazor application exploitation, SQL injection, .NET DLL reversing, malicious Razor component upload, and ProcMon-based password interception for privilege escalation.

## Key facts extracted
- **Skipper SSRF**: CVE-2022-38580 allows accessing internal services via X-Skipper-Proxy header
- **Internal services**: Port 5000 hosts InternaLantern Blazor WebAssembly app with SQLite
- **SQL injection**: Vacation booking form vulnerable to UNION-based SQLite injection
- **DLL credentials**: InternaLantern.dll contains base64-encoded admin password in OnInitializedAsync
- **File upload**: FileUpload.dll vulnerable to directory traversal via filename manipulation
- **Razor exploit**: Requires .NET 6.0, class named "Component", inheriting ComponentBase
- **ProcMon privesc**: sudo access to ProcMon allows capturing nano write syscalls containing password
- **Blazor messages**: Binary format decoded with Blazor Traffic Processor Burp extension

## Filed into
[[lantern]], [[ssrf-skipper]], [[sql-injection]], [[dotnet-dll-reversing]], [[blazor-file-upload]], [[razor-dll-upload]], [[procmon-password-capture]]