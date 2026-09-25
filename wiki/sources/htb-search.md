---
type: source
title: "HTB Search writeup"
raw: raw/htb-search.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[search]]
---
# Source: HTB Search writeup
> In-depth Active Directory writeup covering credential extraction from website images, Kerberoasting, password reuse analysis, Excel password extraction, client certificate authentication, PowerShell Web Access exploitation, and GMSA-based privilege escalation.

## Key facts extracted
- Search domain has 106 users, 63 groups, and multiple Kerberoastable service accounts
- Hope Sharp credentials extracted from website image text provide initial AD access
- web_svc Kerberoastable account shares password with Edgar.Jacobs
- Protected Excel file contains Sierra.Frye credentials that unlock certificate-based authentication
- Sierra.Frye has ReadGMSAPassword permission on BIR-ADFS-GMSA which has GenericAll over Domain Admin

## Filed into
[[search]], [[image-metadata-extraction]], [[kerberoasting]], [[password-spraying]], [[excel-password-extraction]], [[certificate-authentication]], [[gmsa-password-recovery]]
