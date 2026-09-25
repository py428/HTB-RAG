---
type: source
title: "HTB WifineticTwo writeup"
raw: raw/htb-wifinetictwo.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[wifinetictwo]]
---
# Source: HTB WifineticTwo writeup
> Comprehensive guide covering OpenPLC CVE-2021-31630 exploitation, wireless network scanning and WPS pixie dust attacks, WiFi connection techniques, chisel port forwarding, and multiple privilege escalation paths against OpenWRT.

## Key facts extracted
- OpenPLC v3 vulnerable to CVE-2021-31630 command injection in hardware layer
- Default OpenPLC credentials: openplc:openplc
- Wireless network: plcrouter with WPS enabled
- WPA PSK: NoWWEDoKnowWhaTisReal123!
- WPS PIN: 12345670 (default)
- OpenWRT root password: empty by default
- Multiple paths to root: cron jobs, SSH key upload, SSH with empty password

## Filed into
[[wifinetictwo]], [[cve-2021-31630]], [[wireless-scanning]], [[wps-pixie-dust]], [[wifi-connection]], [[port-forwarding]], [[default-credentials]], [[cron-job-abuse]], [[ssh-key-abuse]], [[openplc]], [[openwrt]], [[ci-cd-build-exploitation]]
