---
type: source
title: "HTB Blazorized writeup"
raw: raw/htb-blazorized.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[blazorized]]
---
# Source: HTB Blazorized writeup
> Comprehensive exploitation of Blazor.NET applications covering DLL reverse engineering, JWT secret extraction, SQL injection to RCE, targeted Kerberoasting, ACL abuse for logon script planting, and DCSync domain compromise.

## Key facts extracted
- Blazorized.Helper.dll contains hardcoded JWT signing key for HS512 tokens
- Admin panel uses localStorage JWT token for authentication
- SQL injection in duplicate check form enables xp_cmdshell RCE
- BloodHound reveals nu_1055 has WriteSPN privilege over RSA_4810
- RSA_4810 has WriteProperty on SSA_6010 ScriptPath attribute  
- SYSVOL scripts directory writable by RSA_4810
- SSA_6010 has DCSync privileges via GetChangesAll permission
- Multiple privilege escalation paths demonstrate layered AD security model

## Filed into
[[blazorized]], [[dll-reverse-engineering]], [[jwt-forgery]], [[sqli]], [[targeted-kerberoast]], [[acl-abuse]], [[logon-script-abuse]], [[dcsync]]
