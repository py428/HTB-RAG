---
type: source
title: "HTB Cereal writeup"
raw: raw/htb-cereal.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[cereal]]
---
# Source: HTB Cereal writeup
> C#/.NET application with React frontend writeup covering Git exposure, JWT forging, XSS to deserialization chain, SQLite database extraction, and GraphQL SSRF exploitation with GenericPotato for SYSTEM privilege escalation.

## Key facts extracted
- Machine: Cereal (Hard, Windows)
- ASP.NET backend with React frontend
- Exposed .git repository with JWT secret leak
- React XSS via react-marked-markdown vulnerability
- JSON.NET deserialization with DownloadHelper gadget
- SQLite database with sonny credentials
- GraphQL SSRF via updatePlant mutation
- SeImpersonatePrivilege with GenericPotato exploitation
- Windows Server Core without Print Spooler service

## Filed into
[[cereal]], [[git-exposure]], [[jwt-forging]], [[xss]], [[deserialization]], [[sqlite-sqli]], [[hash-cracking]], [[graphql-ssrf]], [[generic-potato]], [[named-pipe-impersonation]]
