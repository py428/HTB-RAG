---
type: source
title: "HTB Beep writeup"
raw: raw/htb-beep.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[beep]]
---
# Source: HTB Beep writeup
> Comprehensive writeup demonstrating five different exploitation paths on an Elastix PBX system, including LFI, webshell upload, and multiple privilege escalation techniques.
## Key facts extracted
- Elastix vtigercrm vulnerable to LFI with null byte injection on PHP 5
- Multiple passwords found: amp109, jEhdIekWmdjE, amp111, passw0rd
- Five distinct paths to root: RCE via 18650.py, webmin login, SSH as root, shellshock, webshell upload
- Webmin credentials work for both web interface and SSH access
- Asterisk user has extensive sudo permissions including nmap and chmod
## Filed into
[[beep]], [[lfi-with-null-byte]], [[sudo-abuse]], [[webmin]], [[shellshock]], [[webshell-upload-smtp]]
