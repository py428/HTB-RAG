---
type: source
title: "HTB Analysis writeup"
raw: raw/htb-analysis.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[analysis]]
---
# Source: HTB Analysis writeup
> Comprehensive guide to exploiting LDAP injection for user enumeration and credential extraction, PHP webshell upload, and DLL hijacking via Snort dynamic preprocessor directory on a Windows Domain Controller.

## Key facts extracted
- LDAP injection in internal web application allows user enumeration
- Shared technician account password in LDAP description field
- PHP upload functionality allows webshell execution
- Autologon credentials found in Windows registry
- Snort dynamic preprocessor directory writable by Users group
- DLL in writable directory loaded by Snort running as SYSTEM

## Filed into
[[analysis]], [[ldap-injection]], [[ldap-attribute-extraction]], [[ldap-description-credential]], [[php-webshell]], [[autologon-credential]], [[dll-hijack]]
