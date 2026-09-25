---
type: machine
title: Sunday
platform: htb
os: solaris
difficulty: easy
tags: [solaris, finger, privesc, password-cracking, wget, sudo-abuse]
solved: 2026-07-09
sources: [[htb-sunday]]
related: []
---
# Sunday
> Solaris box with finger service for user enumeration and password cracking for user escalation, then multiple wget privilege escalation vectors for root access.
## Attack path
1. [[finger-enum]] to enumerate users (sunny, sammy)
2. [[password-cracking]] — shadow.backup hash cracking with hashcat
3. [[password-reuse]] — sammy's credentials work for SSH
4. [[sudo-abuse]] — wget with multiple privilege escalation techniques
## Techniques used
- [[finger-enum]] — User enumeration via finger protocol and brute forcing
- [[password-cracking]] — Solaris shadow file hashes (SHA-256) cracked with hashcat
- [[sudo-abuse]] — wget allows multiple privilege escalation techniques:
  - `--input-file` to read protected files
  - `--post-file` to exfiltrate data
  - `-O` to overwrite binaries (troll, passwd, shadow, sudoers)
## Tools used
- [[nmap]] — port scanning (79, 111, 22022, 65258)
- finger-user-enum.pl — username brute forcing
- [[hashcat]] — shadow file hash cracking (mode 7400)
- [[ssh]] — access with sammy credentials
- [[wget]] — privilege escalation via multiple techniques
- [[netcat]] — reverse shell and data exfiltration
## Services / ports
- finger (79) — User enumeration service
- rpcbind (111) — RPC service
- ssh (22022) — Non-standard SSH port
- smserverd (65258) — SMB/RPC service
## Lessons / notes
- Solaris finger service allows user enumeration and authentication timing attacks
- Solaris uses different hash format than Linux (requires mode 7400 in hashcat)
- wget offers multiple privilege escalation vectors beyond file writing
- Overwrite scripts can reset privileged binaries, requiring race conditions
- Solaris system uses different paths and commands than Linux
- finger protocol can be used for file transfer in both directions
