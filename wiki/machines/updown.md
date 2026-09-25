---
type: machine
title: UpDown
platform: htb
os: linux
difficulty: medium
tags: [linux, web, php, python, medium]
solved: 2026-07-09
sources: [[htb-updown]]
related: []
---
# UpDown
> Medium website status checker box featuring git repository exposure, PHP archive (PHAR) upload for RCE, Python2 input() vulnerability, and easy_install privilege escalation.

## Attack path
1. [[git-dumper]] — expose source code from `/dev/.git` repository
2. [[header-bypass]] — add `Special-Dev: only4dev` header to bypass Apache access controls
3. [[phar-upload]] — upload PHP archive with malicious code using allowed file extensions
4. [[lfi-phar]] — trigger code execution via `phar://` wrapper in page parameter
5. [[python2-input]] — exploit eval() in Python2 input() function via setuid binary
6. [[easy-install-privesc]] — abuse sudo easy_install to execute arbitrary Python code as root

## Techniques used
- [[git-dumper]] — Download exposed `.git` repository from web server
- [[header-bypass]] — Bypass Apache `.htaccess` restrictions with custom header
- [[phar-upload]] — Upload PHP code inside zip archive with renamed extension
- [[lfi-phar]] — Local file inclusion using `phar://` stream wrapper to execute code from archive
- [[python2-input]] — Python2 input() function evaluates input as code, allowing RCE
- [[easy-install-privesc]] — sudo easy_install executes setup.py with root privileges

## Tools used
- [[nmap]] — port scanning
- feroxbuster — directory brute forcing
- [[curl]] — HTTP testing and header manipulation
- git-dumper — git repository extraction
- [[python]]2 — vulnerable input() exploitation

## Services / ports
- [[ssh]] — 22/tcp
- [[http]] — 80/tcp (Apache, PHP application)

## Lessons / notes
- `.git` folders on web servers can leak source code
- Apache `.htaccess` can enforce custom headers for access control
- PHAR format allows executing PHP code from within zip archives
- `phar://` wrapper can execute code from uploaded archives
- Python2 input() is equivalent to eval(), making it dangerous
- easy_install runs setup.py, useful for privilege escalation
- PHP disable_functions can often be bypassed with proc_open
