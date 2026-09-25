---
type: source
title: "HTB Strutted writeup"
raw: raw/htb-strutted.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[strutted]]
---
# Source: HTB Strutted writeup
> Medium Linux box highlighting CVE-2024-53677 in Apache Struts, exploited via file upload parameter manipulation to upload webshell, followed by credential reuse and tcpdump GTFObins for root access.
## Key facts extracted
- Apache Tomcat 9 running Struts 6.3.0.1 (vulnerable to CVE-2024-53677)
- CVE-2024-53677 allows path traversal via top.UploadFileName parameter
- File upload requires exact "Upload" parameter name (capital U)
- Tomcat admin credentials in commented configuration blocks
- tcpdump GTFObins for privilege escalation
- Systemd NoNewPrivileges protection affecting su behavior
## Filed into
[[strutted]], [[apache-struts-rce]], [[webshell-upload]], [[password-reuse]], [[gtfobins]], [[sudo-abuse]]
