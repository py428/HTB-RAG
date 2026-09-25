---
type: service
title: LDAP
ports: [389, 636, 3268, 3269]
updated: 2026-07-09
---

# LDAP

## Default ports
- **389/tcp** — LDAP (AD directory access).
- **636/tcp** — LDAPS (TLS).
- **3268/3269/tcp** — Global Catalog (GC / GC-over-SSL).

## Enumeration / interaction approach
Anonymous queries usually blocked beyond the base naming context; authenticate (NTLM or Kerberos `-Y GSSAPI`). Hunt for users/groups/descriptions, GPOs, ACLs. `ldapsearch`, [[crackmapexec]] `ldap`, [[bloodhound]]/SharpHound collection, [[certipy]] `find`.

## Related techniques
- [[ldap-description-credential]], [[kerberos-username-enumeration]], [[dacl-write-members]]

## Appears on
- [[absolute]]
- [[active]] — AD backend (2008 R2 DC).
- [[forest]] — user/group enum via BloodHound/SharpHound; AS-REP/DCSync target.
