---
type: source
title: "HTB Flight writeup"
raw: raw/htb-flight.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[flight]]
---
# Source: HTB Flight writeup
> Hard-difficulty Windows AD domain controller box with complex multi-stage attack path involving web vulnerabilities, SMB share manipulation, and Kerberos delegation abuse.

## Key facts extracted
- Windows DC running flight.htb domain with DNS, LDAP, Kerberos, SMB, WinRM services exposed
- PHP site at school.flight.htb has file read vulnerability via view parameter
- NetNTLMv2 hash capture via SMB authentication triggered by file inclusion
- Password reuse across domain users (svc_apache → S.Moon)
- SMB shares with write permissions for webshell upload
- Internal IIS development site on port 8000 accessible via tunneling
- IIS application pool identity authenticates as machine account over network
- Kerberos delegation abuse to get machine account TGT for DCSync

## Filed into
[[flight]], [[sqli]], [[netntlm-relay]], [[password-cracking]], [[kerberos-username-enumeration]], [[password-spray]], [[webshell]], [[port-forwarding]], [[kerberos-relay]], [[dcsync]]
