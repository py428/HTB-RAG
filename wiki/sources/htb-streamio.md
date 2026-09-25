---
type: source
title: "HTB StreamIO writeup"
raw: raw/htb-streamio.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[streamio]]
---
# Source: HTB StreamIO writeup
> Medium Windows domain controller with PHP/IIS web application vulnerable to SQL injection and file inclusion, requiring Firefox credential extraction and BloodHound-guided LAPS exploitation for administrator access.
## Key facts extracted
- Domain controller (DC.streamio.htb) running IIS with PHP 7.2.26
- Two web applications: streamio.htb (main) and watch.streamio.htb (search)
- MSSQL database with MD5 hashed passwords
- Remote file inclusion via debug parameter in master.php
- Firefox with saved Slack credentials for domain user
- LAPS deployment for local administrator password management
## Filed into
[[streamio]], [[sqli]], [[file-include]], [[firefox-credentials]], [[bloodhound]], [[laps]], [[ad]], [[winrm]], [[ldap]]
