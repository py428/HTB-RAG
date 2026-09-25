---
type: source
title: "HTB WingData writeup"
raw: raw/htb-wingdata.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[wingdata]]
---
# Source: HTB WingData writeup
> Full walkthrough of WingData HackTheBox machine covering Wing FTP exploitation via CVE-2025-47812, password hash cracking, and privilege escalation using CVE-2025-4517 tarfile vulnerability.
## Key facts extracted
- Wing FTP Server v7.4.3 with anonymous access enabled
- CVE-2025-47812: Null-byte injection in username allows Lua code execution
- Password hashes stored in /opt/wftpserver/Data in XML format
- SHA256(password + salt) format with salt "WingFTP"
- CVE-2025-4517: Python tarfile filter="data" path validation bypass
- Sudo script for backup operations using tarfile.extractall()
## Filed into
[[wingdata]], [[cve-2025-47812]], [[cve-2025-4517]], [[password-cracking]], [[sudo-abuse]], [[web]], [[linux]]
