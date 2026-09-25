---
type: service
title: SMB
ports: [139, 445]
updated: 2026-07-09
---

# SMB

## Default ports
- **445/tcp** — SMB over TCP (primary).
- **139/tcp** — NetBIOS session (legacy).

## Enumeration / interaction approach
Check signing (`signing:True` blocks NTLM relay), enumerate shares/permissions and sessions. [[crackmapexec]] `--shares`, [[impacket]] `smbclient.py`, `smbmap`. Note: signing being **required** (common on DCs) defeats classic NTLM relay — see [[kerberos-relay]] for the Kerberos-era alternative.

## Related techniques
- [[ldap-description-credential]] (creds used to read shares), [[dcsync]] (`--ntds` over SMB)

## Appears on
- [[absolute]]
- [[active]] — anonymous `Replication` share (GPP).
- [[forest]] — signing required; `secretsdump`/DCSync over 445.
