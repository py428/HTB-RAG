---
type: machine
title: Dropzone
platform: htb
os: windows
difficulty: hard
tags: [windows, web, privesc, tftp, wmi, mof]
solved: 2026-07-09
sources: [[htb-dropzone]]
related: []
---
# Dropzone
> Windows XP box with no TCP ports open, only unauthenticated TFTP on UDP 69. Exploit via MOF file WMI code execution using TFTP to drop malicious file that auto-compiles, giving SYSTEM shell. Flags hidden in NTFS alternate data streams.

## Attack path
1. [[tftp]] — Upload malicious MOF file and tools via unauthenticated TFTP on UDP 69
2. [[mof-wmi]] — Drop MOF file to auto-compile directory for SYSTEM code execution
3. [[alternative-data-streams]] — Extract flags from ADS of text files on desktop

## Techniques used
- [[tftp]] — Unauthenticated TFTP on UDP 69 for file upload/download to Windows XP system root
- [[mof-wmi]] — WMI MOF file auto-compilation in `wbem\mof\` directory for code execution as SYSTEM (similar to Stuxnet MS10-061 technique)
- [[alternative-data-streams]] — Flags stored in NTFS alternate data streams of desktop files

## Tools used
[[nmap]], tftp, netcat, whoami, streams

## Services / ports
[[tftp]] (UDP 69)

## Lessons / notes
- TFTP allowed writing to system32 and reading files, indicating privileged access
- MOF files define WMI events/filters/consumers and auto-compile when dropped in wbem\mof\ directory
- Used Stuxnet-inspired technique: write malicious MOF to trigger automatic code execution
- Alternative data streams (ADS) used to hide flags in NTFS file system
- Windows XP lacks modern tools like PowerShell for ADS enumeration, required streams.exe
