---
type: source
title: "HTB Scepter writeup"
raw: raw/htb-scepter.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[scepter]]
---
# Source: HTB Scepter writeup
> Active Directory certificate abuse walkthrough covering NFS share enumeration, certificate authentication, ESC14 exploitation for privilege escalation, and DCSync for domain compromise. Shows advanced AD CS abuse techniques with altSecurityIdentities manipulation.

## Key facts extracted
- NFS share /helpdesk contains 4 certificate files (baker crt/key, clark/lewis/scott pfx)
- All certificates have password "newpassword" but only d.baker account is enabled
- d.baker has ForceChangePassword over a.carter (via BloodHound analysis)
- a.carter in IT Support has GenericAll over Staff Access Certificate OU
- h.brown's altSecurityIdentities set to X509:<RFC822>h.brown@scepter.htb
- ESC14 abuse: modify d.baker email to match target's altSecurityIdentities, request cert
- CMS group has WriteProperty on p.adams altSecurityIdentities for second ESC14
- p.adams member of Replication Operators enables DCSync
- Disabled accounts show KDC_ERR_CLIENT_REVOKED but certificates remain valid

## Filed into
[[scepter]], [[nfs-enumeration]], [[certificate-authentication]], [[esc14]], [[dcsync]], [[force-change-password]]
