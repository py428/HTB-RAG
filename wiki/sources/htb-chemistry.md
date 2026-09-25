---
type: source
title: "HTB Chemistry writeup"
raw: raw/htb-chemistry.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[chemistry]]
---
# Source: HTB Chemistry writeup
> Exploitation of pymatgen CIF file parser deserialization vulnerability for initial access, followed by database hash cracking, SSH tunneling to internal AIOHTTP service, and directory traversal for root SSH key.

## Key facts extracted
- Flask website processes Crystallographic Information Files (CIF)
- pymatgen CVE-2024-23346 allows RCE via eval injection in transformation string
- SQLite database contains MD5 hashes of user passwords
- Internal AIOHTTP monitoring site on TCP 8080 blocked by iptables for app user
- AIOHTTP CVE-2024-23334 allows reading files via static assets with follow_symlinks=True

## Filed into
[[chemistry]], [[deserialization]], [[ssh-tunnel]], [[directory-traversal]]
