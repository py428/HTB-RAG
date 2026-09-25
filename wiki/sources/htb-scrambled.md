---
type: source
title: "HTB Scrambled writeup"
raw: raw/htb-scrambled.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[scrambled]]
---
# Source: HTB Scrambled writeup
> Windows Active Directory box with NTLM authentication disabled, requiring Kerberos-only tooling. Covers web-based credential discovery, kerberoasting for silver ticket generation, MSSQL exploitation, custom .NET deserialization, and JuicyPotato for SYSTEM escalation.

## Key facts extracted
- NTLM authentication disabled, requires Kerberos throughout
- Web application contains credential hints for initial access
- File shares provide additional credential discovery opportunities
- Service account kerberoasting enables silver ticket generation
- Silver ticket grants MSSQL access for further credential harvesting
- Custom .NET executables contain deserialization vulnerabilities
- MSSQL xp_cmdshell provides command execution capabilities
- JuicyPotato enables SYSTEM privilege escalation from user context

## Filed into
[[scrambled]], [[kerberoasting]], [[silver-ticket]], [[mssql-xp-cmdshell]], [[deserialization]], [[juicy-potato]], [[ntlm-disabled-protected-users]]
