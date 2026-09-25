---
type: source
title: "HTB Hathor writeup"
raw: raw/htb-hathor.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[hathor]]
---
# Source: HTB Hathor writeup
> Insane difficulty Active Directory exploitation involving mojoPortal, AppLocker bypasses, code signing certificate abuse, and DCSync for domain domination.

## Key facts extracted
- mojoPortal default credentials admin@admin.com/admin for admin access
- AppLocker blocks unsigned binaries except whitelisted paths like `C:\share\Bginfo64.exe` and specific DLLs
- AutoIt scheduled task loads `C:\share\scripts\7-zip64.dll` every 3 minutes
- Code signing certificate with "abceasyas123" password found in recycle bin
- Get-bADpasswords scheduled task runs as bpassrunner with Domain Admin privileges
- NTLM authentication disabled for Protected Users, requiring Kerberos authentication
- DCSync possible from bpassrunner account due to domain-level permissions

## Filed into
[[hathor]], [[webshell]], [[dll-hijacking]], [[applocker]], [[code-signing]], [[crackpkcs12]], [[dcsync]], [[kerberos]], [[ntlm-disabled-protected-users]]
