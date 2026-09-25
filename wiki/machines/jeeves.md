---
type: machine
title: Jeeves
platform: htb
os: windows
difficulty: medium
tags: [windows, web, jenkins, privesc]
solved: 2026-07-09
sources: [[htb-jeeves]]
related: []
---
# Jeeves
> Medium Windows machine featuring an unauthenticated Jenkins instance, KeePass database exfiltration, and pass-the-hash for privilege escalation. The final flag is hidden in an NTFS alternate data stream.

## Attack path
1. Unauthenticated [[jenkins-rce]] via job or script console
2. Exfiltrate CEH.kdbx KeePass database from kohsuke user
3. Crack master password and extract Administrator NT hash
4. [[pass-the-hash]] with psexec for SYSTEM shell
5. Find root.txt in NTFS alternate data stream

## Techniques used
- [[jenkins-rce]] — No authentication required, create job with Windows batch command or use Script Console with Groovy
- [[keepass-cracking]] — keepass2john + hashcat to crack master password "moonshine1"
- [[pass-the-hash]] — Administrator NT hash e0fb1fb85756c24235ff238cbe81fe00 from KeePass backup entry
- [[alternate-data-stream]] — Windows ADS: `more < hm.txt:root.txt` reads hidden stream

## Tools used
[[nmap]], [[feroxbuster]], gobuster, nc, [[hashcat]], crackmapexec, [[psexec]] (impacket), kpcli, keepass2john

## Services / ports
[[http]] (80), [[smb]] (445), jetty (50000)

## Lessons / notes
- Jenkins on port 50000 accessible via /askjeeves, no authentication configured
- Groovy Script Console: `println "cmd.exe /c whoami".execute().text`
- Alternative data streams: `dir /R` shows streams, `more < file:stream` reads contents
- Windows LM hash aad3b435b51404eeaad3b435b51404ee indicates empty password (ignored)
- Pass-the-hash works with Administrator hash even without LM component
- KeePass "Backup stuff" entry contained NT hash, not cleartext password
