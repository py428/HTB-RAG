---
type: machine
title: Mist
platform: htb
os: windows
difficulty: insane
tags: [ad, windows, web, av-evasion, relay]
solved: 2026-07-09
sources: [[htb-mist]]
related: []
---
# Mist

> Mist is an Insane-level Windows Active Directory box that starts with a file disclosure vulnerability in Pluck CMS, progresses through AMSI bypass, PetitPotam LDAP relay, and shadow credential attacks, culminating in ADCS ESC13 exploitation for Domain Administrator access.

## Attack path
1. Exploit CVE-2024-9405 file disclosure in Pluck CMS to recover admin password and upload webshell
2. Overwrite symbolic links in "Common Applications" directory to execute as Brandon.Keywarp
3. Use [[shadow-credentials]] to add certificate-based authentication to Brandon.Keywarp account
4. Employ [[petitpotam]] to coerce MS01$ machine account authentication and relay to LDAP
5. Add shadow credentials to MS01$ using interactive LDAP shell from relayed authentication
6. Use MS01$ shadow credential to obtain machine account NTLM hash via certificate authentication
7. Perform S4U impersonation attack to get Administrator service ticket for MS01
8. Read Sharon.Mullard's KeePass database with partial password disclosure using image analysis
9. Escalate to Administrator using [[adcs]] ESC13 with multiple certificate template abuses

## Techniques used
- [[file-disclosure]] — CVE-2024-9405 in Pluck CMS albums module allows reading arbitrary files without authentication
- [[webshell]] — Upload malicious Pluck CMS module containing PHP webshell for remote code execution
- [[amsi-bypass]] — Modify PowerShell variable names to evade AMSI signature detection
- [[lnk-persistence]] — Overwrite symbolic links in shared directory to achieve execution as different user
- [[shadow-credentials]] — Add KeyCredentialLink attribute to Brandon.Keywarp for certificate-based authentication
- [[petitpotam]] — Coerce MS01$ machine account authentication via MS-EFSRPC for relay attack
- [[ldap-relay]] — Relay machine account authentication to LDAP with shadow credential addition
- [[kerberoasting]] — Request certificate as Brandon.Keywarp and extract NTLM hash using Rubeus
- [[s4u]] — S4U2self impersonation to obtain Administrator service ticket for MS01
- [[keePass-cracking]] — Extract password from KeePass database using partial password from image
- [[adcs]] — ESC13 (SAN exhaustion) and ESC8 abuse for privilege escalation

## Tools used
- [[nmap]] — Port scanning and service enumeration
- [[curl]] — Web shell interaction and HTTP requests
- [[python]] — Web shell and reverse shell creation
- [[netcat]] — Reverse shell listener
- [[feroxbuster]] — Directory brute force on Pluck CMS installation
- [[certify]] — ADCS template enumeration and certificate requests
- [[rubeus]] — Kerberos ticket operations and NTLM hash extraction from certificates
- [[chisel]] — SOCKS proxy tunneling through firewalled networks
- [[petitpotam]] — MS-EFSRPC authentication coercion
- [[ntlmrelayx]] — LDAP relay with interactive shadow credential support
- [[certipy]] — Certificate authentication and NTLM hash extraction
- [[getTGT]] — Kerberos TGT generation from NTLM hashes
- [[wmiexec]] — Windows remote command execution using Kerberos tickets
- [[hashcat]] — KeePass database cracking with partial password hint
- [[bloodhound]] — Active Directory relationship analysis

## Services / ports
- [[http]] (80) — Pluck CMS web application with file disclosure vulnerability
- [[ssh]] (22) — Secure shell access
- [[smb]] (445) — File sharing and domain authentication
- [[dns]] (53) — Domain name services
- [[kerberos]] (88) — Kerberos authentication
- [[ldap]] (389, 636, 3268, 3269) — Directory services
- [[winrm]] (5985) — Windows Remote Management
- [[rpc]] (135) — Remote Procedure Call services

## Lessons / notes
- File disclosure vulnerabilities in CMS modules can expose sensitive configuration and credential files
- AMSI can be bypassed by renaming PowerShell variables to avoid signature detection
- Symbolic links in shared directories can be abused for privilege escalation through user interaction
- Certificate-based authentication (shadow credentials) provides persistence without password knowledge
- PetitPotam can coerce machine account authentication even when webclient service is stopped
- LDAP relay attacks are powerful when LDAP signing is not enforced on domain controllers
- S4U impersonation allows machine accounts to request service tickets as any domain principal
- KeePass databases with partial password disclosure can be cracked using targeted rules
- ADCS ESC vulnerabilities (like ESC13) can be exploited even when templates appear secure at first glance
- Windows Defender exclusions for web directories can be abused to maintain webshell persistence
