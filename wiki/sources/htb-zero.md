---
type: source
title: "HTB Zero writeup"
raw: raw/htb-zero.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[zero]]
---
# Source: HTB Zero writeup
> Detailed writeup covering Zero hosting provider exploitation including .htaccess file read primitive, database credential extraction, Apache configuration validation abuse, and multiple root methods via process faking and malicious Apache modules.

## Key facts extracted
- Hosting provider with SFTP upload and .htaccess manipulation capabilities
- Apache ErrorDocument %{file:/path} directive allows arbitrary file read
- Database credentials exposed in stats.php source code
- Cron job validates Apache configuration by executing apache2ctl on matching processes
- Multiple paths to root via process name faking and apache2ctl injection
- Apache module loading and log pipe exploitation techniques

## Filed into
[[zero]], [[htaccess-file-read]], [[apache2ctl-injection]], [[process-fake]], [[apache-log-pipe]], [[apache-module]]