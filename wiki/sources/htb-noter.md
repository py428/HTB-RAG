---
type: source
title: "HTB Noter writeup"
raw: raw/htb-noter.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[noter]]
---

# Source: HTB Noter writeup
> Complete walkthrough covering Flask cookie cracking, username enumeration, FTP default password pattern, CVE-2021-23639 exploitation in md-to-pdf, and MySQL UDF privilege escalation.

## Key facts extracted
- Flask session secret "secret123" crackable from rockyou.txt
- Different login errors for invalid user vs invalid password enables enumeration
- FTP default password pattern: `username@site_name!` (e.g., ftp_admin@Noter!)
- md-to-pdf library processes markdown with embedded JavaScript execution
- Alternative command injection via quotes in subprocess call
- Source code available via FTP backups
- MySQL runs as root with UDF loading capability
- Raptor UDF exploit creates do_system() function for root commands

## Filed into
[[noter]], [[flask-cookie-cracking]], [[username-enumeration]], [[flask-session-forgery]], [[password-policy-abuse]], [[cve-exploitation]], [[command-injection]], [[mysql-udf-exploitation]]
