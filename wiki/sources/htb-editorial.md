---
type: source
title: "HTB Editorial writeup"
raw: raw/htb-editorial.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[editorial]]
---
# Source: HTB Editorial writeup
> Editorial is a Linux box with a simple publishing website. The main attack path involves exploiting an SSRF vulnerability to access an internal API, extracting credentials from Git history, and exploiting CVE-2022-24439 in GitPython for root access.
## Key facts extracted
- SSRF in image upload preview allows internal port enumeration
- Internal API on localhost:5000 contains hardcoded dev credentials
- Git history contains prod credentials in a previous commit
- GitPython 3.1.29 vulnerable to CVE-2022-24439 for command injection
## Filed into
[[editorial]], [[ssrf]], [[git-history]], [[password-reuse]], [[cve-exploitation]]