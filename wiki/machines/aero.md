---
type: machine
title: Aero
platform: htb
os: windows
difficulty: medium
tags: [windows, web, cve, kernel, rce]
solved: 2026-07-09
sources: [[htb-aero]]
related: []
---
# Aero
> A Windows box showcasing two critical CVEs: ThemeBleed (CVE-2023-38146) for initial access via malicious theme files, and a Windows kernel CLFS exploit (CVE-2023-28252) for privilege escalation.

## Attack path
1. [[themebseed]] (CVE-2023-38146) exploitation via malicious .theme file upload
2. Custom DLL payload with reverse shell exploiting theme validation race condition
3. [[kernel-clfs-exploit]] (CVE-2023-28252) for privilege escalation to SYSTEM

## Techniques used
- [[themebseed]] — CVE-2023-38146 race condition in Windows theme signature verification
- [[dll-reverse-shell]] — Custom DLL with VerifyThemeVersion export for theme exploit
- [[kernel-clfs-exploit]] — CVE-2023-28252 Common Log File System kernel vulnerability

## Tools used
[[nmap]] [[feroxbuster]] Visual Studio ThemeBleed POC netcat

## Services / ports
- [[http]] 80 — Microsoft IIS 10.0 with theme upload functionality

## Lessons / notes
- Windows theme files (.theme) can contain malicious .msstyles references with _vrf.dll
- ThemeBleed exploits a race condition between signature check and DLL loading
- Building custom DLL payloads requires Visual Studio and proper export function naming
- Windows kernel CLFS exploit requires precise memory layout and token manipulation
- The box demonstrates the importance of patching Windows themes and kernel vulnerabilities

## CVEs
- CVE-2023-38146 (ThemeBleed)
- CVE-2023-28252 (CLFS kernel exploit)
