---
type: source
title: "HTB Rabbit writeup"
raw: raw/htb-rabbit.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[rabbit]]
---

# Source: HTB Rabbit writeup

> Complete writeup for HTB Rabbit covering SQL injection exploitation, Exchange OWA phishing, macro execution, Windows scheduled task analysis, and WAMP server privilege escalation.

## Key facts extracted

- **SQL Injection**: Multiple vulnerable endpoints in Complain Management System at /complain/view.php and process.php
- **Database Access**: Secret database with 10 user hashes, 4 cracked via sqlmap
- **OWA Access**: Multiple user credentials work for Outlook Web Access login
- **Email Automation**: Scheduled tasks download attachments every 6 minutes and execute every 3 minutes
- **PowerShell CLM**: System uses PowerShell v2 and constrained language mode
- **WAMP Permissions**: C:\wamp64\www directory allows user write for webshell deployment

## Filed into

[[rabbit]], [[sqli]], [[hash-cracking]], [[phishing]], [[macro]], [[scheduled-task]], [[file-upload]], [[constrained-language-mode]], [[file-permission-abuse]]
