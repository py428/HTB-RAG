---
type: source
title: "HTB Static writeup"
raw: raw/htb-static.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[static]]
---
# Source: HTB Static writeup
> Comprehensive writeup covering advanced exploitation chain: gzip recovery for TOTP seed, VPN pivot, Xdebug RCE, PHP-FPM exploitation, and format string privilege escalation.
## Key facts extracted
- Corrupted gzipped SQL backup contains recoverable TOTP seed
- NTP server allows time synchronization for TOTP validation
- VPN access provides internal network pivot (172.20.0.0/16)
- Xdebug enabled on internal PHP server with remote debugging
- CVE-2019-11043: PHP-FPM fastcgi_split_path_info vulnerability
- easy-rsa tool has format string vulnerability in print function
- easy-rsa calls openssl without full path (path hijack)

## Filed into
[[static]], [[gzip-recovery]], [[ntp-sync]], [[totp-bypass]], [[vpn-pivot]], [[xdebug-rce]], [[cve-2019-11043]], [[format-string-exploit]]
