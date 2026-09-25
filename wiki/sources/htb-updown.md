---
type: source
title: "HTB UpDown writeup"
raw: raw/htb-updown.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[updown]]
---
# Source: HTB UpDown writeup
> Comprehensive writeup for HTB UpDown covering git repository exposure, Apache header bypass, PHAR upload for RCE, Python2 input() vulnerability, and easy_install privilege escalation.

## Key facts extracted
- Exposed `.git` repository on `/dev` subdomain contains source code
- Apache `.htaccess` enforces custom header requirement
- File upload allows renamed zip archives to bypass extension filtering
- PHP proc_open not in disable_functions, allows reverse shell
- Setuid binary wraps Python2 script with vulnerable input() function
- Sudo easy_install allows arbitrary code execution as root

## Filed into
[[updown]], [[git-dumper]], [[header-bypass]], [[phar-upload]], [[lfi-phar]], [[python2-input]], [[easy-install-privesc]]
