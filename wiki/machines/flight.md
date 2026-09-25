---
type: machine
title: Flight
platform: htb
os: windows
difficulty: hard
tags: [windows, ad, web, rfi, sqli, smb, winrm]
solved: 2026-07-09
sources: [[htb-flight]]
related: []
---
# Flight
> Windows Active Directory box featuring multiple web vulnerabilities leading to domain compromise. Exploiting PHP file inclusion on an internal site to capture NetNTLMv2 hashes, password spraying across domain users, leveraging webshells for initial access, then abusing Kerberos delegation and DCSync for privilege escalation.

## Attack path
1. [[sqli]] on school.flight.htb PHP application to read files
2. Capture [[netntlm-relay]] (SMB hash capture) via file inclusion
3. [[password-cracking]] to crack NetNTLMv2 hash  
4. [[kerberos-username-enumeration]] via RPC to list domain users
5. [[password-spray]] cracked password across users
6. Upload malicious files to SMB share to capture another NetNTLMv2 hash
7. Crack hash to get new user credentials
8. [[webshell]] upload via SMB share (PHP)
9. [[runascs]] to lateral move to user with write access
10. [[port-forwarding]] with [[chisel]] to access internal IIS site
11. [[webshell]] upload via SMB (ASPX)
12. [[kerberos-relay]] (machine account delegation abuse) with [[rubeus]]
13. [[dcsync]] to dump NTDS and get Administrator hash
14. [[psexec]] for SYSTEM shell

## Techniques used
- [[sqli]] — Union-based SQL injection on cancellation page to enumerate database and extract credentials
- [[netntlm-relay]] — Captured NetNTLMv2 hashes by triggering SMB authentication via PHP file inclusion vulnerability
- [[password-cracking]] — Cracked NetNTLMv2 hashes using hashcat with rockyou.txt wordlist
- [[kerberos-username-enumeration]] — Enumerated domain users using Impacket's lookupsid.py via RPC
- [[password-spray]] — Reused cracked password across multiple domain users to find additional access
- [[webshell]] — Uploaded PHP and ASPX webshells via SMB shares with write permissions
- [[runascs]] — Lateral movement using RunasCs to authenticate as another user with explicit credentials
- [[port-forwarding]] — Used Chisel to tunnel internal IIS development site through existing SSH session
- [[kerberos-relay]] — Abused Kerberos delegation to get machine account ticket from IIS application pool identity
- [[dcsync]] — Used machine account credentials to DCSync domain and extract Administrator NTLM hash
- [[psexec]] — Pass-the-hash attack using Administrator credentials for remote code execution

## Tools used
- [[nmap]], [[feroxbuster]], [[crackmapexec]], [[netexec]]
- [[impacket]] (lookupsid.py, secretsdump.py, psexec.py)
- [[hashcat]], [[john]]
- [[smbclient]], [[smbmap]], [[responder]]
- [[rubeus]], [[runascs]], [[evil-winrm]]
- [[chisel]]

## Services / ports
- [[smb]] (445), [[ldap]] (389/636), [[kerberos]] (88)
- [[http]] (80 - Apache), [[http]] (8000 - IIS), [[winrm]] (5985)
- DNS (53), RPC (135)

## Lessons / notes
- Chain of file inclusion → hash capture → credential reuse is common in AD environments
- Web applications often have access to interesting SMB shares for file operations
- IIS application pool identities authenticate as machine accounts over the network
- Machine account tickets can be requested via Kerberos delegation (tgtdeleg)
- DCSync requires privileged access but provides complete domain compromise
