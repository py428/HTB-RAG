---
type: source
title: "HTB TombWatcher writeup"
raw: raw/htb-tombwatcher.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[tombwatcher]]
---
# Source: HTB TombWatcher writeup
> Comprehensive Active Directory exploitation guide covering BloodHound analysis, targeted Kerberoasting, GMSA password recovery, shadow credentials, AD Recycle Bin recovery, and ESC15 certificate template abuse.
## Key facts extracted
- Assume breach scenario starting with henry credentials
- Complex BloodHound path from Henry to Administrator via multiple users
- Targeted Kerberoasting, GMSA abuse, ForceChangePassword, and shadow credentials
- AD Recycle Bin recovery of deleted cert_admin account
- ESC15 vulnerability (CVE-2024-49019) in WebServer certificate template
- Windows Server 2019 Domain Controller with ADCS deployment
## Filed into
[[tombwatcher]], [[targeted-kerberoast]], [[gmsa-password-recovery]], [[force-change-password]], [[shadow-credentials]], [[ad-recycle-bin]], [[ESC15]]
