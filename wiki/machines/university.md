---
type: machine
title: University
platform: htb
os: windows
difficulty: insane
tags: [ad, web, python, relay, kerberos, wpad, rbcd]
solved: 2026-07-09
sources: [[htb-university]]
related: []
---
# University
> Insane Windows Active Directory box featuring CVE-2023-33733 RCE, certificate abuse, WPAD spoofing, relay attacks, RBCD, unconstrained delegation, GMSA abuse, and multi-tier escalation.

## Attack path
1. [[cve-2023-33733]] in ReportLab PDF generation for initial shell
2. [[certificate-abuse]] by forging professor login certificates
3. [[wpad-spoofing]] to trigger authentication from internal systems
4. [[ntlm-relay]] for RBCD configuration on WS-3$
5. [[kerberos-delegation]] abuse using Rubeus to dump tickets
6. [[gmsa-abuse]] to read GMSA-PClient01$ password
7. [[rbcd]] from GMSA-PClient01$ to DC for DA access

## Techniques used
- [[cve-2023-33733]] — ReportLab PDF generation RCE via Python code injection
- [[certificate-abuse]] — Forged professor certificates using stolen CA keys
- [[open-redirect]] — /redirect endpoint abused for JWKS hosting
- [[malicious-file-upload]] — URL files in lecture packages for execution
- [[wpad-spoofing]] — mitm6 to poison WPAD DNS requests
- [[ntlm-relay]] — ntlmrelayx to relay WS-3$ authentication for RBCD
- [[rbcd]] — Resource-based constrained delegation abuse
- [[unconstrained-delegation]] — Ticket dumping from WS-3 memory
- [[gmsa-abuse]] — Reading GMSA password for domain escalation
- [[s4u2proxy]] — Kerberos S4U2Proxy for impersonation

## Tools used
- [[nmap]]
- [[netexec]]
- [[bloodhound]]
- [[chisel]]
- mitm6
- ntlmrelayx
- Rubeus
- addcomputer.py
- getST.py
- [[evil-winrm]]
- [[msfvenom]]

## Services / ports
- [[dns]] — TCP/UDP 53
- [[kerberos]] — TCP 88
- [[ldap]] — TCP 389, 636, 3268, 3269
- [[smb]] — TCP 445
- [[http]] — TCP 80, 5985
- [[winrm]] — TCP 5985

## Lessons / notes
- Multi-tier AD environments require careful enumeration of all hosts
- Internal networks may need tunneling (Chisel) for access
- WPAD spoofing works even without internet access
- RBCD requires creating fake computer accounts or relaying to existing ones
- Unconstrained delegation allows TGT dumping from memory
- GMSA passwords can be read by Account Operators
- Certificate systems with accessible CA keys allow complete compromise
- UHC (Ultimate Hacking Championship) qualifier boxes are non-competitive

## CVEs
- CVE-2023-33733 — ReportLab PDF generation RCE
