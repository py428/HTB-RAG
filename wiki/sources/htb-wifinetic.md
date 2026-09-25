---
type: source
title: "HTB Wifinetic writeup"
raw: raw/htb-wifinetic.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[wifinetic]]
---
# Source: HTB Wifinetic writeup
> Introduction to wireless network exploitation covering anonymous FTP reconnaissance, OpenWRT configuration analysis, WPA/WPS cracking with reaver, and password reuse for lateral movement on an easy Linux box.

## Key facts extracted
- Anonymous FTP contains OpenWRT backup files with wireless configuration
- WPA PSK: VeRyUniUqWiFIPasswrd1!
- WPS PIN: 12345670 (default)
- Root password: WhatIsRealAnDWhAtIsNot51121!
- Reaver has CAP_NET_RAW capability for wireless attacks
- Multiple virtual wireless interfaces configured on the host

## Filed into
[[wifinetic]], [[anonymous-ftp]], [[config-file-analysis]], [[password-reuse]], [[wps-pixie-dust]], [[openwrt]], [[wireless-security]]
