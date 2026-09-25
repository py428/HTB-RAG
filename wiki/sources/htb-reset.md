---
type: source
title: "HTB Reset writeup"
raw: raw/htb-reset.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[reset]]
---
# Source: HTB Reset writeup
> Detailed analysis of the Reset HackTheBox machine covering password reset vulnerabilities, log poisoning techniques, and Berkeley r-command abuse.

## Key facts extracted
- PHP application uses include() to load log files for display
- Password reset endpoint returns new password in JSON response
- Apache access.log can be poisoned via User-Agent header
- /etc/hosts.equiv configured to allow sadm user without password
- sadm user has active tmux session containing credentials
- sudo configuration allows nano as any user for specific files
- Log poisoning bypasses directory traversal restrictions

## Filed into
[[reset]], [[password-reset-bypass]], [[log-poisoning]], [[rlogin-abuse]], [[tmux-session-recovery]], [[sudo-nano-escape]]
