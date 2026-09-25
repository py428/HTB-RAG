---
type: source
title: "HTB Secret writeup"
raw: raw/htb-secret.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[secret]]
---
# Source: HTB Secret writeup
> Detailed writeup for HTB Secret machine covering Git history analysis for JWT secrets, token forgery, command injection exploitation, and two different SUID binary exploitation techniques using file descriptors and core dump analysis.

## Key facts extracted
- Secret runs Node.js Express application with downloadable source code containing Git repository
- JWT signing secret was changed from long random string to "secret" in Git commit history
- Admin user "theadmin" has access to `/api/priv` and `/api/logs` endpoints
- `/api/logs` contains command injection in git log execution with unsanitized file parameter
- SUID binary `/opt/count` allows reading files via file descriptors and core dump exploitation

## Filed into
[[secret]], [[git-history-analysis]], [[jwt-forging]], [[command-injection]], [[suid-file-descriptor-abuse]], [[core-dump-analysis]]
