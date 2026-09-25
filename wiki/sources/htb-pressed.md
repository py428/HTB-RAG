---
type: source
title: "HTB Pressed writeup"
raw: raw/htb-pressed.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[pressed]]
---
# Source: HTB Pressed writeup
> Detailed writeup of Pressed, a Hard WordPress box featuring XML-RPC abuse for 2FA bypass, webshell injection via PHPeverywhere plugin, and PwnKit privilege escalation.

## Key facts extracted
- WordPress 5.9 on Apache 2.4.41 (Ubuntu 20.04)
- wp-config.php.bak leaked database credentials: admin/uhc-jan-finals-2022
- XML-RPC enabled at xmlrpc.php with custom htb.get_flag method
- PHPEverywhere plugin executing PHP code within posts
- PwnKit (CVE-2021-4034) vulnerable pkexec binary
- Firewall blocking outbound connections
- Custom method htb.get_flag returned user flag via XML-RPC

## Filed into
[[pressed]], [[config-file-leak]], [[xml-rpc-abuse]], [[webshell-injection]], [[pwnkit]], [[iptables-modification]]
