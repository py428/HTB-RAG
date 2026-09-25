---
type: source
title: "HTB Appsanity writeup"
raw: raw/htb-appsanity.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[appsanity]]
---
# Source: HTB Appsanity writeup

> Comprehensive walkthrough for HTB Appsanity box covering JWT token abuse, SSRF exploitation, file upload bypass, registry credential extraction, and DLL hijacking for privilege escalation.

## Key facts extracted

- **Dual application**: Main website and portal sharing JWT authentication
- **Initial access**: Hidden field manipulation for role escalation and JWT cookie reuse
- **Internal discovery**: SSRF for port scanning and internal service access
- **File upload**: PDF magic bytes preservation for ASPX webshell upload
- **Privilege escalation**: Registry credential extraction and DLL hijacking
- **Custom service**: ReportManagement.exe with writable Libraries directory

## Filed into

[[appsanity]], [[jwt-token-reuse]], [[ssrf]], [[file-upload-bypass]], [[registry-enumeration]], [[dll-hijacking]]
