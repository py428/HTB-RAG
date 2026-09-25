---
type: source
title: "HTB Previse writeup"
raw: raw/htb-previse.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[previse]]
---
# Source: HTB Previse writeup
> Complete walkthrough of Previse, an Easy PHP box demonstrating execution after redirect, command injection, hash cracking, and sudo path hijacking techniques.

## Key facts extracted
- PHP application on Apache 2.4.29 (Ubuntu 18.04)
- Execution after redirect vulnerability on index page
- Command injection in logs.php: exec("/usr/bin/python /opt/scripts/log_process.py {$_POST['delim']}")
- Database credentials: root/mySQL_p@ssw0rd!:)
- MD5crypt hash with emoji salt cracked to ilovecody112235!
- Sudo rule: (root) /opt/scripts/access_backup.sh
- Sudo configuration missing secure_path, env_reset, and mail_badpass
- Unintended SQL injection in files.php INSERT statement (Beyond Root)

## Filed into
[[previse]], [[execution-after-redirect]], [[command-injection]], [[hash-cracking]], [[password-reuse]], [[path-hijack]], [[sudo-misconfiguration]]
