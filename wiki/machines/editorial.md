---
type: machine
title: Editorial
platform: htb
os: linux
difficulty: easy
tags: [linux, web, ssrf, git, cve]
solved: 2026-07-09
sources: [[htb-editorial]]
related: []
---
# Editorial
> Linux hosting box with a publishing website featuring an SSRF vulnerability in the image upload functionality. Internal API on port 5000 leaks credentials for SSH access. Password reuse and Git history analysis reveal credentials for the next user. Exploiting CVE-2022-24439 in GitPython for root.
## Attack path
1. [[ssrf]] to access internal API on port 5000
2. Extract dev credentials from API response
3. SSH as dev, find prod credentials in [[git-history]]
4. [[password-reuse]] to login as prod via SSH
5. Exploit [[cve-exploitation]] CVE-2022-24439 in GitPython for root
## Techniques used
- [[ssrf]] - Internal port fuzzing via image upload preview to find API on 5000
- [[git-history]] - Found prod credentials in git diff between commits
- [[password-reuse]] - Database credentials from XWiki config reused for SSH
- [[cve-exploitation]] - CVE-2022-24439 in GitPython 3.1.29 for RCE via clone URLs
## Tools used
- [[nmap]], [[ffuf]], [[feroxbuster]], [[curl]], [[netexec]], [[sshpass]], [[git]]
## Services / ports
- [[ssh]] (22), [[http]] (80)
## Lessons / notes
- The SSRF only works with HTTP/HTTPS URLs - other protocols fail
- ffuf calibration with `-ac` automatically filters by response time differences
- GitPython vulnerable to `ext::` protocol for command injection via clone URLs
- The `-c protocol.ext.allow=always` flag enables the vulnerable protocol