---
type: source
title: "HTB Silo writeup"
raw: raw/htb-silo.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[silo]]
---
# Source: HTB Silo writeup
> Oracle database exploitation guide with webshell upload, memory forensics, and multiple privilege escalation paths.
## Key facts extracted
- Oracle SID: XE (Express Edition)
- Database credentials: SCOTT:tiger (works with SYSDBA privilege)
- Alternative SIDs: XEXDB, PLSExtProc, CLRExtProc
- Administrator NTLM hash: 9e730375b7cbcebf74ae46481e07b0c7
- Oracle service runs as SYSTEM on Windows
- Memory dump from Dropbox with password: £%Hm8646uC$
## Filed into
[[silo]], [[oracle-enumeration]], [[oracle-webshell]], [[memory-forensics]], [[pass-the-hash]], [[oracle-direct-execution]]
