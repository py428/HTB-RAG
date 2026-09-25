---
type: source
title: "HTB Anubis writeup"
raw: raw/htb-anubis.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[anubis]]
---
# Source: HTB Anubis writeup

> Comprehensive walkthrough for HTB Anubis covering ASP SSTI exploitation, Jamovi file vulnerabilities, internal network tunneling, AD CS template abuse, and Kerberos certificate authentication for domain compromise.

## Key facts extracted

- **Multi-stage attack**: Web container → internal network → user compromise → AD CS abuse → domain admin
- **Initial foothold**: ASP SSTI in contact form providing SYSTEM in Windows container
- **Internal access**: Chisel tunnel through container to reach softwareportal.windcorp.htb
- **User compromise**: NTLM hash capture and Jamovi malicious file for diegocruz access
- **Privilege escalation**: AD CS Web template abuse with smart card logon extension
- **Time sensitivity**: Kerberos certificate authentication requires matching system clocks

## Filed into

[[anubis]], [[asp-ssti]], [[jamovi-cve-2021-28079]], [[adcs-template-abuse]], [[kerberos-pkinit]], [[ntlm-relay]]
