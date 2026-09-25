---
type: source
title: "HTB SolarLab writeup"
raw: raw/htb-solarlab.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[solarlab]]
---
# Source: HTB SolarLab writeup
> Comprehensive writeup covering SMB enumeration, ReportLab CVE exploitation, OpenFire vulnerability exploitation, and Windows privilege escalation paths.

## Key facts extracted
- SMB Documents share accessible with guest credentials
- Excel file contains usernames and potential passwords
- ReportHub login shows different error messages for valid/invalid users
- CVE-2023-33733 in ReportLab allows RCE via color attribute injection
- SQLite database contains additional credentials
- OpenFire 4.7.4 vulnerable to CVE-2023-32315 path traversal
- OpenFire embedded database contains encrypted admin password
- Blowfish decryption with passwordKey yields admin credentials

## Filed into
[[solarlab]], [[password-spray]], [[cve-2023-33733]], [[cve-2023-32315]], [[openfire-plugin-rce]]
