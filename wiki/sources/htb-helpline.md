---
type: source
title: "HTB Helpline writeup"
raw: raw/htb-helpline.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[helpline]]
---
# Source: HTB Helpline writeup
> Comprehensive analysis of Helpline HackTheBox machine covering ManageEngine ServiceDesk Plus vulnerabilities including XXE (CVE-2017-9362), LFI (CVE-2017-11511), and bcrypt password cracking. Writeup is incomplete but covers initial exploitation through database backup extraction.
## Key facts extracted
- ManageEngine ServiceDesk Plus 9.3 runs on port 8080 with default guest/guest credentials
- CVE-2017-9362 XXE allows reading files via API cmdb/ci endpoint with XML payload
- CVE-2017-11511 LFI allows downloading files relative to SDP install directory
- Database backups stored in E:\ManageEngine\ServiceDesk\bin\..\backup\
- Bcrypt hashes with $2a$12$ prefix cracked with hashcat in mode 3200
- Multiple attack paths available (Windows Commando VM vs Kali)
## Filed into
[[helpline]], [[xxe]], [[lfi]], [[password-cracking]]
