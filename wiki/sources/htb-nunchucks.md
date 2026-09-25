---
type: source
title: "HTB Nunchucks writeup"
raw: raw/htb-nunchucks.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[nunchucks]]
---

# Source: HTB Nunchucks writeup
> Guide covering Nunjucks server-side template injection for initial access, and AppArmor bypass via shebang execution for privilege escalation with Perl capabilities.

## Key facts extracted
- Nunjucks template engine processes email subscription input
- SSTI allows code execution via `range.constructor()` pattern
- Perl binary has cap_setuid capability but restricted by AppArmor
- AppArmor profile `/usr/bin/perl` blocks /root access and limits executable paths
- Shebang execution (`./script.pl`) bypasses AppArmor profile restrictions
- Direct binary invocation (`perl script.pl`) applies AppArmor protections
- GTFObins documents Perl setuid exploitation methods

## Filed into
[[nunchucks]], [[ssti]], [[rce]], [[capabilities]], [[apparmor-bypass]], [[setuid-binary]]
