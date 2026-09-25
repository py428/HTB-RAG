---
type: source
title: "HTB Arkham writeup"
raw: raw/htb-arkham.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[arkham]]
---
# Source: HTB Arkham writeup
> Medium Windows box walkthrough covering LUKS cracking, JSF deserialization, and UAC bypass techniques for privilege escalation.

## Key facts extracted
- Arkham runs Windows Server 2016 with IIS and Tomcat services
- SMB BatShare contains LUKS-encrypted backup image with password "batmanforever"
- Mounted image contains Tomcat configuration with JSF SECRET and MAC keys
- JSF ViewState uses DES encryption with PKCS padding and HMAC-SHA1 signing
- Alfred user OST email file contains Batman credentials: Zx^#QZX+T!123
- Batman user in Administrators and Remote Management Users groups
- UAC bypass via CMSTP DLL loading or SystemPropertiesAdvanced srrstr.dll hijacking
- PowerShell Constrained Language Mode restricts direct command execution
- Alternative root access via localhost c$ share exploitation

## Filed into
[[arkham]], [[luks-brute-force]], [[deserialization]], [[uac-bypass]], [[file-format-exploitation]]
