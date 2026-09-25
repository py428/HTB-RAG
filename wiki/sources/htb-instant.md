---
type: source
title: "HTB Instant writeup"
raw: raw/htb-instant.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[instant]]
---
# Source: HTB Instant writeup
> Comprehensive guide covering Android APK reverse engineering, JWT authentication abuse, file read vulnerabilities, and SolarPuTTY credential decryption.

## Key facts extracted
- Android app contains hardcoded admin JWT with expiration in 3023
- Swagger UI exposes admin API endpoints with file read functionality
- SQLite database contains Werkzeug password hashes
- SolarPuTTY sessions file encrypted with password-crackable encryption

## Filed into
[[instant]], [[apk-reversing]], [[jwt-hardcoded]], [[directory-traversal]], [[solarputty-decrypt]], [[sqlite-extraction]]
