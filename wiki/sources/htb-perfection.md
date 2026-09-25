---
type: source
title: "HTB Perfection writeup"
raw: raw/htb-perfection.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[perfection]]
---
# Source: HTB Perfection writeup
> Ruby web application exploitation featuring newline injection to bypass input filters, server-side template injection for initial access, and hash cracking with custom masks for privilege escalation.

## Key facts extracted
- Target: WEBrick 1.7.0 Ruby server with Sinatra framework
- Vulnerability: ERB SSTI in weighted grade calculator
- Filter bypass: Newline injection (%0a) breaks regex character class validation
- Database: SQLite with SHA256 hashes and password format hints
- Privilege escalation: Sudo access with cracked database password

## Filed into
[[perfection]], [[newline-injection]], [[ssti]], [[hash-cracking]], [[password-reuse]]
