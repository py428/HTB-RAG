---
type: machine
title: Nunchucks
platform: htb
os: linux
difficulty: easy
tags: [web, linux, ssti, rce, apparmor, privesc, perl, capabilities]
solved: 2026-07-09
sources: [[htb-nunchucks]]
related: []
---

# Nunchucks
> Nunchucks is a Nunjucks template engine application with server-side template injection leading to RCE, and privilege escalation via Perl with setuid capability and AppArmor bypass.

## Attack path
1. [[ssti]] — Template injection in email subscription form
2. [[rce]] — Nunjucks SSTI with `range.constructor()` for code execution
3. [[capabilities]] — Perl has cap_setuid capability
4. [[apparmor-bypass]] — Execute Perl via shebang to bypass AppArmor profile
5. Get root shell via Perl setuid binary

## Techniques used
- [[ssti]] — Nunjucks template injection detected with `{{7*7}}` payload
- [[rce]] — `range.constructor("return global.process.mainModule.require('child_process').execSync('cmd')")()`
- [[capabilities]] — Perl binary has cap_setuid+ep capability
- [[apparmor-bypass]] — Shebang execution bypasses AppArmor binary profile restrictions
- [[setuid-binary]] — Perl script runs as root when executed via shebang

## Tools used
- [[nmap]]
- wfuzz
- feroxbuster
- [[netcat]]
- python
- perl

## Services / ports
- SSH (22) — OpenSSH 8.2
- HTTP (80) — nginx 1.18.0
- HTTPS (443) — nginx 1.18.0

## Lessons / notes
- Nunjucks is a JavaScript templating engine for Express
- SSTI payload structure: `{{range.constructor("return global.process.mainModule.require('child_process').execSync('cmd')")()}}`
- Template injection often leads to RCE in NodeJS applications
- AppArmor profiles protect binaries but not scripts executed via shebang
- `./script.pl` bypasses AppArmor while `perl script.pl` is protected
- Linux capabilities can provide setuid-like functionality without SUID bit
- GTFObins documents privilege escalation methods for common binaries
