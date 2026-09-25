---
type: source
title: "HTB Aero writeup"
raw: raw/htb-aero.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[aero]]
---
# Source: HTB Aero writeup
> Technical analysis of exploiting Aero, a Windows HackTheBox machine demonstrating ThemeBleed (CVE-2023-38146) and Windows CLFS kernel exploit (CVE-2023-28252) for complete system compromise.

## Key facts extracted
- ThemeBleed (CVE-2023-38146) allows RCE via malicious .theme files
- Windows 11 Build 22000 missing KB5025224 patch for CVE-2023-28252
- Custom DLL payload requires VerifyThemeVersion export function
- CLFS exploit uses Common Log File System vulnerability for kernel privilege escalation
- Theme upload functionality processes uploaded files automatically via PowerShell FileSystemWatcher

## Filed into
[[aero]], [[themebseed]], [[kernel-clfs-exploit]], [[dll-reverse-shell]]
