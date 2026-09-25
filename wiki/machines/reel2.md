---
type: machine
title: Reel2
platform: htb
os: windows
difficulty: hard
tags: [windows, ad, phishing, password-spray, jea, privesc]
solved: 2026-07-09
sources: [[htb-reel2]]
related: []
---
# Reel2
> Windows Active Directory box featuring realistic phishing attack chain: collect usernames from social media, password spray OWA, capture NTLM hash via phishing link, escape JEA limited PowerShell, and abuse custom JEA function to read root flag.

## Attack path
1. [[password-spray]] — Spray OWA with credentials derived from social media usernames
2. [[ntlm-relay]] — Capture NTLM hash via phishing email with link to attacker server
3. [[jea-escape]] — Escape JEA constrained language mode using script blocks
4. [[credential-extraction]] — Extract jea_test_account password from StickyNotes
5. [[jea-abuse]] — Use custom Check-File function to read root flag via path traversal

## Techniques used
- [[password-spray]] — Generated usernames from social media profiles using SprayingToolkit and sprayed OWA with seasonal password
- [[ntlm-relay]] — Sent phishing email from compromised OWA account to capture NTLM hash via responder
- [[hashcat]] — Cracked NTLMv2 hash to get cleartext password
- [[jea-escape]] — Bypassed JEA NoLanguage mode using `&{ script-block }` and function definitions
- [[sticky-notes-creds]] — Extracted credentials from Windows StickyNotes storage in LevelDB
- [[jea-abuse]] — Abused custom Check-File function with path traversal via `C:\ProgramData\..\Users\Administrator\Desktop\root.txt`

## Tools used
- [[nmap]] — Port scanning
- gobuster — Directory brute forcing
- SprayingToolkit — Username generation and password spraying
- evil-winrm — WinRM connection attempts
- [[responder]] — NTLM hash capture
- [[hashcat]] — Hash cracking (mode 5600)
- Nishang — PowerShell reverse shell
- ssh — Shell access

## Services / ports
- [[http]] (80, 8080) — IIS and Apache
- [[https]] (443) — OWA
- [[winrm]] (5985) — WinRM
- rpc — Windows RPC (6000-6017 range)

## Lessons / notes
- JEA has two modes: ConstrainedLanguage (limited but can define functions) and NoLanguage (cannot define functions or access variables)
- JEA escape works by defining functions or using `&{ script-block }` call operator to run blocked commands
- StickyNotes stores data in LevelDB format in `AppData\Roaming\Microsoft\Sticky Notes\Local Storage\leveldb`
- Custom JEA functions can be powerful: Check-File allowed reading any file starting with `C:\ProgramData\*` or `D:\*`, vulnerable to path traversal
- WinRM connection requires `-Authentication Negotiate` when connecting from Linux
- OWA autodiscover reveals internal domain name (HTB) and GAL provides all users for password spraying
