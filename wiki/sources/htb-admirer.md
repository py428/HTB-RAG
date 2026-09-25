---
type: source
title: "HTB Admirer writeup"
raw: raw/htb-admirer.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[admirer]]
---
# Source: HTB Admirer writeup
> Detailed walkthrough of exploiting Admirer, a Linux HackTheBox machine involving web enumeration, FTP credential exposure, Adminer database interface manipulation, and sudo Python library hijacking for privilege escalation.

## Key facts extracted
- FTP credentials found in /admin-dir/credentials.txt: ftpuser / %n?4Wz}R$tTF7
- Database credentials discovered in source code: waldo / &<h5b~yK3F#{PaPB&dA}{H>
- Adminer interface vulnerable to local file read via MySQL LOAD DATA LOCAL INFILE
- sudo configuration allows SETENV on /opt/scripts/admin_tasks.sh enabling PYTHONPATH hijack
- Python library hijacking achieved by creating malicious shutil.py in /var/tmp

## Filed into
[[admirer]], [[web-enumeration]], [[ftp-credential-exposure]], [[adminer-file-read]], [[sudo-pythonpath-hijack]]
