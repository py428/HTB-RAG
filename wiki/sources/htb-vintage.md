---
type: source
title: "HTB Vintage writeup"
raw: raw/htb-vintage.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[vintage]]
---
# Source: HTB Vintage writeup
> Hard AD box starting with low-privilege credentials, requiring BloodHound analysis, GMSA abuse, Kerberoasting, DPAPI credential extraction, and RBCD for complete domain compromise.

## Key facts extracted
- Starting credentials: P.Rosa:Rosaisbest123
- FS01$ password: `fs01` (Pre-Windows 2000 Compatible Access)
- GMSA01$ NTLM: `b3a15bbdfb1c53238d4b50ea2c4d1178`
- Cracked Kerberos password: `Zer0the0ne` (SVC_SQL)
- C.Neri_adm password: `Uncr4ck4bl3P4ssW0rd0312` (from DPAPI)
- Administrator NTLM: `468c7497513f8243b59980f2240a10de`
- L.Bianchi_adm NTLM: `6b751449807e0d73065b0423b64687f0`
- Domain: vintage.htb | DC: DC01

## Filed into
[[vintage]], [[bloodhound]], [[pre-windows-2000-password]], [[gmsa-password-read]], [[targeted-kerberoast]], [[password-spray]], [[dpapi-extraction]], [[rbcd]], [[dcsync]]
