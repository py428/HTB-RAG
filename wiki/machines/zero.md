---
type: machine
title: Zero
platform: htb
os: linux
difficulty: insane
tags: [web, linux, privesc, apache]
solved: 2026-07-09
sources: [[htb-zero]]
related: []
---
# Zero
> Zero is a hosting provider with SFTP file upload and .htaccess manipulation capabilities. The attack path involves abusing .htaccess ErrorDocument directives to read files, extracting database credentials for initial shell access, then exploiting a cron job that validates Apache configuration by executing apache2ctl on processes matching specific patterns.

## Attack path
1. [[htaccess-file-read]] via ErrorDocument directive to enumerate filesystem
2. Database credential extraction from PHP source code
3. SSH access with recovered credentials
4. [[apache2ctl-injection]] via cron job validating fake Apache process names
5. [[process-fake]] to trigger malicious apache2ctl execution as root

## Techniques used
- [[htaccess-file-read]] — ErrorDocument with %{file:/path} directive reads arbitrary files
- [[apache2ctl-injection]] — Cron job executes apache2ctl on processes matching pgrep pattern
- [[process-fake]] — Python execv or Perl $0 manipulation to fake process command line
- [[apache-log-pipe]] — ErrorLog "|/path/to/script" for command execution
- [[apache-module]] — Malicious Apache module with constructor for code execution

## Tools used
[[nmap]], [[feroxbuster]], [[paramiko]], [[curl]], [[ssh]], pspy, nc, python, perl, gcc, apxs

## Services / ports
[[ssh]] (22), [[http]] (80), [[ftp]] (21)

## Lessons / notes
- Apache .htaccess ErrorDocument %{file:/path} directive allows reading arbitrary files
- Pure-FTPd accepts any 32-character username/password combination when they match
- Cron job uses pgrep -f and bash string replacement to execute apache2ctl on running processes
- Process name faking via execv or Perl $0 allows command injection into cron validation
- apache2ctl -d can be specified multiple times, only last one is used
- ErrorLog "|/program" directive allows command execution during Apache config testing