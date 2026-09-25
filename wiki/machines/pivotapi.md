---
type: machine
title: PivotAPI
platform: htb
os: windows
difficulty: insane
tags: [windows, ad, mssql, winrm, ftp, ssh, ldap, kerberos]
solved: 2026-07-09
sources: [[htb-pivotapi]]
related: []
---
# PivotAPI
> Insane-difficulty Windows Active Directory box centered around multi-stage pivoting through MSSQL, WinRM tunneling, KeePass credential extraction, and eventual LAPS abuse for Domain Administrator access.

## Attack path
1. Enumerate FTP service to find PDF files with [[metadata-analysis]] revealing a username
2. Perform [[as-rep-roasting]] against discovered user to obtain crackable Kerberos ticket
3. Crack AS-REP ticket hash to obtain user credentials
4. Use [[bloodhound]] for AD enumeration and identify further targets
5. Access SMB share and find [[reverse-engineering]] targets in NETLOGON
6. Perform dynamic analysis of obfuscated binaries to extract database credentials
7. Access [[mssql]] service as sa user using derived credentials
8. Tunnel [[winrm]] through MSSQL using [[mssqlproxy]] to bypass firewall restrictions
9. Find [[keepass]] database and crack it to obtain SSH credentials
10. Use SSH access and PowerView to identify [[acl-abuse]] opportunities
11. Progressively compromise users through [[password-reset]] attacks
12. Abuse [[account-operators]] group membership to create new user
13. Add created user to [[laps]] read group to extract local administrator password
14. Access target as local administrator via WinRM to obtain root flag

## Techniques used
- [[as-rep-roasting]] — Used AS-REP roasting against user Kaorz found in PDF metadata to obtain crackable Kerberos TGT
- [[metadata-analysis]] — Extracted username from PDF Publisher field on FTP anonymous share
- [[reverse-engineering]] — Dynamically analyzed obfuscated Windows binaries using Procmon and API Monitor to extract Oracle/MSSQL credentials
- [[mssqlproxy]] — Tunnel WinRM through MSSQL server to bypass firewall restrictions on WinRM access
- [[keepass]] — Extracted and cracked KeePass database to obtain SSH credentials for 3v4Si0N user
- [[acl-abuse]] — Leveraged ForceChangePassword permissions to progressively compromise users through AD tree
- [[account-operators]] — Created new user with Account Operator privileges to access LAPS password
- [[laps]] — Read ms-mcs-admpwd attribute to obtain local administrator password

## Tools used
- [[nmap]] — Port and service scanning identifying AD DC services and additional services like FTP, MSSQL
- [[exiftool]] — PDF metadata analysis to discover username
- [[kerbrute]] — Kerberos username enumeration (though AS-REP was more productive)
- [[hashcat]] — Cracked AS-REP hash using rockyou.txt wordlist
- [[bloodhound]] — AD privilege escalation analysis and attack path identification
- [[smbclient]] — SMB share enumeration and file download from NETLOGON share
- [[mssqlclient]] — MSSQL interaction and xp_cmdshell execution
- [[evil-winrm]] — WinRM shell access through MSSQL tunnel
- [[keepass2john]] — KeePass database hash extraction for cracking
- [[powerview]] — ACL analysis and user password reset operations
- [[proxychains]] — SSH tunneling to access WinRM on localhost
- [[netexec]] — SMB credential validation and password spraying

## Services / ports
- [[ftp]] (21) — Anonymous access exposing PDF files with usernames
- [[ssh]] (22) — Access using various credentials throughout exploitation chain
- [[dns]] (53) — Domain DNS service
- [[kerberos]] (88) — AS-REP roasting attack vector
- [[ldap]] (389, 636, 3268, 3269) — AD directory services and Global Catalog
- [[smb]] (445) — File sharing and NETLOGON access
- [[mssql]] (1433) — Database service with xp_cmdshell enabled for tunneling
- [[winrm]] (5985) — Management interface firewalled to localhost

## Lessons / notes
- The box demonstrates multi-stage AD compromise through credential extraction and progressive ACL abuse
- Firewall rules blocking direct WinRM access required creative MSSQL tunneling using mssqlproxy
- The writeup shows both intended paths and unintended shortcuts using techniques like PrintSpoofer for SeImpersonatePrivilege abuse
- PDF metadata analysis can reveal usernames that aren't exposed through standard enumeration
- AS-REP roasting remains valuable when users have UF_DONT_REQUIRE_PREAUTH set
- LAPS provides local administrator passwords but requires proper group membership to access
- Progressive ACL abuse through ForceChangePassword allows horizontal movement without knowing target passwords
- Account Operators group membership provides powerful AD object creation capabilities