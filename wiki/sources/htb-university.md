---
type: source
title: "HTB University writeup"
raw: raw/htb-university.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[university]]
---
# Source: HTB University writeup
> Comprehensive guide to AD exploitation from initial foothold to Domain Admin through multiple attack paths.

## Key facts extracted
- CVE-2023-33733 in ReportLab/xhtml2pdf for initial RCE
- Django application with SQLite database and CA certificate keys
- CA keys allow forging any user's login certificate
- Three internal hosts: DC (192.168.99.1), WS-3 (192.168.99.2), LAB-2 (192.168.99.12)
- WS-3 configured with unconstrained delegation
- WS-3 periodically requests WPAD (every ~15 minutes)
- Rose.L has ReadGMSAPassword on GMSA-PClient01$
- GMSA-PClient01$ has AllowedToAct on DC computer object
- Multiple paths to DA via different user privileges

## Filed into
[[university]], [[cve-2023-33733]], [[certificate-abuse]], [[wpad-spoofing]], [[ntlm-relay]], [[rbcd]], [[unconstrained-delegation]], [[gmsa-abuse]]
