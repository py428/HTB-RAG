---
type: source
title: "HTB Sandworm writeup"
raw: raw/htb-sandworm.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[sandworm]]
---
# Source: HTB Sandworm writeup

> Comprehensive guide to exploiting SSTI in PGP signature verification, escaping Firejail jail through Rust code hijacking, and leveraging CVE-2022-31214 for root access.

## Key facts extracted

- Flask application with PGP encryption demos vulnerable to Jinja2 SSTI in signature verification
- Custom GPG key with SSTI payload in username field executes code when signature is verified
- Firejail jail with restricted binaries, atlas user runs Flask application
- httpie config泄露 silentobserver credentials: `quietLiketheWind22`
- Cron job builds Rust tipnet application every two minutes as atlas
- CVE-2022-31214 in Firejail 0.9.68 allows root escape via join functionality
- MySQL credentials: atlas/GarlicAndOnionZ42, tipnet/4The_Greater_GoodJ4A

## Filed into

[[sandworm]], [[ssti]], [[jail-escape]], [[cargo-hijack]], [[cve-2022-31214]]
