---
type: source
title: "HTB Bastard writeup"
raw: raw/htb-bastard.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[bastard]]
---
# Source: HTB Bastard writeup
> Comprehensive writeup covering multiple exploitation paths against a Drupal 7.54 instance on Windows Server 2008 R2, including three different RCE vulnerabilities (Services module, Drupalgeddon2, Drupalgeddon3) and kernel exploitation for privilege escalation.
## Key facts extracted
- Drupal 7.54 identified via CHANGELOG.txt and droopescan enumeration
- Three unauthenticated RCE methods demonstrated: Services module exploit, Drupalgeddon2, Drupalgeddon3
- Webshell upload leads to shell as nt authority\iusr
- MS15-051 kernel exploit escalates to nt authority\system
- Multiple techniques for shell upgrade and persistence
## Filed into
[[bastard]], [[drupal-services-rce]], [[drupalgeddon2]], [[drupalgeddon3]], [[ms15-051]]
