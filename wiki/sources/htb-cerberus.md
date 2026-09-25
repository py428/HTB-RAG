---
type: source
title: "HTB Cerberus writeup"
raw: raw/htb-cerberus.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[cerberus]]
---
# Source: HTB Cerberus writeup
> Complex Windows+Linux environment writeup covering Icinga CVE exploitation, Firejail container escape, SSSD credential extraction, WinRM access, and ManageEngine ADSelfService Plus SAML vulnerability for SYSTEM access.

## Key facts extracted
- Machine: Cerberus (Hard, Windows/Linux mixed)
- Windows host running Ubuntu VM with Icinga
- IcingaWeb2 2.9.x vulnerable to CVE-2022-24716 and CVE-2022-24715
- Container escape via Firejail CVE-2022-31214
- SSSD cache contains matthew password hash (147258369)
- ManageEngine ADSelfService Plus with SAML vulnerability
- Multi-stage exploitation: container → host → SYSTEM

## Filed into
[[cerberus]], [[icinga-cve-2022-24716]], [[icinga-cve-2022-24715]], [[firejail-cve-2022-31214]], [[sssd-cache]], [[chisel]], [[winrm]], [[saml-cve]]
