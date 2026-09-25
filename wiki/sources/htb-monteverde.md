---
type: source
title: "HTB Monteverde writeup"
raw: raw/htb-monteverde.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[monteverde]]
---
# Source: HTB Monteverde writeup
> Windows Active Directory box focused on Azure Active Directory Services exploitation, involving RPC enumeration, password reuse, SMB file access, and Azure AD Connect database credential extraction.

## Key facts extracted
- Domain: MEGABANK.LOCAL, Windows domain controller with typical AD ports
- RPC null session access available for user enumeration
- Service account `SABatchJobs` used username as password
- Azure XML config file in SMB share contained encrypted password for user `mhope`
- Azure AD Connect installed with LocalDB database containing encrypted credentials
- PowerShell script required to decrypt Azure AD configuration and extract administrator password

## Filed into
[[monteverde]], [[rpc-null-session]], [[password-spray]], [[azure-ad-connect-database]]