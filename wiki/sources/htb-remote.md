---
type: source
title: "HTB Remote writeup"
raw: raw/htb-remote.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[remote]]
---
# Source: HTB Remote writeup
> Complete walkthrough for the Remote HackTheBox machine demonstrating NFS enumeration, hash cracking, CMS exploitation, and Windows registry credential extraction.

## Key facts extracted
- NFS share site_backups accessible without authentication
- Umbraco.sdf database contains admin credentials with SHA1 hashes
- TeamViewer 7 stores encrypted passwords in HKLM\SOFTWARE\WOW6432Node\TeamViewer\Version7
- Static AES-128-CBC key/IV used for TeamViewer password decryption
- Administrator account in Remote Management Users group
- Multiple shell options available via WinRM, PSExec, and WMIExec

## Filed into
[[remote]], [[nfs-enumeration]], [[hash-cracking]], [[cms-exploit]], [[registry-password-extraction]]
