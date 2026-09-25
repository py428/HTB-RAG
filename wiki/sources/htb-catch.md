---
type: source
title: "HTB Catch writeup"
raw: raw/htb-catch.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[catch]]
---
# Source: HTB Catch writeup
> Catch Global Systems writeup covering Android APK analysis, multiple Cachet CVE exploitation paths (SQL injection, SSTI, Laravel configuration injection), and command injection in APK verification script for privilege escalation.

## Key facts extracted
- Machine: Catch (Medium, Linux)
- Multiple paths to shell via Cachet CVEs (CVE-2021-39165, CVE-2021-39172, CVE-2021-39173, CVE-2021-39174)
- Docker container environment with Ubuntu 20.04
- Android APK contains hardcoded Let's Chat API token
- Cachet running on Laravel framework with vulnerable configuration injection
- Redis abuse for PHP deserialization via phpggc Laravel/RCE4 payload
- APK verification script vulnerable to command injection in name field
- Database credentials: will/s2#4Fg0_%3!

## Filed into
[[catch]], [[apk-reversal]], [[api-token-leak]], [[sqli]], [[ssti]], [[cachet-cve-2021-39172]], [[php-deserialization]], [[redis-abuse]], [[command-injection]]
