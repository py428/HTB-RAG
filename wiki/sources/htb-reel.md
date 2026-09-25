---
type: source
title: "HTB Reel writeup"
raw: raw/htb-reel.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[reel]]
---
# Source: HTB Reel writeup
> Comprehensive phishing and Active Directory attack chain covering anonymous FTP reconnaissance, malicious RTF creation with CVE-2017-0199, PowerShell credential extraction, and BloodHound-guided ACL abuse to escalate from nico to Domain Admin.

## Key facts extracted
- Anonymous FTP provides documents including nico@megabank.com email address
- SMTP VRFY enumeration accepts any @htb.local address but validates @megabank.com users
- CVE-2017-0199 RTF exploit with HTA payload executed when opened by nico
- PowerShell credentials stored in cred.xml using Export-CliXml with reversible encryption
- BloodHound analysis shows WriteOwner and WriteDacl ACLs allowing privilege escalation
- Backup_Admins group can access Administrator desktop but root.txt protected by DENY ACL
- Attachment opening automation via AutoHotKey script to accept warnings every 6 seconds

## Filed into
[[reel]], [[ftp-anonymous]], [[smtp-enum]], [[rtf-exploit]], [[pscredential-extraction]], [[bloodhound]], [[acl-writeowner]], [[acl-genericwrite]], [[acl-genericall]]
