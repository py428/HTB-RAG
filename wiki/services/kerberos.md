---
type: service
title: Kerberos
ports: [88, 464]
updated: 2026-07-09
---

# Kerberos

## Default ports
- **88/tcp** — KDC (authentication, AS-REQ/TGS).
- **464/tcp** — kpasswd (password set/change).

## Enumeration / interaction approach
No anonymous access — you interact by requesting tickets. Use `kinit` (get a TGT), `klist` (inspect cache), and `-k`/`KRB5CCNAME` on tools. Watch for clock skew and hosts-file reverse-lookup quirks. See [[ntlm-disabled-protected-users]] for the common Kerberos-only scenario.

## Related techniques
- [[as-rep-roasting]], [[kerberos-username-enumeration]], [[shadow-credentials]], [[kerberos-relay]], [[dcsync]]

## Appears on
- [[absolute]]
- [[active]] — Kerberoasting (TGS for the Administrator SPN).
- [[forest]] — AS-REP roasting; WinRM auth.
