---
type: machine
title: DarkCorp
platform: htb
os: windows
difficulty: insane
tags: [windows, linux, ad, web, insane, multi-host, xss, sql-injection, postgresql-rce, pgp, ntlm-relay, shadow-credentials, upn-spoofing, gpo-abuse, dns-manipulation, kerberos-relay]
solved: 2026-07-09
sources: [[htb-darkcorp]]
related: []
---
# DarkCorp

> Insane difficulty multi-host box with a Debian mail server, Windows domain controller, and Windows web server. Starting with XSS in RoundCube to leak admin credentials and access a development dashboard, then PostgreSQL RCE, PGP-decrypted backup hash cracking, NTLM relay to create DNS records, ADCS abuse for silver tickets, credential recovery, and GPO abuse for complete domain compromise.

## Attack path

1. [[nmap]] port scan → [[ssh]] and [[http]] on Debian host
2. [[ffuf]] subdomain enumeration → discover `mail.drip.htb` RoundCube instance
3. [[xss]] (CVE-2024-42009) in RoundCube → read admin emails → leak `dev-a3f1-01.drip.htb`
4. Password reset via contact form → access development dashboard
5. [[sql-injection]] in PostgreSQL → [[postgresql-rce]] via COPY PROGRAM and archive_command
6. [[gpg]] decrypt backup → crack victor.r hash → [[domain]] credentials
7. [[ntlm-relay]] via monitoring dashboard → create DNS record with CMTI trick
8. [[adcs]] abuse via Kerberos relay → silver ticket for Administrator on WEB-01
9. [[credential-recovery]] via DonPAPI → Administrator password
10. [[shadow-credentials]] → certificate for angela.w.adm
11. [[upn-spoofing]] → access matching `.adm` account on Linux host
12. [[sssd]] cached credentials extraction → domain credentials
13. [[gpo-abuse]] → modify GPO as gpo_manager → complete domain compromise

## Techniques used

- [[xss]] — CVE-2024-42009 exploited to read admin emails from RoundCube webmail
- [[sql-injection]] — PostgreSQL injection in analytics dashboard allows arbitrary query execution
- [[postgresql-rce]] — Two methods: COPY PROGRAM and archive_command modification for reverse shell
- [[pgp-decryption]] — Decrypt PostgreSQL backup using recovered Flask application password
- [[ntlm-relay]] — Relay NTLM authentication from web monitoring dashboard to create malicious DNS records
- [[dns-manipulation]] — CMTI DNS record creation to facilitate Kerberos relay attacks
- [[adcs]] — Certificate enrollment via Kerberos relay for silver ticket generation
- [[credential-recovery]] — DPAPI credential extraction using DonPAPI to recover scheduled task passwords
- [[shadow-credentials]] — ADCS certificate template abuse for privilege escalation
- [[upn-spoofing]] — UPN spoofing to access matching `.adm` account across different systems
- [[sssd]] — Extract cached AD credentials from SSSD database on Linux host
- [[gpo-abuse]] — Modify GPO as gpo_manager to achieve domain administrator privileges

## Tools used

- [[ffuf]] — Subdomain enumeration to discover mail.drip.htb
- [[hydra]] — Username enumeration and password brute force
- [[gpg]] — Decrypt PGP-encrypted PostgreSQL backup file
- [[netexec]] — SMB/LDAP enumeration, NTLM relay, DNS manipulation, DCsync
- [[certipy]] — ADCS certificate enrollment and authentication
- [[impacket]] — Kerberos relay, silver ticket generation, psexec
- [[krbrelayx]] — Kerberos relay to ADCS for silver ticket
- [[ntlmrelayx]] — NTLM relay with MIC removal for LDAP privilege escalation
- [[chisel]] — SOCKS proxy for tunneling through compromised Linux host
- [[dnstool]] — DNS record manipulation for CMTI attacks
- [[godpotato]] — Privilege escalation using SeImpersonatePrivilege
- [[runascs]] — Service logon with full token for privilege escalation
- [[rubeus]] — TGT delegation for ADCS authentication
- [[ticketer]] — Silver ticket creation for local administrator access
- [[donpapi]] — DPAPI credential extraction from Windows hosts

## Services / ports

- 22/tcp [[ssh]] — OpenSSH 9.2p1 Debian (Linux host)
- 80/tcp [[http]] — nginx 1.22.1 hosting RoundCube and Flask application
- 53/tcp [[dns]] — Simple DNS Plus (DC-01)
- 88/tcp [[kerberos]] — Microsoft Windows Kerberos
- 135/tcp [[msrpc]] — Microsoft Windows RPC
- 139/tcp [[netbios-ssn]] — Microsoft Windows NetBIOS
- 389/tcp [[ldap]] — Microsoft Windows Active Directory LDAP
- 445/tcp [[smb]] — Microsoft Windows SMB
- 464/tcp [[kpasswd]] — Kerberos password changing
- 593/tcp [[ncacn_http]] — Microsoft Windows RPC over HTTP
- 636/tcp [[ldapssl]] — Microsoft Windows Active Directory LDAP over SSL
- 1433/tcp [[mssql]] — Microsoft SQL Server 2022 (DC-01)
- 2179/tcp [[vmrdp]] — Hyper-V RDP
- 3268/tcp [[globalcatldap]] — Microsoft Windows Active Directory Global Catalog LDAP
- 3269/tcp [[globalcatldapssl]] — Microsoft Windows Active Directory Global Catalog LDAP over SSL
- 5985/tcp [[winrm]] — Microsoft HTTPAPI httpd 2.0 (WinRM)
- 9389/tcp [[adws]] — Active Directory Web Services
- 5000/tcp [[http]] — Monitoring dashboard with HTTP authentication (WEB-01)

## Lessons / notes

- CVE-2024-42009 in RoundCube allows XSS without user interaction via malformed bgcolor attributes
- PostgreSQL COPY PROGRAM and archive_command are powerful RCE vectors when database has superuser access
- DNS CMTI records enable NTLM relay attacks by embedding target information in the hostname
- Cross-forest trusts provide interesting Kerberos delegation opportunities for silver tickets
- DPAPI-protected credentials can be recovered given sufficient access and master keys
- Shadow credentials provide a modern alternative to traditional Kerberos-based attacks
- UPN spoofing allows cross-system access when accounts have matching usernames across domains
- SSSD cached credentials on Linux hosts can provide Windows domain credentials
- GPO abuse is a powerful domain compromise technique when you have write access
- Multi-host boxes require careful network mapping and pivot planning between different OS environments