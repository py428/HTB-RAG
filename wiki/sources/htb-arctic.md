---
type: source
title: "HTB Arctic writeup"
raw: raw/htb-arctic.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[arctic]]
---
# Source: HTB Arctic writeup
> Detailed guide for exploiting ColdFusion 8 including file upload, authentication bypass, and kernel exploitation for SYSTEM access.

## Key facts extracted
- Arctic runs Windows Server 2008 R2 with ColdFusion 8 on TCP 8500
- ColdFusion administrator login uses client-side HMAC-SHA1 hashing with salt
- Directory traversal vulnerability leaks password.properties hash (2F635F6D20E3FDE0C53075A84B68FB07DCEC9B03)
- Password "happyday" cracks instantly, but HMAC bypass works without cracking
- FCKeditor upload bypass filters by using .txt extension with Java archive content-type
- Scheduled tasks feature allows writing webshell from external URL
- MS10-059 chimichurri exploit provides SYSTEM reverse shell
- No Windows hotfixes installed, vulnerable to multiple kernel exploits

## Filed into
[[arctic]], [[directory-traversal]], [[coldfusion]], [[kernel-exploit]]
