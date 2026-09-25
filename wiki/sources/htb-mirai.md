---
type: source
title: "HTB Mirai writeup"
raw: raw/htb-mirai.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[mirai]]
---
# Source: HTB Mirai writeup

> Complete walkthrough of Mirai, an Easy-level Linux box featuring a Raspberry Pi with PiHole that demonstrates the importance of changing default IoT credentials and basic file recovery techniques.

## Key facts extracted
- Device: Raspberry Pi running PiHole network-wide ad blocker
- Default Raspberry Pi credentials: pi:raspberry for SSH access
- Root flag was intentionally deleted and backed up to USB drive
- Multiple recovery methods available: extundelete, grep/strings, and offline analysis
- Box name references the real Mirai malware that targeted IoT devices with default credentials

## Filed into
[[mirai]], [[default-credentials]], [[sudo-abuse]], [[data-recovery]]
