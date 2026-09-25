---
type: source
title: "HTB DarkCorp writeup"
raw: raw/htb-darkcorp.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[darkcorp]]
---
# Source: HTB DarkCorp writeup

> Comprehensive walkthrough of DarkCorp, an insane-difficulty multi-host HTB box featuring a complex attack chain across Linux and Windows systems, including XSS exploitation, PostgreSQL RCE, credential cracking, NTLM relay, ADCS abuse, and GPO manipulation for complete domain compromise.

## Key facts extracted

- RoundCube CVE-2024-42009 XSS vulnerability for email exfiltration
- PostgreSQL database accessible via development dashboard with SQL injection
- PGP-encrypted backup contains additional user credentials
- Windows domain with cross-forest trust and ADCS services
- Monitoring dashboard provides NTLM authentication for relay attacks
- Multiple privilege escalation paths including ADCS, shadow credentials, and GPO abuse

## Filed into

[[darkcorp]], [[xss]], [[sql-injection]], [[postgresql-rce]], [[pgp-decryption]], [[ntlm-relay]], [[adcs]], [[shadow-credentials]], [[upn-spoofing]], [[gpo-abuse]], [[dns-manipulation]]