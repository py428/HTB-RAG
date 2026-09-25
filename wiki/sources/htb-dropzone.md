---
type: source
title: "HTB Dropzone writeup"
raw: raw/htb-dropzone.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[dropzone]]
---
# Source: HTB Dropzone writeup
> Windows XP hard box featuring TFTP-only access and WMI MOF file exploitation for code execution. Writeup covers MOF file compilation technique, alternative data streams for flag extraction, and detailed WMI background.

## Key facts extracted
- No TCP ports open, only unauthenticated TFTP on UDP 69
- Windows XP SP3 identified from license.rtf file
- TFTP allowed file upload/download to C:\ root and system32
- MOF files in wbem\mof\ directory auto-compile via mofcomp.exe
- Flags stored in NTFS alternate data streams of desktop files
- Used nc.exe for reverse shell and streams.exe for ADS enumeration

## Filed into
[[dropzone]], [[tftp]], [[mof-wmi]], [[alternative-data-streams]]
