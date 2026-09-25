---
type: machine
title: VulnEscape
platform: htb
os: windows
difficulty: easy
tags: [windows, rdp, kiosk, privesc, gui]
solved: 2026-07-09
sources: [[htb-vulnescape]]
related: []
---
# VulnEscape
> VulnEscape is an easy Windows box that starts with RDP access using a kiosk account with no password. The kiosk mode runs Edge in full screen, which I'll exploit to access the filesystem, download cmd.exe, rename it to msedge.exe to bypass application allow lists, then use BulletsPassView to recover an admin password from a Remote Desktop Plus profile file, and finally bypass UAC to get SYSTEM access.

## Attack path
1. Connect to [[rdp]] as KioskUser0 with empty password
2. Exploit kiosk mode by opening Edge and accessing C: drive via URL bar
3. Download cmd.exe to Downloads folder and rename to msedge.exe to bypass allow list
4. Use BulletsPassView to recover admin password from Remote Desktop Plus profile
5. Use runas as admin user with password, bypass [[uac-bypass]] for full privileges
6. Access Administrator desktop for root flag

## Techniques used
- [[kiosk-escape]] — Breaking out of restricted kiosk mode via Edge browser filesystem access
- [[file-renaming-bypass]] — Renaming cmd.exe to msedge.exe to bypass application allow lists
- [[password-recovery]] — Using BulletsPassView to extract password from obfuscated dots in GUI
- [[uac-bypass]] — Bypassing User Account Control via interactive prompt approval

## Tools used
- [[nmap]] — Port scanning and service enumeration
- xfreerdp — RDP client for Linux
- bulletsview — NirSoft tool to reveal passwords behind asterisk/bullet characters
- smbserver.py (impacket) — File transfer for BulletsPassView tool
- runas — Alternate credential execution

## Services / ports
- 3389/tcp — [[rdp]] (Microsoft Terminal Services)

## Lessons / notes
- Kiosk mode escape: Edge browser can access local filesystem via C: URL or file:// protocol
- Application allow lists: Often based on filename; renaming trusted executables bypasses restrictions
- Password recovery: GUI tools like BulletsPassView can reveal passwords behind obfuscated characters
- UAC bypass: Interactive approval prompts can be triggered with runas /savedcred or similar techniques
- RDP kiosk deployments: Common in enterprise environments but often escape-prone via browser access
- Language settings: Korean locale may require AI translation for error messages and interface elements
