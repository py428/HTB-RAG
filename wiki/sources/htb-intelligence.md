---
type: source
title: "HTB Intelligence writeup"
raw: raw/htb-intelligence.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[intelligence]]
---
# Source: HTB Intelligence writeup
> In-depth analysis of Active Directory enumeration, DNS manipulation, NTLM relay capture, GMSA abuse, and Kerberos delegation exploitation.

## Key facts extracted
- Default password policy creates weak credentials for new users
- PowerShell scheduled task queries DNS records starting with "web"
- DNS records can be added via LDAP with user permissions
- GMSA svc_int$ has ReadGMSAPassword permission for ITSupport group
- svc_int$ has constrained delegation on DC

## Filed into
[[intelligence]], [[directory-brute-force]], [[kerberos-username-enumeration]], [[password-spray]], [[ad-dns-manipulation]], [[ntlm-relay]], [[gmsa-password-read]], [[constrained-delegation]]
