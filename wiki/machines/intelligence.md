---
type: machine
title: Intelligence
platform: htb
os: windows
difficulty: medium
tags: [ad, windows, web, ldap, kerberos, dns, snmp, privesc]
solved: 2026-07-09
sources: [[htb-intelligence]]
related: []
---
# Intelligence
> Intelligence is a Windows Active Directory medium box focusing on enumeration and credential abuse. Initial access involves brute-forcing PDF filenames to find a default password, followed by password spraying. Privilege escalation exploits DNS manipulation combined with NTLM relay capture, GMSA password reading, and Kerberos delegation abuse.

## Attack path
1. Brute-force date-based PDF filenames on website to find new user PDFs
2. Extract usernames from PDF metadata and validate via [[kerberos-username-enumeration]]
3. Find default password in PDF and [[password-spray]] across all users
4. Gain SMB access and enumerate domain with [[bloodhound]]
5. Manipulate AD-integrated DNS to add malicious record pointing to attacker IP
6. Capture NTLM hash when scheduled task queries web* DNS records
7. Crack hash and use GMSA password reading capability via [[gmsa-password-read]]
8. Exploit constrained delegation for impersonate attack to DC

## Techniques used
- [[directory-brute-force]] — Date-based PDF filename brute-forcing
- [[kerberos-username-enumeration]] — Username validation via Kerberos
- [[password-spray]] — Default password testing across valid users
- [[ad-dns-manipulation]] — Adding malicious DNS records via LDAP
- [[ntlm-relay]] — Hash capture via Responder when scheduled task runs
- [[gmsa-password-read]] — Reading Group Managed Service Account passwords
- [[constrained-delegation]] — S4U2self/S4U2proxy impersonation attack

## Tools used
- [[nmap]], [[dnsenum]], [[ldapsearch]], [[kerbrute]], [[crackmapexec]], [[smbmap]], [[smbclient]], [[bloodhound]], [[dnstool.py]], [[responder]], [[hashcat]], [[gmsadumper]], [[impacket]]

## Services / ports
- 53/tcp/udp — [[dns]]
- 80/tcp — [[http]] (IIS)
- 88/tcp — [[kerberos]]
- 135/tcp — [[rpc]]
- 139/445/tcp — [[smb]]
- 389/tcp — [[ldap]]
- 636/tcp — [[ldaps]]
- 3268/3269/tcp — Global Catalog LDAP
- 161/udp — [[snmp]]

## Lessons / notes
- PDF metadata can contain valid usernames
- Default passwords are often used in new account creation workflows
- AD-integrated DNS allows record manipulation with appropriate permissions
- GMSA passwords can be read by users/groups with ReadGMSAPassword permission
- Constrained delegation can be exploited for domain compromise
- Scheduled tasks making web requests are useful for NTLM relay capture
