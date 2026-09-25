---
type: source
title: "HTB Axlle writeup"
raw: raw/htb-axlle.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[axlle]]
---
# Source: HTB Axlle writeup
> Comprehensive guide to exploiting a Windows AD environment through Excel XLL phishing, credential harvesting, and LOLBIN abuse.

## Key facts extracted
- Windows Server 2022 domain controller with multiple services exposed
- Excel XLL add-on files execute code automatically when enabled
- SMTP server available for sending phishing emails
- URL files can execute arbitrary commands when opened
- Hardcoded credentials stored in application directories
- Password change functionality can be abused without authentication
- StandaloneRunner.exe can execute commands with elevated privileges

## Filed into
[[axlle]], [[xll-phishing]], [[url-file-exploit]], [[credential-harvesting]], [[password-change]], [[lolbin-abuse]]
