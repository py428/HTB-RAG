---
type: source
title: "HTB VulnEscape writeup"
raw: raw/htb-vulnescape.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[vulnescape]]
---
# Source: HTB VulnEscape writeup
> 0xdf's complete writeup for HTB VulnEscape covering RDP kiosk mode escape, filesystem access via Edge browser, application allow list bypass through file renaming, password recovery using BulletsPassView, and UAC bypass for SYSTEM access.

## Key facts extracted
- KioskUser0 account: Empty password, restricted to Edge browser kiosk mode
- Edge escape: Access C: drive via URL bar to download and execute cmd.exe as msedge.exe
- Application allow list: Bypassed by renaming executables to allowed names (msedge.exe)
- Remote Desktop Plus: Stores admin credentials in C:\_admin\profiles.xml
- BulletsPassView: Recovers password from GUI password field obfuscated with bullets
- UAC bypass: Interactive approval via start-process powershell.exe -verb runas
- Language: Entire interface in Korean, requiring translation for understanding

## Filed into
[[vulnescape]], [[kiosk-escape]], [[file-renaming-bypass]], [[password-recovery]], [[uac-bypass]]
