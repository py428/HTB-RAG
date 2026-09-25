---
type: source
title: "HTB DarkZero writeup"
raw: raw/htb-darkzero.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[darkzero]]
---
# Source: HTB DarkZero writeup

> Detailed walkthrough of DarkZero, a hard-difficulty Windows AD box with cross-forest trust, featuring MSSQL linked server exploitation, multiple privilege escalation paths including token impersonation, ADCS abuse, NTLM authentication reflection, and CVE exploitation, culminating in DCSync for complete domain compromise.

## Key facts extracted

- Cross-forest trust between darkzero.htb and darkzero.ext
- MSSQL linked server DC02.darkzero.ext with sysadmin privileges for john.w
- Multiple privilege escalation techniques available on unpatched DC02
- CVE-2025-58726 allows NTLM relay authentication reflection
- ADCS services enabled on both domains for certificate enrollment
- Cross-forest TGT delegation provides path to DC01 compromise

## Filed into

[[darkzero]], [[mssql-linked-servers]], [[xp-cmdshell]], [[token-impersonation]], [[adcs]], [[ntlm-relay]], [[kerberos-delegation]], [[dcsync]], [[cve-2025-58726]]