---
type: machine
title: Search
platform: htb
os: windows
difficulty: hard
tags: [ad, windows, kerberos, ldap, bloodhound]
solved: 2026-07-09
sources: [[htb-search]]
related: []
---
# Search
> Search is a hard Active Directory Windows box demonstrating credential extraction from images, Kerberoasting, password spraying, Excel file analysis, certificate-based authentication, and GMSA abuse. The attack involves finding credentials in website images, Kerberoasting a service account, password reuse across users, extracting passwords from protected Excel worksheets, using client certificates for PowerShell Web Access, and finally leveraging GMSA password read access to compromise a domain admin.

## Attack path
1. [[nmap]] enumeration reveals comprehensive AD services including DNS, Kerberos, LDAP, SMB
2. Extract credentials from website image - "Hope Sharp" with password "IsolationIsKey?"
3. Use [[ldapsearch]] with Hope Sharp credentials to enumerate domain users and groups
4. [[bloodhound]] analysis reveals Kerberoastable service account web_svc
5. Perform [[kerberoasting]] with GetUserSPNs and crack hash with [[hashcat]] to obtain web_svc password
6. Spray web_svc password across domain users - find Edgar.Jacobs credential reuse
7. Extract protected Excel worksheet from SMB share and crack sheet protection password
8. Obtain credentials for Sierra.Frye from Excel file and access user.txt
9. Find client certificates in Sierra.Frye downloads, crack PFX passwords with [[john]]
10. Use certificates for client certificate authentication to PowerShell Web Access at /staff
11. [[bloodhound]] analysis shows Sierra.Frye can read GMSA BIR-ADFS-GMSA password
12. Extract GMSA password and use it to reset Domain Admin Tristan.Davies password
13. Access Domain Admin via [[wmiexec]] and obtain root.txt

## Techniques used
- [[image-metadata-extraction]] — Credentials found in image text on website
- [[kerberoasting]] — Extract and crack Kerberos service ticket for web_svc account
- [[password-spraying]] — Test shared passwords across multiple domain accounts
- [[excel-password-extraction]] — Extract passwords from protected Excel worksheets by manipulating XML
- [[certificate-authentication]] — Use cracked client certificates for PowerShell Web Access
- [[gmsa-password-recovery]] — Extract Group Managed Service Account password using AD PowerShell cmdlets

## Tools used
[[nmap]], [[feroxbuster]], [[crackmapexec]], [[ldapsearch]], [[bloodhound]], [[GetUserSPNs]], [[hashcat]], [[john]], [[wmiexec]]

## Services / ports
53/tcp — DNS, 88/tcp — [[kerberos]], 389/tcp — [[ldap]], 443/tcp — HTTPS, 445/tcp — SMB

## Lessons / notes
- Images on websites may contain sensitive information including credentials
- Kerberoasting works even when SPN accounts have never logged in
- Excel sheet protection can be removed by deleting protection tags in the XML structure
- Client certificate authentication can bypass standard username/password forms
- GMSA passwords can be retrieved by accounts with ReadGMSAPassword permission
- Bloodhound is essential for identifying complex AD attack paths involving GMSA accounts
