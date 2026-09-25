---
type: source
title: "HTB Bizness writeup"
raw: raw/htb-bizness.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[bizness]]
---
# Source: HTB Bizness writeup
> Complete exploitation guide for Apache OFBiz server covering CVE-2023-49070 pre-auth RCE, Derby database exfiltration and analysis, custom OFBiz hash cracking, and privilege escalation via password reuse.

## Key facts extracted
- Apache OFBiz 18.12.09 vulnerable to CVE-2023-49070 pre-auth RCE via XML-RPC deserialization
- XML-RPC endpoint accessible at /webtools/control/xmlrpc;/ without authentication
- OFBiz uses embedded Apache Derby database with legacy plaintext password storage
- Custom hash format: $SHA$d$d$base64hash where d is single character salt
- Database contains admin user with crackable hash
- Root access achieved via password reuse (admin and root share same password)

## Filed into
[[bizness]], [[cve-2023-49070]], [[deserialization]], [[database-exfiltration]], [[hash-cracking]]
