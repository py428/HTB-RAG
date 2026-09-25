---
type: source
title: "HTB Multimaster writeup"
raw: raw/htb-multimaster.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[multimaster]]
---
# Source: HTB Multimaster writeup
> Insane-difficulty Windows Active Directory box with SQL injection, CEF debugging, complex AD privilege escalation, and multiple root paths including ZeroLogon.

## Key facts extracted
- Domain: MEGACORP.LOCAL with multiple web applications and database backend
- WAF blocked SQL injection characters but unicode encoding bypassed restrictions  
- MSSQL database Hub_DB contained colleague information and password hashes
- Hash cracking revealed reused passwords across multiple user accounts
- Visual Studio Code with CEF debugging exposed code execution vulnerability
- Custom DLL contained database credentials for service account escalation
- BloodHound revealed GenericWrite privileges enabling AS-REP roasting attack
- Server Operators group membership allowed service modification for SYSTEM access
- ZeroLogon (CVE-2020-1472) provided direct domain compromise path

## Filed into
[[multimaster]], [[waf-bypass]], [[sqli]], [[cef-debugging]], [[acl-genericwrite]], [[as-rep-roasting]], [[service-permission-abuse]], [[zerologon]]