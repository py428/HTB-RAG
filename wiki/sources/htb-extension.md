---
type: source
title: "HTB Extension writeup"
raw: raw/htb-extension.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[extension]]
---
# Source: HTB Extension writeup
> Hard Linux box with complex multi-stage exploitation involving IDOR, password reset prediction, custom Firefox extension, and Docker escape.

## Key facts extracted
- Laravel management endpoint /management/dump exposes user database via POST
- Password reset tokens: MD5(email) + 3 hex chars (1000 possibilities)
- Custom Firefox extension with XSS allows arbitrary requests to Gitea
- Hash extension vulnerability enables command injection via template injection
- Docker socket writable inside container for privilege escalation

## Filed into
[[extension]], [[database-dump]], [[idor]], [[password-reset-token-prediction]], [[xss]], [[command-injection]], [[docker-socket-abuse]]