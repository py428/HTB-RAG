---
type: source
title: "HTB Stocker writeup"
raw: raw/htb-stocker.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[stocker]]
---
# Source: HTB Stocker writeup
> Writeup covering NoSQL injection for authentication bypass, server-side XSS in PDF generation for file reading, and sudo misconfiguration for privilege escalation.
## Key facts extracted
- Dev site uses MongoDB with NoSQL injection vulnerability
- Login bypass: `{"username":{"$ne": "x"}, "password":{"$ne":"x"}}`
- PDF generation uses Chromium, interpreting HTML/JS in input
- Server-side XSS allows file reading via XMLHttpRequest
- MongoDB credentials leaked in source code: `IHeardPassphrasesArePrettySecure`
- Sudo rule: `(ALL) /usr/bin/node /usr/local/scripts/*.js`
- Wildcard allows path traversal: `../../../dev/shm/exploit.js`

## Filed into
[[stocker]], [[nosql-injection]], [[server-side-xss]], [[file-read-xss]], [[sudo-misconfiguration]]
