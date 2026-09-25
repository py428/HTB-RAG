---
type: source
title: "HTB Intuition writeup"
raw: raw/htb-intuition.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[intuition]]
---
# Source: HTB Intuition writeup
> Extensive writeup for HTB Intuition covering XSS exploitation, file reads via urllib bypass, and multiple privilege escalation paths including Ansible abuse and Docker escape.

## Key facts extracted
- Multi-domain setup: comprezzor.htb, auth.comprezzor.htb, report.comprezzor.htb, dashboard.comprezzor.htb
- Python 3.11.3 vulnerable to CVE-2023-24329 (urllib.parse bypass)
- wkhtmltopdf 0.12.6 used for PDF generation from URLs
- FTP credentials: ftp_admin/u3jai8y71s2 for ftp.local
- Suricata IDS logs FTP commands including passwords
- Ansible authentication key: UHI75GHINKOP (MD5: 0feda17076d793c2ef2870d7427ad4ed)

## Filed into
[[intuition]], [[blind-xss]], [[python-urllib-bypass]], [[ansible-galaxy-cve-2023-5115]], [[command-injection]]