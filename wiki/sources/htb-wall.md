---
type: source
title: "HTB Wall writeup"
raw: raw/htb-wall.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[wall]]
---
# Source: HTB Wall writeup
> Detailed writeup covering Centreon CVE-2019-13024 exploitation with WAF bypass, Python bytecode decompilation for credential recovery, and SUID screen binary exploitation for privilege escalation on a medium Linux difficulty box.

## Key facts extracted
- Centreon v19.04 vulnerable to CVE-2019-13024 authenticated RCE via poller configuration
- ModSecurity WAF blocks common exploit payloads including space character
- WAF bypass using ${IFS} environment variable instead of spaces
- Python backup script compiled as .pyc with obfuscated password building
- SUID screen 4.5.0 binary vulnerable to shared library hijacking
- Credentials: admin:password1 (Centreon), shelby:ShelbyPassw@rdIsStrong! (SSH)

## Filed into
[[wall]], [[cve-2019-13024]], [[waf-bypass]], [[python-bytecode-decompilation]], [[suid-binary-exploitation]], [[centreon]]
