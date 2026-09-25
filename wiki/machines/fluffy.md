---
type: machine
title: Fluffy
platform: htb
os: windows
difficulty: easy
tags: [windows, ad, cve, smb, winrm, adcs]
solved: 2026-07-09
sources: [[htb-fluffy]]
related: []
---
# Fluffy
> Easy-difficulty Windows AD domain controller starting with user credentials. Exploiting CVE-2025-24071 library-ms vulnerability to capture NetNTLMv2 hash, then using BloodHound to identify GenericWrite privileges over service accounts, leading to shadow credentials abuse and ESC16 ADCS exploit for Administrator access.

## Attack path
1. Start with provided credentials: j.fleischman / J0elTHEM4n1990!
2. Exploit [[cve-2025-24071]] (Windows library-ms vulnerability) to capture NetNTLMv2 hash
3. [[password-cracking]] to crack hash for p.agila
4. [[bloodhound]] analysis to identify GenericWrite over service accounts
5. Add p.agila to Service Accounts group via [[bloodyad]]
6. [[shadow-credentials]] abuse using [[certipy]] to get winrm_svc NTLM hash
7. [[winrm]] access as winrm_svc for user.txt
8. [[esc16]] ADCS exploit using ca_svc certificate enrollment
9. Get Administrator certificate and NTLM hash
10. [[winrm]] as administrator for root.txt

## Techniques used
- [[cve-2025-24071]] — Exploited Windows library-ms vulnerability in zip archives to trigger NTLM authentication to attacker-controlled SMB server
- [[password-cracking]] — Cracked NetNTLMv2 hash using hashcat with rockyou.txt wordlist
- [[bloodhound]] — Analyzed AD permissions to identify attack paths via GenericWrite privileges
- [[acl-genericwrite]] — Abused GenericWrite over service accounts to add shadow credentials
- [[shadow-credentials]] — Used certipy to add Key Credentials to service accounts and retrieve NTLM hashes
- [[esc16]] — Exploited ADCS ESC16 vulnerability where security extension is disabled on CA, allowing UPN manipulation for certificate enrollment
- [[adcs-template-abuse]] — Enrolled in User certificate as modified ca_svc with administrator UPN

## Tools used
- [[nmap]], [[netexec]], [[crackmapexec]]
- [[impacket]], [[bloodyad]], [[bloodhound]]
- [[hashcat]], [[responder]]
- [[certipy]], [[evil-winrm]]

## Services / ports
- [[smb]] (445), [[ldap]] (389/636), [[kerberos]] (88)
- [[winrm]] (5985), DNS (53), RPC (135)
- [[http]] (80) - redirect to HTTPS

## Lessons / notes
- CVE-2025-24071 demonstrates how Windows Explorer processes malicious .library-ms files in zip archives
- BloodHound analysis crucial for identifying service account abuse paths
- Shadow credentials provide a clean way to get NTLM hashes without password changes
- ESC16 is a powerful ADCS exploit when CA security extensions are disabled
- Starting with user credentials in assume-breach scenarios is common in modern AD pentesting
