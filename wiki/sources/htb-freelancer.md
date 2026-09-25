---
type: source
title: "HTB Freelancer writeup"
raw: raw/htb-freelancer.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[freelancer]]
---
# Source: HTB Freelancer writeup
> Complete writeup for Freelancer HTB machine covering Django IDOR, MSSQL impersonation, memory dump analysis, and resource-based constrained delegation for domain compromise.

## Key facts extracted
- Windows Server 2019 DC running freelancer.htb domain
- Django web application with QR-code login vulnerability
- MSSQL with impersonation privileges from webapp user to sa
- Memory dump (MEMORY.7z) containing LSA secrets
- Multiple user credentials in configuration files
- RBCD configuration allowing delegation to DC
- Critical users: sql_svc, mikasaAckerman, lorra199, Administrator

## Filed into
[[freelancer]], [[idor]], [[mssql-impersonation]], [[xp-cmdshell]], [[memory-analysis]], [[lsa-secrets]], [[rbcd-exploit]]
