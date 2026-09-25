---
type: source
title: "HTB Quick writeup"
raw: raw/htb-quick.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[quick]]
---

# Source: HTB Quick writeup

> Complete writeup for HTB Quick covering QUIC protocol enumeration, Edge Side Include injection, printer job race condition exploitation, SQL injection attacks, and privilege escalation via symlink abuse and credential extraction.

## Key facts extracted

- **QUIC Portal**: portal.quick.htb on UDP 443 with credentials elisa@wink.co.uk / Quick4cc3$$
- **ESI Injection**: Ticket system vulnerable to ESI tags for SSRF and XSLT code execution
- **Race Condition**: Printer job processing allows symlink creation for arbitrary file read/write
- **SQL Injection**: Multiple vulnerable endpoints in Complain Management System
- **Database Creds**: db_adm / db_p4ss from source code analysis
- **CUPS Cache**: srvadm@quick.htb / &ftQ4K3SGde8? from printer configuration

## Filed into

[[quick]], [[quic]], [[file-include]], [[esi-injection]], [[race-condition]], [[sqli]], [[symlink-abuse]], [[credential-extraction]], [[password-reuse]]
