---
type: machine
title: Reel
platform: htb
os: windows
difficulty: hard
tags: [windows, ad, phishing, rt, privesc, acl-abuse]
solved: 2026-07-09
sources: [[htb-reel]]
related: []
---
# Reel
> Classic Windows AD phishing box: anonymous FTP provides documents for malicious RTF creation, CVE-2017-0199 exploit gains initial foothold, then chain through AD users exploiting ACL abuse (WriteOwner, WriteDacl) to reach Domain Admin.

## Attack path
1. [[ftp-anonymous]] — Anonymous FTP access provides documents and email addresses
2. [[rtf-exploit]] — CVE-2017-0199 malicious RTF with HTA payload for reverse shell
3. [[pscredential-extraction]] — Extract credentials from Export-CliXml file
4. [[acl-writeowner]] — Use WriteOwner to take ownership of claire's user object
5. [[acl-genericwrite]] — Grant ResetPassword permission on claire's account
6. [[acl-genericall]] — Add claire to Backup_Admins group via WriteDacl
7. [[password-reuse]] — Extract admin password from backup script

## Techniques used
- [[smtp-enum]] — SMTP VRFY enumeration to identify valid users (accepts @htb.local, rejects @megabank.com except nico)
- [[rtf-exploit]] — CVE-2017-0199 RTF exploit with embedded HTA payload for reverse shell as nico
- [[pscredential-extraction]] — Import-CliXml to decrypt stored PowerShell credentials for tom
- [[bloodhound]] — Analyze ACL relationships to identify attack paths (tom→claire→Backup_Admins)
- [[acl-writeowner]] — Set-DomainObjectOwner to become owner of claire's user object
- [[acl-genericwrite]] — Add-DomainObjectAcl to grant password reset permission on claire
- [[acl-genericall]] — WriteDacl abuse to add self to Backup_Admins group
- [[password-reuse]] — Found admin password in backup script on Administrator desktop

## Tools used
- [[nmap]] — Port scanning
- smtp-user-enum — SMTP user enumeration
- sendEmail — Email sending with attachment
- CVE-2017-0199 toolkit — Malicious RTF generation
- Metasploit — Alternative RTF exploit generation
- PowerView — AD enumeration and ACL abuse
- BloodHound — ACL relationship analysis
- ssh — Shell access
- [[exiftool]] — Document metadata extraction

## Services / ports
- [[ftp]] (21) — Anonymous FTP
- [[ssh]] (22) — SSH access
- [[smtp]] (25) — SMTP with VRFY enumeration

## Lessons / notes
- CVE-2017-0199 works with Wordpad but not CVE-2017-8759 or CVE-2017-11826 due to how attachments are opened
- Attachment opening automation: AutoHotKey script to ALT+TAB and press space every 6 seconds to accept warnings
- Email attachments processed from C:\Users\nico\Documents\Attachments to Processed every 6 seconds
- Cleanup script deletes processed RTF/DOC files but doesn't check subdirectories
- ACL abuse path: WriteOwner → become owner → Add-DomainObjectAcl with ResetPassword → Set-DomainUserPassword
- Backup_Admins group has full access to Administrator desktop but root.txt has explicit DENY ACL for Backup_Admins
- OST file analysis (readpst) revealed unused second path with Julia's credentials
