---
type: source
title: "HTB Bounty writeup"
raw: raw/htb-bounty.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[bounty]]
---
# Source: HTB Bounty writeup
> Windows IIS exploitation with web.config RCE and multiple privilege escalation paths.

## Key facts extracted
- Windows Server 2008 R2 Datacenter with no hotfixes
- IIS 7.5 with ASP.NET, upload form at /transfer.aspx
- UploadedFiles directory cleared every few minutes
- Multiple valid exploits: MS10-073, MS10-092, MS11-046, MS12-042, MS13-005, MS15-051, MS16-014

## Filed into
[[bounty]], [[web-config-rce]], [[null-byte-upload-bypass]], [[lonely-potato]], [[kernel-exploit]]
