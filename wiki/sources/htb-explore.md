---
type: source
title: "HTB Explore writeup"
raw: raw/htb-explore.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[explore]]
---
# Source: HTB Explore writeup
> First Android HTB box demonstrating CVE-2019-6447 in ES File Explorer and ADB exploitation.

## Key facts extracted
- ES File Explorer exposes file system via JSON API on ports 42135 and 59777
- Password extracted from exfiltrated image file (creds.jpg)
- ADB debug bridge accessible via SSH port forwarding for root shell

## Filed into
[[explore]], [[cve-2019-6447]], [[file-read]], [[adb]]