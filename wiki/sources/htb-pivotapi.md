---
type: source
title: "HTB PivotAPI writeup"
raw: raw/htb-pivotapi.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[pivotapi]]
---
# Source: HTB PivotAPI writeup
> Comprehensive writeup covering an insane-difficulty Windows Active Directory machine involving multi-stage pivoting through MSSQL, WinRM tunneling, KeePass credential extraction, and LAPS abuse.

## Key facts extracted
- User Kaorz discovered through PDF metadata analysis on FTP anonymous share
- AS-REP roasting successful against Kaorz due to UF_DONT_REQUIRE_PREAUTH being set
- Password cracking revealed credential pattern: #oracle_s3rV1c3!2010 → #mssql_s3rV1c3!2020
- MSSQL sa access achieved using derived password pattern
- WinRM access obtained through mssqlproxy tunneling since direct access firewalled
- KeePass database found containing SSH credentials for 3v4Si0N user
- Progressive ACL abuse through ForceChangePassword enabled horizontal movement
- Account Operators group abuse allowed creation of new user with LAPS read access
- LAPS password extracted via ms-mcs-admpwd attribute for local administrator access
- Multiple unintended paths including PrintSpoofer for SeImpersonatePrivilege abuse

## Filed into
[[pivotapi]], [[as-rep-roasting]], [[metadata-analysis]], [[reverse-engineering]], [[mssqlproxy]], [[keepass]], [[acl-abuse]], [[account-operators]], [[laps]]