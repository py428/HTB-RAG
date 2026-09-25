---
type: source
title: "HTB Napper writeup"
raw: raw/htb-napper.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[napper]]
---
# Source: HTB Napper writeup
> Hard-difficulty Windows box with IIS backdoor exploitation, custom malware reverse engineering, and Elastic database-based LAPS password extraction.

## Key facts extracted
- Internal blog post credentials: example:ExamplePassword for HTTP basic auth
- Blog documented real IIS malware Naplistener with backdoor details
- Custom IIS helper modified original malware for HTB environment  
- Hugo-based static sites with internal draft post about custom LAPS solution
- Elastic database running on localhost:9200 with credentials user:DumpPassword$Here
- Custom LAPS script generates random password, encrypts with seed-derived key, stores in Elastic
- Go binary a.exe performs password rotation every 5 minutes via scheduled task
- Password encryption uses AES-CFB with IV and key derived from random seed

## Filed into
[[napper]], [[iis-backdoor]], [[dotnet-reverse-shell]], [[elastic-database]], [[custom-laps]], [[uac-bypass]]