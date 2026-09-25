---
type: source
title: "HTB Help writeup"
raw: raw/htb-help.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[help]]
---
# Source: HTB Help writeup
> Complete walkthrough of Help HackTheBox machine covering GraphQL enumeration, HelpDeskZ SQL injection exploitation, and kernel privilege escalation via CVE-2017-16995 or CVE-2017-5899. Alternative path via unauthenticated file upload also documented.
## Key facts extracted
- GraphQL API on port 3000 exposes user credentials via schema introspection
- HelpDeskZ 1.0.2 vulnerable to authenticated SQLi in ticket attachment parameter
- Staff password hash d318f44739dced66793b1a603028133a76ae680e cracks to "Welcome1"
- Ubuntu 16.04 with kernel 4.4.0-116 vulnerable to multiple exploits
- Alternative unauthenticated upload via HelpDeskZ (file MD5(filename+time).php)
## Filed into
[[help]], [[graphql-enum]], [[sqli]], [[password-cracking]], [[kernel-exploit]], [[file-upload]]
