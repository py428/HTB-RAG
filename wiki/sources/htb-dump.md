---
type: source
title: "HTB Dump writeup"
raw: raw/htb-dump.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[dump]]
---
# Source: HTB Dump writeup
> Linux hard box with packet capture website. Exploitation via wildcard injection in zip download feature, followed by database credential extraction and sudo tcpdump abuse. Writeup covers parameter identification, multiple tcpdump exploitation vectors, and AppArmor restrictions.

## Key facts extracted
- Packet capture website on TCP 80 with login/registration and PCAP management
- Download feature used zip command with wildcard allowing parameter injection
- Identified `-T -TT` injection for command execution via zip testing mechanism
- SQLite database contained plaintext passwords for user authentication
- sudo rules allowed www-data to run tcpdump with specific path patterns
- Multiple tcpdump abuse vectors: file write, file read, sudoers manipulation

## Filed into
[[dump]], [[wildcard-injection]], [[command-injection]], [[sudo-abuse]], [[password-reuse]]
